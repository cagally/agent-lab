#!/bin/bash
#
# Install Agent Skills to Claude Code
#
# Usage:
#   ./install-skills-to-claude.sh [--all | skill1 skill2 ...]
#
# Examples:
#   ./install-skills-to-claude.sh --all                    # Install all skills
#   ./install-skills-to-claude.sh pytorch-at-dispatch-v2   # Install specific skill
#

set -e

SKILLS_SOURCE="/home/ubuntu/agent-lab/skills-data/raw-skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🚀 Claude Code Skills Installer"
echo "================================"
echo

# Create Claude skills directory if it doesn't exist
if [ ! -d "$CLAUDE_SKILLS_DIR" ]; then
    echo -e "${YELLOW}📁 Creating Claude skills directory...${NC}"
    mkdir -p "$CLAUDE_SKILLS_DIR"
    echo -e "${GREEN}✅ Created: $CLAUDE_SKILLS_DIR${NC}"
    echo
fi

# Function to install a single skill
install_skill() {
    local skill_name=$1
    local source_path="$SKILLS_SOURCE/$skill_name"
    local dest_path="$CLAUDE_SKILLS_DIR/$skill_name"
    
    if [ ! -d "$source_path" ]; then
        echo -e "${RED}❌ Skill not found: $skill_name${NC}"
        return 1
    fi
    
    if [ ! -f "$source_path/SKILL.md" ]; then
        echo -e "${RED}❌ No SKILL.md found in: $skill_name${NC}"
        return 1
    fi
    
    # Copy skill directory
    cp -r "$source_path" "$dest_path"
    echo -e "${GREEN}✅ Installed: $skill_name${NC}"
    return 0
}

# Parse arguments
if [ $# -eq 0 ] || [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: $0 [--all | skill1 skill2 ...]"
    echo
    echo "Available skills:"
    ls -1 "$SKILLS_SOURCE" | sed 's/^/  - /'
    exit 0
fi

if [ "$1" == "--all" ]; then
    echo "📦 Installing all skills..."
    echo
    
    installed=0
    failed=0
    
    for skill_dir in "$SKILLS_SOURCE"/*; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            if install_skill "$skill_name"; then
                ((installed++))
            else
                ((failed++))
            fi
        fi
    done
    
    echo
    echo "================================"
    echo -e "${GREEN}✅ Installed: $installed skills${NC}"
    if [ $failed -gt 0 ]; then
        echo -e "${RED}❌ Failed: $failed skills${NC}"
    fi
else
    echo "📦 Installing specified skills..."
    echo
    
    installed=0
    failed=0
    
    for skill_name in "$@"; do
        if install_skill "$skill_name"; then
            ((installed++))
        else
            ((failed++))
        fi
    done
    
    echo
    echo "================================"
    echo -e "${GREEN}✅ Installed: $installed skills${NC}"
    if [ $failed -gt 0 ]; then
        echo -e "${RED}❌ Failed: $failed skills${NC}"
    fi
fi

echo
echo "💡 Next steps:"
echo "   1. Launch Claude Code: cd ~/agent-lab && claude"
echo "   2. Verify skills: Ask 'What skills are available?'"
echo "   3. Start testing!"
echo
