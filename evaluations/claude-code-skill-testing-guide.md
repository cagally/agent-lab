# Claude Code Skill Testing Guide

**Date:** Dec 25, 2025  
**Purpose:** Complete guide for using Claude Code to test and evaluate agent skills

---

## How Skills Work in Claude Code

### Key Concepts

**Skills are Model-Invoked**: Claude autonomously decides when to use skills based on your request and the skill's description. This is different from slash commands which are user-invoked.

**Skill Structure**: Each skill consists of:
- `SKILL.md` file (required) - Contains YAML frontmatter + instructions
- Optional supporting files (scripts, templates, documentation)

**Skill Locations**:
- **Personal Skills**: `~/.claude/skills/` (available across all projects)
- **Project Skills**: `.claude/skills/` (shared with team via git)
- **Plugin Skills**: Bundled with installed plugins

---

## Installing Skills for Testing

### Method 1: Manual Installation (Recommended for Testing)

**For Personal Skills:**
```bash
mkdir -p ~/.claude/skills/skill-name
# Copy SKILL.md and supporting files into this directory
```

**For Project Skills:**
```bash
mkdir -p .claude/skills/skill-name
# Copy SKILL.md and supporting files into this directory
```

### Method 2: Clone from Anthropic's GitHub

We'll pull skills from: https://github.com/anthropics/skills

```bash
# Clone the skills repository
git clone https://github.com/anthropics/skills.git

# Copy individual skills to Claude Code
cp -r skills/skill-name ~/.claude/skills/skill-name
```

---

## Testing Skills for Our Evaluation Framework

### 1. Activation Rate Testing

**Goal**: Measure if skills activate when they should (80% target)

**Process**:
1. Create 10 test prompts that SHOULD trigger the skill based on its description
2. Run each prompt in Claude Code
3. Observe if skill activates (Claude will mention using the skill)
4. Count successes: Activation Rate = (Successes / 10) × 100%

**Example Test Prompts Template**:
```
For a "data-analyzer" skill:
1. "Can you analyze this CSV file?"
2. "I need to create a chart from this data"
3. "Help me visualize these statistics"
4. "What patterns do you see in this dataset?"
5. "Generate a summary report of this data"
... (10 total)
```

**How to Check if Skill Activated**:
- Claude will explicitly mention using the skill in its response
- Look for phrases like "I'll use the [skill-name] skill to..."
- Check Claude's reasoning/thinking output

---

### 2. Task Completion Rate Testing

**Goal**: Measure if skills successfully complete their stated tasks

**Process**:
1. Define 5-10 tasks the skill claims to handle
2. Execute each task using the skill
3. Evaluate if output meets expectations
4. Count full successes (partial = failure)
5. Task Completion Rate = (Successes / Total) × 100%

**Success Criteria**:
- Task completes without errors
- Output matches expected format
- Results are accurate and useful
- No manual intervention needed

---

### 3. Output Consistency Testing

**Goal**: Measure if skills produce similar outputs for same inputs

**Process**:
1. Select 3-5 representative test cases
2. Run each test case 3 times
3. Compare outputs for similarity
4. Calculate consistency score:
   - Identical outputs = 100%
   - Functionally equivalent = 80%
   - Similar but different = 60%
   - Completely different = 0%
5. Average across all test cases

---

### 4. Token Tracking

**Goal**: Measure token consumption during skill execution

**Process**:
1. Run 5 typical tasks with the skill
2. Track tokens used (input + output)
3. Calculate average tokens per task
4. Compare to baseline (same task without skill)
5. Calculate overhead percentage

**Note**: Claude Code shows token usage in the interface after each response

---

## Viewing Available Skills

**Ask Claude directly**:
```
What Skills are available?
```

**Check filesystem**:
```bash
# List personal skills
ls ~/.claude/skills/

# List project skills
ls .claude/skills/

# View specific skill
cat ~/.claude/skills/skill-name/SKILL.md
```

---

## Debugging Skills That Don't Activate

### Common Issues:

**1. Vague Description**
- ❌ Bad: "Helps with documents"
- ✅ Good: "Extract text and tables from PDF files. Use when working with PDFs or document extraction."

**2. Wrong File Path**
- Verify: `ls ~/.claude/skills/skill-name/SKILL.md`

**3. Invalid YAML Syntax**
- Check frontmatter: `cat SKILL.md | head -n 10`
- Ensure `---` on line 1 and closing `---` before content

**4. View Errors**
- Run with debug mode: `claude --debug`

---

## SKILL.md Format

```yaml
---
name: skill-name
description: Brief description of what this skill does and when to use it
---

# Skill Name

## Instructions
Step-by-step guidance for Claude

## Examples
Concrete examples of using this skill
```

**Field Requirements**:
- `name`: Lowercase letters, numbers, hyphens only (max 64 chars)
- `description`: What it does + when to use it (max 1024 chars)

---

## Testing Workflow for Our Project

### Phase 1: Setup (30 min)
1. Install Claude Code on your machine
2. Authenticate with Claude account
3. Clone Anthropic's skills repository
4. Create test project directory

### Phase 2: Skill Installation (1 hour)
1. Select 20-50 skills from Anthropic's repo
2. Copy skills to `~/.claude/skills/` for testing
3. Verify skills load correctly: `claude` → "What skills are available?"

### Phase 3: Automated Analysis (2 hours)
1. Extract skill metadata (description length, YAML structure)
2. Run GPT-based analysis on descriptions
3. Identify activation methods (keyword vs organic)
4. Calculate description efficiency metrics

### Phase 4: Manual Testing (6-8 hours)
1. Test top 10-15 skills based on automated scores
2. Run activation tests (10 prompts per skill)
3. Run task completion tests (5-10 tasks per skill)
4. Run consistency tests (3 runs per test case)
5. Track token usage across all tests

### Phase 5: Data Collection (2 hours)
1. Compile all test results
2. Generate scorecards in JSON format
3. Create user-facing summaries
4. Validate automated vs manual scores

---

## Key Commands for Testing

```bash
# Start Claude Code
claude

# Start with debug mode
claude --debug

# Check installation
claude doctor

# Update Claude Code
claude update

# View skills
ls ~/.claude/skills/

# Test a skill
# Just ask Claude a question that should trigger it
```

---

## Next Steps for You

1. **Install Claude Code** using the native installer
2. **Authenticate** with your Claude account (Pro/Max or Console)
3. **Clone Anthropic's skills repo**: `git clone https://github.com/anthropics/skills.git`
4. **Create test directory**: `mkdir ~/skill-testing && cd ~/skill-testing`
5. **Copy first skill** to test: `cp -r ~/skills/[skill-name] ~/.claude/skills/`
6. **Start Claude Code**: `claude`
7. **Test skill activation**: Ask relevant questions and observe behavior

---

## Questions to Clarify

Before we proceed, I need to know:

1. **What OS are you using?** (macOS, Linux, or Windows)
2. **Do you have Node.js installed?** (Check with `node --version`)
3. **Do you have a Claude Pro/Max subscription or API access?**
4. **Are you comfortable with command line?** (We'll need terminal access)

Let me know these details and I'll create a step-by-step setup guide tailored to your environment.
