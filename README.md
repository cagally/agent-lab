# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 1 - Skill Acquisition & Testing Setup

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
│   ├── skillsmp-top12-skills.json     # ⭐ Master list of top 12 skills
│   ├── skillsmp-reconnaissance.md     # SkillsMP analysis & strategy
│   └── raw-skills/                    # ⭐ Downloaded SKILL.md files (12 skills)
├── evaluations/          # Evaluation framework, scorecards, test results
│   ├── framework-v2-final.md          # ⭐ FINAL research-validated framework
│   ├── metrics-validation.md          # User research analysis
│   ├── testing-methodology.md         # Practical testing guide
│   ├── claude-code-setup-notes.md     # ⭐ Claude Code setup guide
│   └── claude-code-skill-testing-guide.md  # ⭐ How to test skills
├── scripts/              # ⭐ NEW - Automation scripts
│   ├── install-skills-to-claude.sh    # ⭐ Install skills to Claude Code
│   ├── skillsmp-scraper.py            # HTML scraper (needs Selenium)
│   └── scrape-skillsmp-browser.py     # Browser-based scraper
├── website/              # Website code, designs, deployment configs
├── branding/             # Brand guidelines, visual assets, messaging
├── gtm/                  # Go-to-market strategy, content, campaigns
├── operations/           # SOPs, workflows, business operations
└── README.md            # This file - project status and navigation
```

---

## 🎯 Current Status

**Last Updated:** Dec 25, 2025 - Session 3

### ✅ Completed

**Previous Sessions:**
- Repository structure established with organized folders
- Project vision documented
- Knowledge base protocol defined
- **Evaluation framework v1.0 designed** (5 dimensions)
- **Deep user research conducted** (Reddit, GitHub, blogs, competitive analysis)
- **Evaluation framework v2.0 finalized** (6 research-validated metrics)
- **Testing methodology designed** (3-day implementation plan)
- GitHub authentication configured and working

**This Session (Dec 25):**
- ✅ **SkillsMP reconnaissance completed** - Analyzed structure, identified top skills
- ✅ **Top 12 skills downloaded** from PyTorch (4), OpenAI (2), Anthropic (6)
- ✅ **Claude Code setup completed** - User environment configured on macOS
- ✅ **Installation script created** - `install-skills-to-claude.sh`
- ✅ **Skills metadata tracked** - Complete JSON with GitHub links, stars, descriptions
- ✅ **All work committed to GitHub** - Repository up to date

### 🚧 In Progress

- **User Action Required:** Install skills to Claude Code for manual testing
- **Next:** Run evaluation tests on top 12 skills

### 📋 Next Steps

1. **User installs skills to Claude Code:**
   ```bash
   cd ~/agent-lab
   ./scripts/install-skills-to-claude.sh --all
   ```

2. **User launches Claude Code and verifies:**
   ```bash
   cd ~/agent-lab
   claude
   # Then ask: "What skills are available?"
   ```

3. **User runs manual evaluation tests:**
   - Activation Rate (10 test prompts per skill)
   - Task Completion Rate
   - Output Consistency (3 runs per test)
   - Token usage tracking

4. **Document evaluation results** in `evaluations/skillsmp-evaluation-results.json`

5. **Analyze results and create skill scorecards**

6. **Build MVP website** with top evaluated skills

---

## 📊 Skills Inventory (Top 12)

| Rank | Skill | Stars | Repository | Status |
|------|-------|-------|------------|--------|
| 1 | at-dispatch-v2 | 95.4k | pytorch/pytorch | ✅ Downloaded |
| 2 | add-uint-support | 95.4k | pytorch/pytorch | ✅ Downloaded |
| 3 | skill-writer | 95.4k | pytorch/pytorch | ✅ Downloaded |
| 4 | docstring | 95.4k | pytorch/pytorch | ✅ Downloaded |
| 5 | skill-creator | 54.5k | openai/codex | ✅ Downloaded |
| 6 | skill-installer | 54.5k | openai/codex | ✅ Downloaded |
| 7 | frontend-design | 47.9k | anthropics/claude-code | ✅ Downloaded |
| 8 | hook-development | 47.9k | anthropics/claude-code | ✅ Downloaded |
| 9 | command-development | 47.9k | anthropics/claude-code | ✅ Downloaded |
| 10 | agent-identifier | 47.9k | anthropics/claude-code | ✅ Downloaded |
| 11 | rule-identifier | 47.9k | anthropics/claude-code | ✅ Downloaded |
| 12 | mcp-integration | 47.9k | anthropics/claude-code | ✅ Downloaded |

**All skill files available in:** `skills-data/raw-skills/`

---

## 🔬 Research Insights

### Key Findings:
- **#1 User Complaint:** Skills won't activate (Activation Rate is critical)
- **#2 User Complaint:** Token waste and cost inefficiency
- **#3 User Complaint:** Unpredictable/inconsistent outputs
- **Hidden Issue:** Context limit (15k chars) silently breaks skills - users have NO idea
- **Competitive Gap:** SkillsMP (33,132 skills) just aggregates - NO ONE tests skills
- **Our Moat:** We will be the FIRST to actually test and validate skills

### Final Metrics (6):
1. **Activation Rate** (0-10) - Does it trigger when needed?
2. **Task Completion Rate** (0-10) - Does it work reliably?
3. **Output Consistency** (0-10) - Same input = same output?
4. **Token Efficiency** (0-10) - Cost-effective?
5. **Description Efficiency** (0-10) - Fits in context budget?
6. **Maintenance Status** (0-10) - Actively maintained?

---

## 🧠 Knowledge Base Protocol

### Session Start
1. Read this README for latest status
2. Navigate to relevant project folder for your task
3. Review existing files before creating new ones

### During Session
- Create and update files in appropriate folders
- Build on existing context - no reinventing
- Keep files organized and well-named

### Session End
1. Update this README with:
   - **Completed:** What you accomplished
   - **In-Progress:** Current status
   - **Next Steps:** What happens next
2. Commit and push all changes with clear message

---

## 🚀 Quick Links

- **Vision Doc:** `/home/ubuntu/projects/agent-lab-2b9b282d/Agent Skills Platform V.0001.md`
- **Evaluation Framework v2.0:** `/evaluations/framework-v2-final.md` ⭐
- **Testing Methodology:** `/evaluations/testing-methodology.md`
- **User Research:** `/evaluations/user-research-notes.md`
- **Skills Metadata:** `/skills-data/skillsmp-top12-skills.json` ⭐
- **SkillsMP Analysis:** `/skills-data/skillsmp-reconnaissance.md` ⭐
- **Anthropic Skills:** https://github.com/anthropics/skills
- **Claude Skills Docs:** https://code.claude.com/docs/en/skills
- **Competitor (SkillsMP):** https://skillsmp.com/

---

## 📊 Key Metrics & Goals

- **Target:** 20-50 evaluated skills at launch (started with top 12)
- **Timeline:** 3 days to MVP
- **Quality Bar:** Non-technical users can understand and use every skill
- **First Mover Advantage:** Speed is critical
- **Competitive Moat:** Testing > Aggregating

---

*This is our shared brain. Any agent can pick up where another left off.*
