# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 4 - Activation Testing V2 (Redesign)

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
│   ├── skillsmp-top12-skills.json     # Master list of top 12 skills
│   ├── skill-ids-map.json             # Anthropic API skill ID mapping
│   ├── skill-ids.json                 # Full skill ID registry
│   └── raw-skills/                    # Downloaded SKILL.md files (12 skills)
├── evaluations/          # Evaluation framework, implementation guides, results
│   ├── evaluation-framework-v3.md                    # FINAL 11-dimension framework
│   ├── lessons-learned-activation-testing.md         # ⭐ V1 post-mortem + V2 plan
│   ├── brutal-analysis.md                            # ⭐ Honest analysis of failed approach
│   ├── test-prompts-final.csv                        # 180 V1 prompts (too explicit)
│   └── [other evaluation docs...]
├── scripts/              # Automation scripts for evaluation
│   ├── run-api-tests-v2-fixed.py                     # V1 script (flawed detection)
│   ├── check-eval-progress.py                        # Progress monitoring
│   ├── estimate-completion.py                        # ETA calculator
│   └── [other scripts...]
├── research/             # Research documentation
│   └── real-world-skill-usage.md                     # Progressive disclosure findings
└── README.md            # This file - project status and navigation
```

---

## 🎯 Current Status

**Last Updated:** Dec 28, 2025 - Session 6 (Activation Testing V1 Failed, V2 Planning)

### ✅ Completed

**Previous Sessions:**
- Repository structure established
- Evaluation framework v3.0 finalized
- Top 12 skills downloaded and installed
- Google Sheets structure designed and created
- Automation scripts built and tested

**Session 5 (Dec 27 - Prompt Generation):**
- ✅ Generated 180 test prompts using Claude Sonnet 4.5
- ✅ 5 prompt types created
- ✅ Cleaned and formatted for Google Sheets
- ❌ **FLAW DISCOVERED:** Prompts too explicit, activation-guaranteed

**Session 6 (Dec 28 - Activation Testing V1):**
- ✅ Skills uploaded to Anthropic API
- ✅ Progressive disclosure research completed
- ✅ Ran 44 API tests across 2 skills
- ❌ **FAILED:** 96% activation rate, no differentiation, data unusable
- ✅ Identified 4 critical flaws in approach
- ✅ Designed V2 approach with fixes

### ❌ What Failed (Activation Testing V1)

**Script:** `scripts/run-api-tests-v2-fixed.py`  
**Tests:** 44 completed (stopped early)  
**Cost:** $0.33  
**Result:** Data is not useful for evaluation

**Critical Flaws Identified:**

1. **Prompts Too Explicit**
   - Generated prompts mentioned exact skill names and use cases
   - Result: 96.3% activation rate (no differentiation)
   - Example bad prompt: "I need to add uint16 support to a PyTorch operator"

2. **Detection Logic Too Naive**
   - Marked ANY skill interaction as "activated"
   - Couldn't distinguish "reading skill file" from "using skill"
   - Result: 0 wrong activations, 100% consistency (suspicious)

3. **No Real Multi-Skill Testing**
   - Never saw skill conflicts or wrong activations
   - Loaded 2-3 skills but no interference detected
   - Can't tell if skills play nicely or detection is broken

4. **No Baseline or Negative Tests**
   - Only tested prompts designed to activate
   - No tests for "should NOT activate"
   - Can't measure false positive rate or selectivity

**See:** `evaluations/lessons-learned-activation-testing.md` for full post-mortem

---

## 🚧 Current Focus: Activation Testing V2

### The Problem We're Solving

**V1 gave us:** "These 2 skills activate when you explicitly ask for them"  
**We need:** "Skill X activates 85% on relevant tasks, 5% false positives, handles conflicts well"

### The V2 Approach

**Goal:** Create activation testing that actually differentiates good skills from bad skills

**Key Changes:**

1. **Better Prompts (Manual, Human-Crafted)**
   - Describe PROBLEMS, not solutions
   - Natural language, not technical jargon
   - Mix of positive, negative, conflict, and adversarial tests
   - 60 prompts total (5 per skill)

2. **Smarter Detection (5-Level Classification)**
   - Level 0: No interaction
   - Level 1: Skill consulted (read metadata)
   - Level 2: Skill referenced (mentioned in response)
   - Level 3: Skill activated (instructions followed)
   - Level 4: Skill executed (code from skill ran)

3. **Realistic Multi-Skill Scenarios**
   - Single skill baseline
   - Competitive skills (same domain)
   - Full environment (8-10 skills)
   - Wrong skill tests (different domains)

4. **Clear Baselines and Thresholds**
   - Positive tests: 80-95% activation (not 100%)
   - Negative tests: 0-10% activation
   - Consistency: Varies by difficulty
   - False positive rate: <5% on unrelated prompts

---

## 📋 Next Steps: Activation Testing V2

### Phase 1: Prompt Redesign (NEXT)
**Objective:** Create 60 high-quality test prompts manually

**Prompt types per skill (5 total):**
- 2 Positive tests (should activate, varying difficulty)
- 1 Negative test (should NOT activate, similar domain)
- 1 Conflict test (ambiguous, multiple skills could apply)
- 1 Adversarial test (should resist activation)

**Example transformation:**

| Old (V1 - Bad) | New (V2 - Good) |
|----------------|-----------------|
| "I need to add uint16 support to a PyTorch operator" | "My PyTorch model throws errors with 16-bit unsigned integer tensors. How do I fix this?" |
| "Update my code to use AT_DISPATCH_V2 macros" | "I'm getting deprecation warnings about AT_DISPATCH in my C++ extension. What should I do?" |

**Output:** `evaluations/test-prompts-v2.csv`  
**Time:** 2-3 hours  
**Cost:** $0 (manual work)

---

### Phase 2: Detection Logic Upgrade
**Objective:** Implement 5-level activation detection

**New script:** `scripts/run-api-tests-v3.py`

**Key improvements:**
- Parse tool calls more carefully (read vs. execute)
- Analyze response content for skill patterns
- Compare with baseline (run without skill)
- Classify activation level (0-4)

**Time:** 3-4 hours  
**Cost:** $0 (coding work)

---

### Phase 3: Baseline Testing
**Objective:** Establish baselines for each skill

**Test matrix:** 6 tests × 12 skills = 72 tests
- Positive (solo): Should activate
- Positive (competitive): Should activate target
- Negative (solo): Should NOT activate
- Negative (competitive): Should NOT activate

**Output:** `evaluations/baseline-results.csv`  
**Time:** ~2 hours  
**Cost:** ~$1-2

---

### Phase 4: Full Evaluation V2
**Objective:** Run comprehensive testing with V2 improvements

**Configuration:**
- 60 prompts (5 per skill)
- 3 runs for positive tests (consistency)
- 1 run for negative/conflict/adversarial
- Realistic multi-skill loading

**Total:** ~120 tests  
**Time:** ~3 hours  
**Cost:** ~$3-5

---

### Phase 5: Analysis and Scoring
**Objective:** Generate actionable insights

**Metrics:**
- Activation Reliability (0-10)
- Selectivity (0-10)
- Multi-Skill Behavior (0-10)
- Overall Activation Score (0-10)

**Output:** 
- Per-skill scorecards
- Comparative analysis
- Actionable recommendations

**Time:** 1 hour  
**Cost:** $0

---

## 🔬 Evaluation Framework V3 (Updated)

### Hurdle Criteria (Pass/Fail)
1. **Activation Rate** - Activates on relevant tasks (≥80% on positive tests)
2. **Selectivity** - Resists false activation (≤10% on negative tests)
3. **Task Completion** - Completes stated purpose when activated

### Quality Criteria (0-10 Scale)
4. **Token Efficiency** - Description and body size optimization (automated ✅)
5. **Security Audit** - Malicious code detection, safety rating (automated ✅)
6. **Description Efficiency** - Clarity, specificity, information density (GPT-5 judge)
7. **Output Consistency** - Same prompt, consistent results (API-based 🔄 V2)
8. **Multi-Skill Compatibility** - Works alongside other skills (API-based 🔄 V2)
9. **Failure Mode Resistance** - Graceful failure, edge case handling (API-based 🔄 V2)
10. **Grounding & Faithfulness** - Hallucination rate, factual accuracy (manual)

### Metadata
11. **Maintenance Status** - Active, stale, or archived

**Total Score:** 100 points (10 dimensions × 10)

**Automation Level:** 6/10 dimensions automated (60%)

---

## 📊 Google Sheets Structure

**Sheet URL:** https://docs.google.com/spreadsheets/d/12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY/edit

### 7 Tabs:
1. **Skills Master List** - Registry of all 12 skills
2. **Test Prompts** - V1: 180 prompts (flawed), V2: 60 prompts (pending)
3. **API Responses** - V1: 44 tests (unusable), V2: pending
4. **Automated Scores** - Pending V2 results
5. **Manual Evaluations** - Pending
6. **Final Scorecards** - Pending
7. **Dashboard** - Pending

---

## 📊 Skills Inventory (Top 12)

All skills uploaded to Anthropic API with custom IDs.

| Skill Short ID | Full Name | API Skill ID | Eval Status |
|----------------|-----------|--------------|-------------|
| at-dispatch-v2 | pytorch-at-dispatch-v2 | skill_0182PDm4DHCe1ommUh41DSrC | ⏳ V2 Pending |
| docstring | pytorch-docstring | skill_0182PDm4DHCe1ommUh41DSrD | ⏳ V2 Pending |
| skill-writer | pytorch-skill-writer | skill_0182PDm4DHCe1ommUh41DSrE | ⏳ V2 Pending |
| add-uint-support | pytorch-add-uint-support | skill_0182PDm4DHCe1ommUh41DSrF | ⏳ V2 Pending |
| skill-creator | openai-skill-creator | skill_0182PDm4DHCe1ommUh41DSrG | ⏳ V2 Pending |
| skill-installer | openai-skill-installer | skill_0182PDm4DHCe1ommUh41DSrH | ⏳ V2 Pending |
| frontend-design | anthropic-frontend-design | skill_0182PDm4DHCe1ommUh41DSrI | ⏳ V2 Pending |
| hook-development | anthropic-hook-development | skill_0182PDm4DHCe1ommUh41DSrJ | ⏳ V2 Pending |
| command-development | anthropic-command-development | skill_0182PDm4DHCe1ommUh41DSrK | ⏳ V2 Pending |
| agent-development | anthropic-agent-development | skill_0182PDm4DHCe1ommUh41DSrL | ⏳ V2 Pending |
| writing-hookify-rules | anthropic-writing-rules | skill_0182PDm4DHCe1ommUh41DSrM | ⏳ V2 Pending |
| mcp-integration | anthropic-mcp-integration | skill_0182PDm4DHCe1ommUh41DSrN | ⏳ V2 Pending |

---

## 🛠️ Automation Scripts

### Working Scripts ✅

1. **Token Efficiency Analyzer** - `scripts/eval-token-efficiency.py`
2. **Security Audit Scanner** - `scripts/eval-security-audit.py`

### Failed Scripts ❌

3. **API Evaluation V1** - `scripts/run-api-tests-v2-fixed.py`
   - Flawed detection logic
   - Too-explicit prompts
   - Data not useful
   - See lessons learned document

### Planned Scripts 🔄

4. **API Evaluation V2** - `scripts/run-api-tests-v3.py` (to be built)
   - 5-level activation detection
   - Baseline comparison
   - Multi-skill scenarios
   - Realistic testing

---

## 💰 Cost Analysis

### Session 6 Costs:
- Prompt generation (V1): $2.70
- API testing (V1, 44 tests): $0.33
- **Total V1:** $3.03

### V2 Estimated Costs:
- Phase 1 (Prompts): $0 (manual)
- Phase 2 (Detection): $0 (coding)
- Phase 3 (Baseline): $1-2 (72 tests)
- Phase 4 (Evaluation): $3-5 (120 tests)
- Phase 5 (Analysis): $0 (analysis)
- **Total V2:** $5-7

### Lessons Learned:
- Cheap tests with bad data = waste of money
- Better to spend more on quality prompts and detection
- Manual work upfront saves API costs later

---

## 📚 Key Documentation

### Must-Read Files:
1. **`evaluations/lessons-learned-activation-testing.md`** - ⭐ V1 post-mortem + V2 plan
2. **`evaluations/brutal-analysis.md`** - ⭐ Honest analysis of what went wrong
3. **`evaluations/evaluation-framework-v3.md`** - Complete framework
4. **`skills-data/skill-ids-map.json`** - Anthropic API skill ID mapping
5. **`research/real-world-skill-usage.md`** - Progressive disclosure research

---

## 🧠 Knowledge Base Protocol

### Session Start
1. Read this README for latest status
2. Check `evaluations/lessons-learned-activation-testing.md` for V2 plan
3. Understand what failed and why before starting new work

### During Session
- Don't repeat V1 mistakes (explicit prompts, naive detection)
- Focus on quality over quantity
- Test assumptions before running expensive operations

### Session End
1. Update this README with progress
2. Document lessons learned
3. Commit and push all changes

---

## 🚀 Quick Links

- **Vision Doc:** `/home/ubuntu/projects/agent-lab-2b9b282d/Agent Skills Platform V.0001.md`
- **V2 Plan:** `/evaluations/lessons-learned-activation-testing.md` ⭐
- **V1 Post-Mortem:** `/evaluations/brutal-analysis.md` ⭐
- **Google Sheet:** https://docs.google.com/spreadsheets/d/12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY/edit
- **Skill ID Map:** `/skills-data/skill-ids-map.json`
- **Anthropic Skills:** https://github.com/anthropics/skills

---

## 📊 Success Criteria for V2

We'll know V2 works if:

1. **Activation rates vary by prompt type**
   - NOT 96% across the board
   - Positive: 80-95%, Negative: 0-10%, Conflict: 30-70%

2. **We see skill differentiation**
   - Some skills score 8-10, some 4-7, some 0-3
   - NOT everyone at 9.5/10

3. **We detect real issues**
   - Wrong activations, false positives, inconsistencies
   - NOT perfect behavior everywhere

4. **Data is actionable**
   - Can recommend skills based on scores
   - Can explain WHY a skill scored low
   - NOT just "it works" or "it doesn't"

---

*Next: Phase 1 - Manual prompt redesign (2-3 hours)*
