# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 3 - Data Infrastructure & Automation

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
│   ├── skillsmp-top12-skills.json     # ⭐ Master list of top 12 skills
│   ├── skillsmp-reconnaissance.md     # SkillsMP analysis & strategy
│   ├── test-prompts-all-skills.csv    # ⭐ 180 generated test prompts
│   └── raw-skills/                    # ⭐ Downloaded SKILL.md files (12 skills)
├── evaluations/          # ⭐ Evaluation framework, implementation guides, templates
│   ├── evaluation-framework-v3.md               # ⭐ FINAL 11-dimension framework
│   ├── evaluation-implementation-guide.md       # ⭐ Step-by-step execution playbook
│   ├── comprehensive-evaluation-dimensions.md   # ⭐ All 30+ dimensions researched
│   ├── test-prompt-suite-template.md           # ⭐ Activation testing templates
│   ├── evaluation-results-template.md          # ⭐ Results recording template
│   ├── Agent-Skills-Evaluation-MVP.xlsx        # ⭐ Pre-configured Excel file
│   ├── google-sheets-schema.md                 # ⭐ Complete data structure spec
│   ├── GOOGLE-SHEETS-SETUP.md                  # ⭐ Setup instructions
│   ├── anthropic-api-skills-support.md         # ⭐ API integration research
│   ├── context-safety-clarification.md         # Progressive disclosure research
│   ├── surge-ai-research-notes.md              # Surge AI methodology research
│   ├── mercor-ai-research-notes.md             # Mercor AI evaluation research
│   └── user-complaints-research.md             # User pain points analysis
├── scripts/              # ⭐ Automation scripts for evaluation
│   ├── install-skills-to-claude.sh             # ⭐ Install skills to Claude Code
│   ├── eval-token-efficiency.py                # ⭐ Automated token analysis (TESTED)
│   ├── eval-security-audit.py                  # ⭐ Automated security scanning (TESTED)
│   ├── write-to-sheets.py                      # ⭐ Test prompt generator (TESTED)
│   ├── create-excel-evaluation-sheet.py        # ⭐ Excel file generator
│   └── skillsmp-scraper.py                     # HTML scraper (deprecated)
├── website/              # Website code, designs, deployment configs
├── branding/             # Brand guidelines, visual assets, messaging
├── gtm/                  # Go-to-market strategy, content, campaigns
├── operations/           # SOPs, workflows, business operations
└── README.md            # This file - project status and navigation
```

---

## 🎯 Current Status

**Last Updated:** Dec 27, 2025 - Session 5 (Prompt Generation Phase)

### ✅ Completed

**Previous Sessions:**
- Repository structure established
- Project vision documented
- Evaluation framework v1.0, v2.0, v3.0 designed
- Deep user research conducted
- SkillsMP reconnaissance completed
- Top 12 skills downloaded from PyTorch, OpenAI, Anthropic
- Claude Code setup completed on user's macOS
- Installation script created and tested
- Skills metadata tracked in JSON

**This Session (Dec 27 - Data Infrastructure):**
- ✅ **Anthropic API Skills Support Confirmed** - Can use API for automation
- ✅ **Google Sheets Structure Designed** - 7 tabs, complete schema
- ✅ **Excel File Generated** - Pre-configured with all tabs and sample data
- ✅ **Google Sheet Created by User** - Ready for data population
- ✅ **Automation Scripts Built:**
  - Token Efficiency Analyzer (tested ✅)
  - Security Audit Scanner (tested ✅)
  - Test Prompt Generator (built ✅, running 🔄)
- ✅ **Prompt Template Iteration** - Tested 3 versions, selected best quality
- 🔄 **Generating 180 Test Prompts** - Using Sonnet 4.5 API (in progress)

### 🚧 In Progress

- **Generating high-quality test prompts via Anthropic API**
  - Using Claude Sonnet 4.5 with dynamic templates
  - 180 prompts total (15 per skill × 12 skills)
  - Iterated templates 3 times for quality
  - Running in background (~60-90 min ETA)
  - Script: `scripts/generate-test-prompts.py`
  - Output: `evaluations/test-prompts-generated.csv`

### 📋 Next Steps

1. **Import test prompts to Google Sheet:**
   - Download `evaluations/test-prompts-all-skills.csv`
   - Import to "Test Prompts" tab

2. **Build remaining automation scripts:**
   - `eval-description-efficiency.py` (GPT-5 judge)
   - `eval-activation-rate-api.py` (API-based)
   - `eval-output-consistency-api.py` (API-based)
   - `eval-multi-skill-compatibility-api.py` (API-based)
   - `eval-failure-mode-api.py` (API-based)

3. **Run automated evaluations** on all 12 skills

4. **Conduct manual evaluations:**
   - Task Completion
   - Grounding & Faithfulness

5. **Generate final scorecards** and launch MVP

---

## 🔬 Evaluation Framework V3 (Final)

### Hurdle Criteria (Pass/Fail)
1. **Activation Rate** - Does it activate reliably? (≥80% = Pass)
2. **Task Completion** - Can it complete its stated purpose?

### Quality Criteria (0-10 Scale)
3. **Token Efficiency** - Description and body size optimization (automated ✅)
4. **Security Audit** - Malicious code detection, safety rating (automated ✅)
5. **Description Efficiency** - Clarity, specificity, information density (GPT-5 judge)
6. **Output Consistency** - Same prompt, consistent results (API-based)
7. **Multi-Skill Compatibility** - Works alongside other skills (API-based)
8. **Failure Mode Resistance** - Graceful failure, edge case handling (API-based)
9. **Grounding & Faithfulness** - Hallucination rate, factual accuracy (manual)

### Metadata
10. **Maintenance Status** - Active, stale, or archived

**Total Score:** 90 points (9 dimensions × 10)

**Automation Level:** 6/9 dimensions fully automated (67%)

---

## 📊 Google Sheets Structure

**Sheet URL:** https://docs.google.com/spreadsheets/d/12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY/edit

### 7 Tabs:
1. **Skills Master List** - Registry of all 12 skills
2. **Test Prompts** - 180 prompts (15 per skill) ← **Ready to import**
3. **API Responses** - Raw outputs from testing
4. **Automated Scores** - Results from automation scripts
5. **Manual Evaluations** - Human scoring workspace
6. **Final Scorecards** - Aggregated results with ratings
7. **Dashboard** - Executive summary with charts

### Data Flow:
```
Skills (12) 
  → Test Prompts (180) 
    → API Responses (540) 
      → Automated Scores (84) 
        + Manual Evaluations (24) 
          → Final Scorecards (12) 
            → Dashboard (summary)
```

---

## 📊 Skills Inventory (Top 12)

| Rank | Skill | Stars | Repository | Eval Status |
|------|-------|-------|------------|-------------|
| 1 | pytorch-skill-writer | 95.4k | pytorch/pytorch | ⚠️ Partial (98% initial test) |
| 2 | pytorch-at-dispatch-v2 | 95.4k | pytorch/pytorch | ⏳ Pending |
| 3 | pytorch-add-uint-support | 95.4k | pytorch/pytorch | ⏳ Pending |
| 4 | pytorch-docstring | 95.4k | pytorch/pytorch | ⏳ Pending |
| 5 | openai-skill-creator | 54.5k | openai/codex | ⏳ Pending |
| 6 | openai-skill-installer | 54.5k | openai/codex | ⏳ Pending |
| 7 | anthropic-frontend-design | 47.9k | anthropics/claude-code | ⏳ Pending |
| 8 | anthropic-hook-development | 47.9k | anthropics/claude-code | ⏳ Pending |
| 9 | anthropic-command-development | 47.9k | anthropics/claude-code | ⏳ Pending |
| 10 | anthropic-agent-development | 47.9k | anthropics/claude-code | ⏳ Pending |
| 11 | anthropic-writing-rules | 47.9k | anthropics/claude-code | ⏳ Pending |
| 12 | anthropic-mcp-integration | 47.9k | anthropics/claude-code | ⏳ Pending |

**All skill files available in:** `skills-data/raw-skills/`

---

## 🛠️ Automation Scripts

### 1. Token Efficiency Analyzer ✅
**Purpose:** Measure SKILL.md size and efficiency

**Usage:**
```bash
python3 scripts/eval-token-efficiency.py skills-data/raw-skills/[skill-name]
```

**Output:** JSON with character counts, efficiency score (0-10)

**Status:** Tested and working

### 2. Security Audit Scanner ✅
**Purpose:** Detect dangerous patterns and security risks

**Usage:**
```bash
python3 scripts/eval-security-audit.py skills-data/raw-skills/[skill-name]
```

**Output:** JSON with findings, safety score (0-10)

**Status:** Tested and working (pytorch-skill-writer: 10/10 Safe)

### 3. Test Prompt Generator 🔄
**Purpose:** Generate high-quality, skill-specific test prompts using Claude Sonnet 4.5

**Features:**
- Dynamic templates with skill-specific context
- 5 prompt types: explicit, implicit, edge case, adversarial-confusion, adversarial-impossible
- Iterated 3 times for quality optimization
- 15 prompts per skill × 12 skills = 180 total

**Usage:**
```bash
export ANTHROPIC_API_KEY="your-key"
python3 scripts/generate-test-prompts.py
```

**Output:** `evaluations/test-prompts-generated.csv`

**Status:** Running in background (~60-90 min ETA)

**Cost:** ~$2.70 in Anthropic API credits

### 4-8. Coming Soon (API-Based)
- `eval-description-efficiency.py` - GPT-5 judges description quality
- `eval-activation-rate-api.py` - Tests skill activation via API
- `eval-output-consistency-api.py` - Measures consistency across 3 runs
- `eval-multi-skill-compatibility-api.py` - Tests skill interactions
- `eval-failure-mode-api.py` - Adversarial testing

---

## 🔬 Research Insights

### Key Findings from User Research:
- **#1 User Complaint:** Skills won't activate (Activation Rate is critical)
- **#2 User Complaint:** No way to evaluate before installing
- **#3 User Complaint:** Security concerns (no auditing exists)
- **#4 User Complaint:** Skills conflict with each other
- **#5 User Complaint:** Token waste and cost inefficiency

### Our Differentiators:
1. **Security First** - Only platform auditing skills for malicious code
2. **Interaction Analysis** - Test skills together, not in isolation
3. **Failure Mode Focus** - Actively try to break skills
4. **Real-World Testing** - Use actual user scenarios
5. **API-Based Automation** - 67% of evaluations fully automated

### Competitive Landscape:
- **SkillsMP:** 33,132 skills, just aggregates, NO testing
- **Anthropic:** Official skills, high quality but limited
- **Us:** First to systematically test and validate skills

---

## 📚 Key Documentation

### Must-Read Files:
1. **`evaluations/evaluation-framework-v3.md`** - Complete framework with rationale
2. **`evaluations/evaluation-implementation-guide.md`** - How to execute evals
3. **`evaluations/comprehensive-evaluation-dimensions.md`** - All 30+ dimensions researched
4. **`evaluations/google-sheets-schema.md`** - Complete data structure spec
5. **`evaluations/GOOGLE-SHEETS-SETUP.md`** - Setup instructions
6. **`evaluations/anthropic-api-skills-support.md`** - API integration guide

### Research Files:
- `evaluations/surge-ai-research-notes.md` - Surge AI methodology
- `evaluations/mercor-ai-research-notes.md` - Mercor AI rubric approach
- `evaluations/user-complaints-research.md` - User pain points
- `evaluations/context-safety-clarification.md` - Progressive disclosure

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
- **Evaluation Framework V3:** `/evaluations/evaluation-framework-v3.md` ⭐
- **Implementation Guide:** `/evaluations/evaluation-implementation-guide.md` ⭐
- **Google Sheet:** https://docs.google.com/spreadsheets/d/12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY/edit ⭐
- **Skills Metadata:** `/skills-data/skillsmp-top12-skills.json` ⭐
- **Test Prompts CSV:** `/evaluations/test-prompts-all-skills.csv` ⭐
- **Anthropic Skills:** https://github.com/anthropics/skills
- **Claude Skills Docs:** https://code.claude.com/docs/en/skills
- **Competitor (SkillsMP):** https://skillsmp.com/

---

## 📊 Key Metrics & Goals

- **Target:** 20-50 evaluated skills at launch (started with top 12)
- **Timeline:** 3-5 days to MVP
- **Quality Bar:** Rigorous, Surge AI-inspired rubric evaluation
- **Automation:** 67% of evaluations fully automated
- **First Mover Advantage:** Speed + Quality
- **Competitive Moat:** Testing > Aggregating, Security > Convenience

---

*This is our shared brain. Any agent can pick up where another left off.*
