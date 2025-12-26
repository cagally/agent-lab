# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 2 - Evaluation Framework Finalization & Automation

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
│   ├── skillsmp-top12-skills.json     # ⭐ Master list of top 12 skills
│   ├── skillsmp-reconnaissance.md     # SkillsMP analysis & strategy
│   └── raw-skills/                    # ⭐ Downloaded SKILL.md files (12 skills)
├── evaluations/          # ⭐ Evaluation framework, implementation guides, templates
│   ├── evaluation-framework-v3.md               # ⭐ FINAL 11-dimension framework
│   ├── evaluation-implementation-guide.md       # ⭐ Step-by-step execution playbook
│   ├── comprehensive-evaluation-dimensions.md   # ⭐ All 30+ dimensions researched
│   ├── test-prompt-suite-template.md           # ⭐ Activation testing templates
│   ├── evaluation-results-template.md          # ⭐ Results recording template
│   ├── framework-v2-final.md                   # Previous framework (reference)
│   ├── testing-methodology.md                  # Practical testing guide
│   ├── context-safety-clarification.md         # Progressive disclosure research
│   ├── surge-ai-research-notes.md              # Surge AI methodology research
│   ├── mercor-ai-research-notes.md             # Mercor AI evaluation research
│   └── user-complaints-research.md             # User pain points analysis
├── scripts/              # ⭐ Automation scripts for evaluation
│   ├── install-skills-to-claude.sh    # ⭐ Install skills to Claude Code
│   ├── eval-token-efficiency.py       # ⭐ Automated token analysis (TESTED)
│   ├── eval-security-audit.py         # ⭐ Automated security scanning (TESTED)
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

**Last Updated:** Dec 25, 2025 - Session 4

### ✅ Completed

**Previous Sessions:**
- Repository structure established
- Project vision documented
- Knowledge base protocol defined
- Evaluation framework v1.0 & v2.0 designed
- Deep user research conducted
- SkillsMP reconnaissance completed
- Top 12 skills downloaded from PyTorch, OpenAI, Anthropic
- Claude Code setup completed on user's macOS
- Installation script created and tested
- Skills metadata tracked in JSON

**This Session (Dec 25 - Continued):**
- ✅ **Evaluation Framework V3 Finalized** - 11 dimensions, research-backed
- ✅ **Comprehensive Research Completed** - 30+ evaluation dimensions identified
- ✅ **Implementation Guide Created** - Step-by-step execution playbook
- ✅ **Automation Scripts Built:**
  - Token Efficiency Analyzer (tested ✅)
  - Security Audit Scanner (tested ✅)
- ✅ **Test Templates Created:**
  - Activation test prompt suite template
  - Evaluation results template
- ✅ **Context Safety Issue Resolved** - Progressive disclosure clarified
- ✅ **Surge AI & Mercor AI Research** - Rubric-based evaluation methodologies studied
- ✅ **All documentation committed to GitHub**

### 🚧 In Progress

- **User Action Required:** Review implementation guide and begin manual evaluations
- **Next:** Execute evaluations on all 12 skills

### 📋 Next Steps

1. **User reviews implementation guide:**
   - Read `evaluations/evaluation-implementation-guide.md`
   - Understand the 11-dimension framework
   - Review time estimates (90-130 mins per skill)

2. **Run automated evaluations (easy wins):**
   ```bash
   cd ~/agent-lab
   # Token efficiency
   python3 scripts/eval-token-efficiency.py skills-data/raw-skills/[skill-name]
   # Security audit
   python3 scripts/eval-security-audit.py skills-data/raw-skills/[skill-name]
   ```

3. **Execute manual evaluations in Claude Code:**
   - Activation Rate (10 prompts)
   - Task Completion (verify core function)
   - Output Consistency (3 runs)
   - Grounding & Faithfulness (fact-check)
   - Failure Mode Resistance (5 adversarial prompts)
   - Multi-Skill Compatibility (test with other skills)
   - Tool Call Correctness (observe tool usage)

4. **Document results:**
   - Use `evaluations/evaluation-results-template.md`
   - Fill in scores for all 11 dimensions
   - Record detailed findings

5. **Create skill scorecards** for MVP launch

---

## 🔬 Evaluation Framework V3 (Final)

### Hurdle Criteria (Pass/Fail)
1. **Activation Rate** - Does it activate reliably? (≥80% = Pass)
2. **Task Completion** - Can it complete its stated purpose?

### Quality Criteria (0-10 Scale)
3. **Description Efficiency** - Clarity, specificity, information density (GPT-5 judge)
4. **Output Consistency** - Same prompt, consistent results (semantic similarity)
5. **Token Efficiency** - Description and body size optimization (automated ✅)
6. **Grounding & Faithfulness** - Hallucination rate, factual accuracy
7. **Failure Mode Resistance** - Graceful failure, edge case handling
8. **Security Audit** - Malicious code detection, safety rating (automated ✅)
9. **Multi-Skill Compatibility** - Works alongside other skills
10. **Tool Call Correctness** - Right tools, correct parameters

### Metadata
11. **Maintenance Status** - Active, stale, or archived

**Total Score:** 100 points (2 hurdles + 90 quality points)

**Time per Skill:** 90-130 minutes

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
**Purpose:** Measure static and dynamic token costs

**Usage:**
```bash
python3 scripts/eval-token-efficiency.py skills-data/raw-skills/[skill-name]
```

**Output:** JSON file with character counts, token estimates, efficiency score (0-10)

**Status:** Tested and working

### 2. Security Audit Scanner ✅
**Purpose:** Detect dangerous patterns and security risks

**Usage:**
```bash
python3 scripts/eval-security-audit.py skills-data/raw-skills/[skill-name]
```

**Output:** JSON file with findings, severity ratings, safety score (0-10)

**Detects:**
- Destructive file operations (rm -rf, dd)
- Code execution (eval, exec)
- Hardcoded credentials
- Unsafe network access
- Dangerous bash patterns

**Status:** Tested and working (pytorch-skill-writer: 10/10 Safe)

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
5. **Training Data Generation** - Document failures to improve skills

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
4. **`evaluations/test-prompt-suite-template.md`** - Activation testing guide
5. **`evaluations/evaluation-results-template.md`** - Results recording template

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
- **Skills Metadata:** `/skills-data/skillsmp-top12-skills.json` ⭐
- **Anthropic Skills:** https://github.com/anthropics/skills
- **Claude Skills Docs:** https://code.claude.com/docs/en/skills
- **Competitor (SkillsMP):** https://skillsmp.com/

---

## 📊 Key Metrics & Goals

- **Target:** 20-50 evaluated skills at launch (started with top 12)
- **Timeline:** 3-5 days to MVP
- **Quality Bar:** Rigorous, Surge AI-inspired rubric evaluation
- **First Mover Advantage:** Speed + Quality
- **Competitive Moat:** Testing > Aggregating, Security > Convenience

---

*This is our shared brain. Any agent can pick up where another left off.*
