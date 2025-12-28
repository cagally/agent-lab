# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 4 - API Evaluation Automation (Running)

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
│   ├── skillsmp-top12-skills.json     # Master list of top 12 skills
│   ├── skill-ids-map.json             # ⭐ Anthropic API skill ID mapping
│   ├── skill-ids.json                 # ⭐ Full skill ID registry
│   └── raw-skills/                    # ⭐ Downloaded SKILL.md files (12 skills, reorganized)
├── evaluations/          # ⭐ Evaluation framework, implementation guides, templates
│   ├── evaluation-framework-v3.md               # FINAL 11-dimension framework
│   ├── evaluation-implementation-guide.md       # Step-by-step execution playbook
│   ├── test-prompts-final.csv                   # ⭐ 180 cleaned test prompts (READY)
│   └── [other evaluation docs...]
├── scripts/              # ⭐ Automation scripts for evaluation
│   ├── run-api-tests-v2-fixed.py               # ⭐ Main evaluation script (RUNNING)
│   ├── check-eval-progress.py                  # ⭐ Progress monitoring
│   ├── estimate-completion.py                  # ⭐ ETA calculator
│   ├── monitor-eval-loop.sh                    # ⭐ Background monitor
│   ├── upload-skills-to-anthropic.py           # ⭐ Skill uploader
│   └── [other scripts...]
├── research/             # ⭐ Research documentation
│   └── real-world-skill-usage.md               # ⭐ Progressive disclosure findings
└── README.md            # This file - project status and navigation
```

---

## 🎯 Current Status

**Last Updated:** Dec 28, 2025 - Session 6 (API Evaluation Running)

### ✅ Completed

**Previous Sessions:**
- Repository structure established
- Evaluation framework v3.0 finalized
- Top 12 skills downloaded and installed
- Google Sheets structure designed and created
- Automation scripts built and tested

**Session 5 (Dec 27 - Prompt Generation):**
- ✅ Generated 180 high-quality test prompts using Claude Sonnet 4.5
- ✅ 5 prompt types: activation-explicit, activation-implicit, edge-case, adversarial-confusion, adversarial-impossible
- ✅ Cleaned and formatted for Google Sheets import
- ✅ Cost: $2.70 in API credits

**Session 6 (Dec 28 - API Evaluation):**
- ✅ **Skills uploaded to Anthropic API** - All 12 skills deployed with custom IDs
- ✅ **Progressive disclosure research** - Confirmed metadata-only loading (~850 tokens/skill)
- ✅ **Cost optimization** - Determined 2-3 skills per test is optimal
- ✅ **Selective 3x testing** - Activation prompts 3x, edge/adversarial 1x
- ✅ **Evaluation script optimized** - Implements selective testing with resume mode
- 🔄 **Running 372 API tests** - Started at 19:23 GMT (30/372 completed)

### 🚧 In Progress

**API Evaluation (RUNNING NOW)**
- **Script:** `scripts/run-api-tests-v2-fixed.py`
- **Progress:** 30/372 tests (8.1%)
- **Rate:** ~99 seconds per test (~1.7 minutes)
- **ETA:** 5:00 AM GMT (Dec 28) - **9.5 hours remaining**
- **Cost so far:** $0.14
- **Estimated total cost:** $1.71 (output tokens only, ~306 avg tokens/test)
- **Process:** Running in background with monitoring
- **Output:** Google Sheets "API Responses" tab

**Test Configuration:**
- Activation prompts (96): 3 runs each = 288 tests
- Edge case + Adversarial (84): 1 run each = 84 tests
- Total: 372 tests (optimized from 540)
- Skills per test: 2-3 (expected + 1-2 random competitors)
- Delay: 4 seconds between API calls

### 📋 Next Steps

1. **Wait for evaluation completion** (~9.5 hours)
   - Monitor via `scripts/check-eval-progress.py`
   - Logs in `evaluations/eval-run.log`

2. **Build 5 automated scoring scripts:**
   - Token efficiency analyzer (already built ✅)
   - Security audit scanner (already built ✅)
   - Description efficiency analyzer (GPT-5 judge)
   - Activation rate calculator (from API results)
   - Output consistency analyzer (from 3x runs)

3. **Populate Google Sheets with automated scores**

4. **Create manual testing guide** for user:
   - Task completion testing
   - Grounding & faithfulness evaluation

5. **Generate final scorecards** and comparative analysis

---

## 🔬 Evaluation Framework V3 (Final)

### Hurdle Criteria (Pass/Fail)
1. **Activation Rate** - Does it activate reliably? (≥80% = Pass)
2. **Task Completion** - Can it complete its stated purpose?

### Quality Criteria (0-10 Scale)
3. **Token Efficiency** - Description and body size optimization (automated ✅)
4. **Security Audit** - Malicious code detection, safety rating (automated ✅)
5. **Description Efficiency** - Clarity, specificity, information density (GPT-5 judge)
6. **Output Consistency** - Same prompt, consistent results (API-based 🔄)
7. **Multi-Skill Compatibility** - Works alongside other skills (API-based 🔄)
8. **Failure Mode Resistance** - Graceful failure, edge case handling (API-based 🔄)
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
2. **Test Prompts** - 180 prompts (15 per skill) ✅ Imported
3. **API Responses** - Raw outputs from testing 🔄 Populating (30/372)
4. **Automated Scores** - Results from automation scripts ⏳ Next
5. **Manual Evaluations** - Human scoring workspace ⏳ Next
6. **Final Scorecards** - Aggregated results with ratings ⏳ Next
7. **Dashboard** - Executive summary with charts ⏳ Next

---

## 📊 Skills Inventory (Top 12)

All skills uploaded to Anthropic API with custom IDs. Reorganized folder structure for clarity.

| Skill Short ID | Full Name | API Skill ID | Eval Status |
|----------------|-----------|--------------|-------------|
| at-dispatch-v2 | pytorch-at-dispatch-v2 | skill_0182PDm4DHCe1ommUh41DSrC | 🔄 Testing |
| docstring | pytorch-docstring | skill_0182PDm4DHCe1ommUh41DSrD | 🔄 Testing |
| skill-writer | pytorch-skill-writer | skill_0182PDm4DHCe1ommUh41DSrE | 🔄 Testing |
| add-uint-support | pytorch-add-uint-support | skill_0182PDm4DHCe1ommUh41DSrF | 🔄 Testing |
| skill-creator | openai-skill-creator | skill_0182PDm4DHCe1ommUh41DSrG | 🔄 Testing |
| skill-installer | openai-skill-installer | skill_0182PDm4DHCe1ommUh41DSrH | 🔄 Testing |
| frontend-design | anthropic-frontend-design | skill_0182PDm4DHCe1ommUh41DSrI | 🔄 Testing |
| hook-development | anthropic-hook-development | skill_0182PDm4DHCe1ommUh41DSrJ | 🔄 Testing |
| command-development | anthropic-command-development | skill_0182PDm4DHCe1ommUh41DSrK | 🔄 Testing |
| agent-development | anthropic-agent-development | skill_0182PDm4DHCe1ommUh41DSrL | 🔄 Testing |
| writing-hookify-rules | anthropic-writing-rules | skill_0182PDm4DHCe1ommUh41DSrM | 🔄 Testing |
| mcp-integration | anthropic-mcp-integration | skill_0182PDm4DHCe1ommUh41DSrN | 🔄 Testing |

**Skill files:** `skills-data/raw-skills/[short-id]/SKILL.md`

**Skill ID mapping:** `skills-data/skill-ids-map.json`

---

## 🛠️ Automation Scripts

### 1. API Evaluation Runner 🔄
**Purpose:** Run 372 API tests with skills to measure activation, consistency, and compatibility

**Usage:**
```bash
python3.11 scripts/run-api-tests-v2-fixed.py
```

**Features:**
- Selective 3x testing (activation prompts 3x, others 1x)
- Resume mode (skips completed tests)
- Retry logic with exponential backoff
- 2-3 skills per test (cost-optimized)
- 4-second delay between calls
- Writes to Google Sheets in real-time

**Status:** Running in background (PID: 42094)

**Output:** Google Sheets "API Responses" tab

**Cost:** $1.71 estimated (306 avg output tokens/test)

### 2. Progress Monitor 🔄
**Purpose:** Check evaluation progress without interrupting

**Usage:**
```bash
python3.11 scripts/check-eval-progress.py
```

**Status:** Available

### 3. ETA Calculator 🔄
**Purpose:** Estimate completion time based on actual performance

**Usage:**
```bash
python3.11 scripts/estimate-completion.py
```

**Status:** Available

### 4. Token Efficiency Analyzer ✅
**Purpose:** Measure SKILL.md size and efficiency

**Usage:**
```bash
python3 scripts/eval-token-efficiency.py skills-data/raw-skills/[skill-name]
```

**Status:** Tested and working

### 5. Security Audit Scanner ✅
**Purpose:** Detect dangerous patterns and security risks

**Usage:**
```bash
python3 scripts/eval-security-audit.py skills-data/raw-skills/[skill-name]
```

**Status:** Tested and working

### 6-9. Coming Soon (After API Tests Complete)
- `eval-description-efficiency.py` - GPT-5 judges description quality
- `eval-activation-rate.py` - Calculate from API results
- `eval-output-consistency.py` - Analyze 3x runs
- `eval-multi-skill-compatibility.py` - Analyze skill interactions

---

## 💰 Cost Analysis

### Actual Performance (30 tests completed):
- **Output tokens:** 9,180 total (306 avg per test)
- **Cost per test:** $0.0046
- **Cost so far:** $0.14
- **Estimated remaining:** $1.57
- **Total estimated:** $1.71

### Original Estimates:
- **Initial estimate (540 tests):** $23
- **Optimized estimate (372 tests):** $17
- **Actual (based on real data):** $1.71

**Savings:** $21.29 (93% reduction) due to:
1. Selective 3x testing (saved $6)
2. Lower than expected token usage (saved ~$15)
3. Progressive disclosure working as expected

---

## 🔬 Research Insights

### Progressive Disclosure Confirmed:
- Skills load **metadata only** until activated (~850 tokens/skill)
- Full SKILL.md loads only when skill is used (~5,000 additional tokens)
- 2-3 skills per test is optimal (matches real-world usage)
- Massive cost savings vs. loading all skills upfront

### Key Findings from User Research:
- **#1 User Complaint:** Skills won't activate (Activation Rate is critical)
- **#2 User Complaint:** No way to evaluate before installing
- **#3 User Complaint:** Security concerns (no auditing exists)
- **#4 User Complaint:** Skills conflict with each other
- **#5 User Complaint:** Token waste and cost inefficiency

---

## 📚 Key Documentation

### Must-Read Files:
1. **`evaluations/evaluation-framework-v3.md`** - Complete framework with rationale
2. **`evaluations/evaluation-implementation-guide.md`** - How to execute evals
3. **`evaluations/test-prompts-final.csv`** - 180 ready-to-use test prompts
4. **`skills-data/skill-ids-map.json`** - Anthropic API skill ID mapping
5. **`research/real-world-skill-usage.md`** - Progressive disclosure research

---

## 🧠 Knowledge Base Protocol

### Session Start
1. Read this README for latest status
2. Check if evaluation is still running (`ps aux | grep run-api-tests`)
3. Review progress (`python3.11 scripts/check-eval-progress.py`)

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
- **Google Sheet:** https://docs.google.com/spreadsheets/d/12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY/edit ⭐
- **Test Prompts CSV:** `/evaluations/test-prompts-final.csv` ⭐
- **Skill ID Map:** `/skills-data/skill-ids-map.json` ⭐
- **Anthropic Skills:** https://github.com/anthropics/skills
- **Claude Skills Docs:** https://code.claude.com/docs/en/skills

---

## 📊 Key Metrics & Goals

- **Target:** 20-50 evaluated skills at launch (started with top 12)
- **Timeline:** 3-5 days to MVP
- **Quality Bar:** Rigorous, Surge AI-inspired rubric evaluation
- **Automation:** 67% of evaluations fully automated
- **First Mover Advantage:** Speed + Quality
- **Competitive Moat:** Testing > Aggregating, Security > Convenience

**Current Progress:** Day 4, API evaluation running, on track for MVP

---

*This is our shared brain. Any agent can pick up where another left off.*
