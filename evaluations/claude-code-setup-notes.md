# Claude Code Setup Notes

**Date:** Dec 25, 2025  
**Purpose:** Documentation for setting up Claude Code for skill evaluation and testing

---

## System Requirements

- **OS**: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
- **Hardware**: 4 GB+ RAM
- **Software**: Node.js 18+ (only for npm installation)
- **Network**: Internet connection required for authentication and AI processing
- **Shell**: Works best in Bash, Zsh or Fish
- **Location**: Anthropic supported countries

---

## Installation Methods

### Native Install (Recommended)

**macOS, Linux, WSL:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

### Alternative: NPM Installation
```bash
npm install -g @anthropic-ai/claude-code
```

---

## Starting Claude Code

After installation:
```bash
cd your-project-directory
claude
```

---

## Authentication Options

1. **Claude Console** (Default): OAuth through Anthropic console, requires active billing
2. **Claude App (Pro/Max plan)**: Unified subscription for Claude Code + web interface
3. **Enterprise platforms**: AWS Bedrock, Google Vertex AI, or Microsoft Foundry

---

## Key Commands

- `claude` - Start Claude Code in current directory
- `claude update` - Manually update Claude Code
- `claude doctor` - Check installation type and version
- `claude install` - Migrate to native binary installation
- `/config` - Configure Claude Code settings
- `/init` - Initialize CLAUDE.md file for project

---

## For Our Use Case: Skill Testing

### What We Need Claude Code For:
1. **Activation Rate Testing** - Run 10 test prompts per skill to see if skills activate
2. **Task Completion Testing** - Execute 5-10 real tasks to measure success rate
3. **Output Consistency Testing** - Run same test 3 times to check consistency
4. **Token Tracking** - Monitor token consumption during skill execution

### Key Files for Skill Testing:
- **CLAUDE.md** - Project-specific configuration (created with `/init`)
- **Skills location** - Skills can be installed globally or per-project
- **Test prompts** - We'll need to create test cases for each skill

---

## Next Steps for Setup:
1. Install Claude Code on user's machine
2. Authenticate with Claude Console or Pro/Max account
3. Set up test project directory for skill evaluation
4. Install skills from Anthropic's GitHub repo
5. Create test prompt templates for evaluation framework
