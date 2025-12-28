# Lessons Learned: Activation Testing V1 (Failed)

**Date:** December 28, 2025  
**Status:** STOPPED - Approach fundamentally flawed  
**Tests Completed:** 44 tests across 2 skills  
**Cost:** $0.33 API costs  
**Result:** Data is not useful for evaluation

---

## What We Did

### Approach V1: Explicit Prompt Testing with Simple Detection

**Script:** `scripts/run-api-tests-v2-fixed.py`

**Method:**
1. Generated 180 test prompts using Claude Sonnet 4.5
2. 5 prompt types: activation-explicit, activation-implicit, edge-case, adversarial-confusion, adversarial-impossible
3. Ran prompts through Anthropic API with 2-3 skills loaded
4. Detected activation by checking for `text_editor_code_execution` tool use
5. Recorded results in Google Sheets

**Configuration:**
- Activation prompts: 3 runs each (consistency testing)
- Edge/Adversarial prompts: 1 run each
- Skills per test: Expected skill + 1-2 random competitors
- Total planned: 372 tests

---

## What Went Wrong

### Flaw #1: Prompts Were Too Explicit

**Problem:** Prompts directly mentioned the skill's exact use case and terminology.

**Examples of bad prompts:**
- "I need to add uint16 and uint32 support to a PyTorch operator"
- "I need to update my PyTorch C++ code to use the new AT_DISPATCH_V2 macros"

**Result:** 96.3% activation rate (26/27 tests) - no differentiation between skills

**Why it's bad:** Real users don't say "use the AT_DISPATCH_V2 skill". They describe problems. These prompts are activation-guaranteed, not realistic tests.

---

### Flaw #2: Detection Logic Was Too Naive

**Current detection code:**
```python
if tool_name == 'text_editor_code_execution' or '/skills/' in tool_input:
    skill_activated = True
```

**Problem:** This marks ANY interaction with skills as "activated", including:
- Model reading the skill file to learn about it
- Model browsing skill metadata
- Model saying "let me check the skill..."

**Result:** 
- 0 wrong skill activations detected
- 100% consistency across 3-run tests (suspicious)
- No way to distinguish "skill was consulted" from "skill was actually used"

**Why it's bad:** We're measuring curiosity, not activation. The model might just be reading documentation.

---

### Flaw #3: No Real Multi-Skill Testing

**Configuration:** Loaded 2-3 skills per test (expected + 1-2 random)

**Problem:** Never saw:
- Wrong skill activations (0 found)
- Skill conflicts
- Skills interfering with each other

**Result:** Can't tell if skills play nicely together or if detection is just broken.

**Why it's bad:** Real users have 5-10 skills installed. We need to test realistic multi-skill environments.

---

### Flaw #4: No Baseline or Negative Tests

**What we tested:** Prompts designed to activate skills

**What we didn't test:**
- Prompts that should NOT activate any skill
- Prompts that sound similar but are wrong domain
- Prompts that should activate a DIFFERENT skill

**Result:** No way to know if 96% activation is good or if the skills are just over-eager.

**Why it's bad:** Without negative tests, we can't measure false positive rate or skill selectivity.

---

## Key Insights (What We Actually Learned)

### 1. Activation Rate Alone Is Meaningless

**Finding:** 96.3% of tests activated the expected skill

**Problem:** We don't know if this is:
- ✅ Good (skills are reliable)
- ❌ Bad (skills are over-eager and activate on everything)

**Need:** Negative tests to establish false positive rate

---

### 2. Prompt Quality Matters More Than Quantity

**Finding:** 180 prompts generated, but all too explicit

**Problem:** 
- LLM-generated prompts mimic the skill's description language
- They're optimized to activate, not to challenge
- No diversity in difficulty or ambiguity

**Need:** Human-crafted prompts with varying difficulty levels

---

### 3. Detection Needs to Measure Impact, Not Intent

**Finding:** Model often says "let me read the skill" but detection marks this as activation

**Problem:** We're measuring whether the model LOOKED at the skill, not whether it USED it

**Need:** Check if skill's guidance was actually followed in the output

---

### 4. Consistency Testing Revealed Nothing

**Finding:** 100% consistency across all 3-run tests

**Problem:** This is suspicious - real systems have variance

**Possible causes:**
- Prompts are too easy (no edge cases)
- Detection is binary and crude
- Sample size too small

**Need:** More challenging prompts that might have inconsistent activation

---

## What We Need to Fix

### Fix #1: Better Prompt Generation

**Goal:** Create prompts that test skill selectivity, not just activation

**New prompt types needed:**

1. **Positive Tests (Should Activate)**
   - Describe the PROBLEM, not the solution
   - Use natural language, not technical jargon
   - Vary difficulty: obvious → subtle → ambiguous

2. **Negative Tests (Should NOT Activate)**
   - Similar domain but wrong use case
   - Right keywords but wrong context
   - Completely unrelated tasks

3. **Conflict Tests (Multiple Skills Could Apply)**
   - Ambiguous requests that 2+ skills could handle
   - Measure which skill wins and why
   - Test skill priority and selection logic

4. **Adversarial Tests (Should Resist Activation)**
   - Deliberately confusing prompts
   - Prompts with skill keywords but wrong intent
   - Edge cases that sound right but aren't

**Example transformation:**

| Old (Bad) | New (Good) |
|-----------|------------|
| "I need to add uint16 support to a PyTorch operator" | "My PyTorch model is throwing errors when I pass in 16-bit unsigned integer tensors. How do I fix this?" |
| "Update my code to use AT_DISPATCH_V2 macros" | "I'm getting deprecation warnings about AT_DISPATCH in my C++ extension. What should I do?" |

---

### Fix #2: Smarter Activation Detection

**Goal:** Detect whether the skill was USED, not just consulted

**New detection logic needed:**

1. **Check for Skill Execution**
   - Did the model execute code FROM the skill?
   - Did the model follow the skill's specific instructions?
   - Did the model reference skill-specific patterns?

2. **Verify Output Impact**
   - Compare output with and without the skill
   - Check if skill's guidance appears in the response
   - Measure if the skill changed the behavior

3. **Distinguish Consultation from Activation**
   - Reading skill file = consultation (not activation)
   - Following skill instructions = activation
   - Executing skill code = strong activation

**Proposed detection hierarchy:**
- **Level 0:** No skill interaction
- **Level 1:** Skill consulted (read metadata)
- **Level 2:** Skill referenced (mentioned in response)
- **Level 3:** Skill activated (instructions followed)
- **Level 4:** Skill executed (code from skill ran)

---

### Fix #3: Realistic Multi-Skill Scenarios

**Goal:** Test skills in realistic environments with 5-10 skills loaded

**New test configurations:**

1. **Single Skill Baseline**
   - Load only the expected skill
   - Measure activation rate
   - Establish baseline behavior

2. **Competitive Skills**
   - Load 2-3 skills from the same domain (e.g., all PyTorch skills)
   - Test which skill wins on ambiguous prompts
   - Measure conflict rate

3. **Full Environment**
   - Load 8-10 diverse skills (realistic user setup)
   - Test if expected skill still activates
   - Measure interference and false positives

4. **Wrong Skill Tests**
   - Load skills from different domains
   - Use prompts that should activate NONE of them
   - Measure false positive rate

---

### Fix #4: Establish Baselines and Thresholds

**Goal:** Define what "good" looks like for each metric

**Baselines needed:**

1. **Activation Rate**
   - Positive tests: Should be 80-95% (not 100%)
   - Negative tests: Should be 0-10%
   - Ambiguous tests: Should be 30-70%

2. **Consistency**
   - Easy prompts: 90-100% consistency
   - Medium prompts: 70-90% consistency
   - Hard prompts: 50-70% consistency

3. **False Positive Rate**
   - Unrelated prompts: <5% activation
   - Similar domain: <20% activation
   - Ambiguous prompts: <50% wrong skill

4. **Multi-Skill Behavior**
   - Expected skill wins: >70% of ambiguous cases
   - No conflicts: <10% of tests
   - Graceful degradation: >90% when skill missing

---

## Next Steps: Activation Testing V2

### Phase 1: Prompt Redesign (Manual)

**Objective:** Create 60 high-quality test prompts (5 per skill × 12 skills)

**Prompt distribution per skill:**
- 2 Positive tests (should activate, varying difficulty)
- 1 Negative test (should NOT activate, similar domain)
- 1 Conflict test (ambiguous, multiple skills could apply)
- 1 Adversarial test (should resist activation)

**Method:**
- Human-crafted prompts based on real user scenarios
- Review actual Claude Code usage patterns
- Test prompts manually first to verify behavior

**Output:** `evaluations/test-prompts-v2.csv`

**Time:** 2-3 hours  
**Cost:** $0 (manual work)

---

### Phase 2: Detection Logic Upgrade

**Objective:** Implement smarter activation detection with 5 levels

**Changes to `run-api-tests-v3.py`:**

1. **Parse tool calls more carefully**
   ```python
   # Check if skill file was READ (consultation)
   if 'read' in tool_input and '/skills/' in tool_input:
       consultation = True
   
   # Check if skill code was EXECUTED (activation)
   if 'execute' in tool_input or 'run' in tool_input:
       activation = True
   ```

2. **Analyze response content**
   ```python
   # Check if skill's specific patterns appear in output
   skill_patterns = load_skill_patterns(skill_id)
   if any(pattern in response_text for pattern in skill_patterns):
       skill_referenced = True
   ```

3. **Compare with baseline**
   ```python
   # Run same prompt WITHOUT the skill
   baseline_response = run_without_skill(prompt)
   
   # Measure difference
   impact_score = calculate_difference(response, baseline_response)
   ```

**Output:** Updated detection with 5-level classification

**Time:** 3-4 hours  
**Cost:** $0 (coding work)

---

### Phase 3: Baseline Testing

**Objective:** Establish baselines for each skill with controlled tests

**Test matrix per skill:**

| Test Type | Skills Loaded | Expected Result | Tests |
|-----------|---------------|-----------------|-------|
| Positive (solo) | 1 (target only) | Activate | 2 |
| Positive (competitive) | 3 (same domain) | Activate target | 2 |
| Negative (solo) | 1 (target only) | No activation | 1 |
| Negative (competitive) | 3 (different domains) | No activation | 1 |

**Total:** 6 tests × 12 skills = 72 baseline tests

**Method:**
- Run with new detection logic
- Record activation levels (0-4)
- Establish per-skill baselines

**Output:** `evaluations/baseline-results.csv`

**Time:** ~2 hours (automated)  
**Cost:** ~$1-2 (72 tests × $0.02 avg)

---

### Phase 4: Full Evaluation V2

**Objective:** Run comprehensive testing with improved prompts and detection

**Configuration:**
- 60 prompts (5 per skill)
- 3 runs for positive tests (consistency)
- 1 run for negative/conflict/adversarial tests
- Realistic multi-skill loading (5-10 skills)

**Total tests:** ~120 tests

**Method:**
- Use `run-api-tests-v3.py` with new detection
- Load skills based on test type (solo/competitive/full)
- Record 5-level activation classification
- Calculate metrics against baselines

**Output:** 
- `evaluations/activation-results-v2.csv`
- Per-skill activation scorecards
- Multi-skill conflict analysis

**Time:** ~3 hours (automated)  
**Cost:** ~$3-5 (120 tests × $0.03 avg)

---

### Phase 5: Analysis and Scoring

**Objective:** Generate actionable insights and skill ratings

**Metrics to calculate:**

1. **Activation Reliability**
   - Positive test success rate
   - Consistency score (3-run variance)
   - Rating: 0-10 based on baseline comparison

2. **Selectivity**
   - Negative test resistance rate
   - False positive rate
   - Rating: 0-10 (lower false positives = higher score)

3. **Multi-Skill Behavior**
   - Conflict resolution rate (wins ambiguous cases)
   - Interference rate (activates when shouldn't)
   - Rating: 0-10 (better behavior = higher score)

4. **Overall Activation Score**
   - Weighted average: Reliability (40%) + Selectivity (40%) + Multi-Skill (20%)
   - Final rating: 0-10

**Output:**
- `evaluations/activation-scores-v2.csv`
- Updated Google Sheets with real insights
- Comparative analysis across skills

**Time:** 1 hour  
**Cost:** $0 (analysis only)

---

## Success Criteria for V2

### We'll know V2 works if:

1. **Activation rates vary by prompt type**
   - Positive: 80-95%
   - Negative: 0-10%
   - Conflict: 30-70%
   - NOT 96% across the board

2. **We see skill differentiation**
   - Some skills score 8-10 (excellent)
   - Some skills score 4-7 (mediocre)
   - Some skills score 0-3 (poor)
   - NOT everyone at 9.5/10

3. **We detect real issues**
   - Wrong skill activations
   - False positives on negative tests
   - Inconsistency on hard prompts
   - NOT perfect behavior everywhere

4. **Data is actionable**
   - Can recommend skills based on scores
   - Can identify specific weaknesses
   - Can explain WHY a skill scored low
   - NOT just "it works" or "it doesn't"

---

## Timeline and Budget

### Total Effort: ~10 hours
- Phase 1 (Prompts): 2-3 hours
- Phase 2 (Detection): 3-4 hours
- Phase 3 (Baseline): 2 hours
- Phase 4 (Evaluation): 3 hours
- Phase 5 (Analysis): 1 hour

### Total Cost: ~$5-7
- Phase 3: $1-2
- Phase 4: $3-5
- Other phases: $0

### Expected Completion: 1-2 days

---

## Conclusion

**V1 Failed Because:**
- Prompts were too easy
- Detection was too naive
- Testing wasn't realistic
- No baselines to compare against

**V2 Will Succeed By:**
- Human-crafted challenging prompts
- Smart 5-level detection
- Realistic multi-skill scenarios
- Clear baselines and thresholds

**The goal:** Generate data that actually differentiates good skills from bad skills, with actionable insights for users.

---

*Next: Begin Phase 1 - Manual prompt redesign*
