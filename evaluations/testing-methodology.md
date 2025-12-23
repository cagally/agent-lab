# Testing Methodology - Practical Implementation Guide

**Date:** Dec 23, 2025  
**Purpose:** Define how to measure each metric quickly and accurately for MVP

---

## Design Principles

1. **Speed First** - We need to evaluate 20-50 skills in 2 days
2. **Automated Where Possible** - Use GPT + scripts for bulk analysis
3. **Manual Where Critical** - Real testing for activation and consistency
4. **Actionable Output** - Every metric produces user-facing recommendations

---

## Metric 1: Activation Rate

### What We're Measuring
Percentage of relevant prompts that successfully trigger the skill

### How to Test

**Automated Analysis (GPT-based):**
- Analyze skill description and activation triggers
- Identify potential activation keywords
- Flag vague or overly broad descriptions
- Predict activation method (keyword vs organic)

**Manual Testing (10 test prompts per skill):**
1. Create 10 prompts that SHOULD trigger the skill based on its description
2. Run each prompt in Claude Code with skill installed
3. Check if skill actually activates (visible in Claude's response)
4. Count successes: Activation Rate = (Successes / 10) × 100%

**Scoring:**
- 90-100% = 10/10 (Excellent)
- 70-89% = 7-9/10 (Good)
- 50-69% = 5-6/10 (Fair)
- 30-49% = 3-4/10 (Poor)
- 0-29% = 0-2/10 (Broken)

**Output for Users:**
- Activation Rate: 80%
- Method: Keyword-based
- Recommended triggers: "analyze data", "create chart"
- Tips: "Use explicit keywords for reliable activation"

---

## Metric 2: Task Completion Rate

### What We're Measuring
Does the skill successfully complete its stated task?

### How to Test

**Automated Analysis (GPT-based):**
- Review skill code/scripts for error handling
- Check for edge case coverage
- Identify potential failure modes
- Assess scope appropriateness

**Manual Testing (5-10 real tasks):**
1. Define 5-10 tasks the skill claims to handle
2. Execute each task using the skill
3. Evaluate if output meets expectations
4. Count full successes (partial = failure)
5. Task Completion Rate = (Successes / Total) × 100%

**Scoring:**
- 90-100% = 10/10 (Highly Reliable)
- 70-89% = 7-9/10 (Reliable)
- 50-69% = 5-6/10 (Inconsistent)
- 30-49% = 3-4/10 (Unreliable)
- 0-29% = 0-2/10 (Broken)

**Output for Users:**
- Completion Rate: 85%
- Tested on: 10 tasks
- Best for: "Simple data analysis tasks"
- Avoid: "Complex multi-step workflows"

---

## Metric 3: Output Consistency

### What We're Measuring
Does the skill produce similar outputs for the same input?

### How to Test

**Automated Analysis (GPT-based):**
- Identify if skill is deterministic or generative
- Check for randomness/variability in code
- Flag LLM-based generation without constraints

**Manual Testing (3 runs per test case):**
1. Select 3-5 representative test cases
2. Run each test case 3 times
3. Compare outputs for similarity
4. Calculate consistency score:
   - Identical outputs = 100%
   - Functionally equivalent = 80%
   - Similar but different = 60%
   - Completely different = 0%
5. Average across all test cases

**Scoring:**
- 95-100% = 10/10 (Deterministic)
- 80-94% = 7-9/10 (Highly Consistent)
- 60-79% = 5-6/10 (Moderately Consistent)
- 40-59% = 3-4/10 (Inconsistent)
- 0-39% = 0-2/10 (Unpredictable)

**Output for Users:**
- Consistency: 92% (Highly Consistent)
- Variability: Low
- Type: Deterministic
- Note: "Produces reliable, repeatable results"

---

## Metric 4: Token Efficiency

### What We're Measuring
How many tokens does the skill consume relative to value delivered?

### How to Test

**Automated Analysis:**
1. **Description Length**
   - Count characters in skill description
   - Estimate tokens (chars ÷ 4)
   - Flag if >2000 tokens (approaching 15k char limit)

2. **Execution Cost** (Manual Testing)
   - Run 5 typical tasks with the skill
   - Track tokens used (input + output)
   - Calculate average tokens per task
   - Compare to baseline (same task without skill)

**Scoring:**
- Description Efficiency:
  - <500 tokens = Excellent
  - 500-1000 tokens = Good
  - 1000-2000 tokens = Acceptable
  - 2000-3000 tokens = High
  - >3000 tokens = Excessive (WARNING)

- Execution Efficiency:
  - <20% overhead vs baseline = Excellent
  - 20-50% overhead = Good
  - 50-100% overhead = Acceptable
  - 100-200% overhead = High
  - >200% overhead = Excessive

**Output for Users:**
- Description: 450 tokens (Excellent)
- Avg Execution: 1,200 tokens/task
- Overhead: +30% vs baseline (Good)
- Cost Impact: Low
- Warning: None

---

## Metric 5: Description Efficiency (Context Limit Safety)

### What We're Measuring
Will this skill fit within Claude's system prompt budget?

### How to Test

**Automated Analysis (100% automated):**
1. Count total characters in skill description
2. Calculate token estimate (chars ÷ 4)
3. Check against Claude Code limits:
   - Default budget: 15,000 chars (≈3,750 tokens)
   - Extended budget: 30,000 chars (≈7,500 tokens)
4. Calculate "budget consumption" percentage

**Scoring:**
- <10% of budget = 10/10 (Minimal)
- 10-25% = 7-9/10 (Low)
- 25-50% = 5-6/10 (Moderate)
- 50-75% = 3-4/10 (High)
- >75% = 0-2/10 (CRITICAL WARNING)

**Output for Users:**
- Characters: 1,200 (8% of budget)
- Status: ✅ Safe
- Impact: Minimal
- OR
- Characters: 12,000 (80% of budget)
- Status: ⚠️ WARNING
- Impact: May prevent other skills from loading
- Recommendation: "Consider using extended budget or removing other skills"

---

## Metric 6: Maintenance Status

### What We're Measuring
Is this skill actively maintained or abandoned?

### How to Test

**Automated Analysis (GitHub API):**
1. Last commit date
2. Last release date (if applicable)
3. Open issues count
4. Recent activity (commits in last 90 days)
5. Repository status (archived, active)

**Scoring:**
- Updated <30 days ago = 10/10 (Active)
- 30-90 days = 7-9/10 (Recent)
- 90-180 days = 5-6/10 (Stale)
- 180-365 days = 3-4/10 (Outdated)
- >365 days or archived = 0-2/10 (Abandoned)

**Output for Users:**
- Last Updated: 15 days ago
- Status: ✅ Active
- Recent Activity: 8 commits in last 90 days
- Confidence: High
- OR
- Last Updated: 8 months ago
- Status: ⚠️ Outdated
- Recent Activity: None
- Confidence: Low - may not work with latest Claude

---

## Implementation Priority for MVP

### Phase 1: Automated Only (Day 1)
- Description Efficiency ✅ (100% automated)
- Maintenance Status ✅ (100% automated via GitHub API)
- Token Efficiency - Description part ✅ (automated)

**Output:** 20-50 skills with basic metrics in <4 hours

### Phase 2: Selective Manual Testing (Day 2)
- Activation Rate (top 10-15 skills)
- Task Completion Rate (top 10-15 skills)
- Output Consistency (top 10-15 skills)
- Token Efficiency - Execution part (top 10-15 skills)

**Output:** Deep evaluation of priority skills

### Phase 3: Refinement (Day 3)
- Validate automated predictions against manual results
- Adjust scoring thresholds
- Generate final scorecards

---

## Scorecard Output Format

```json
{
  "skill_name": "data-analyzer",
  "overall_score": 8.2,
  "scores": {
    "activation_rate": 8,
    "task_completion": 9,
    "output_consistency": 9,
    "token_efficiency": 7,
    "description_efficiency": 10,
    "maintenance_status": 8
  },
  "details": {
    "activation": {
      "rate": "80%",
      "method": "keyword",
      "triggers": ["analyze data", "create chart"],
      "tips": "Use explicit keywords for best results"
    },
    "completion": {
      "rate": "90%",
      "tested_tasks": 10,
      "best_for": "Simple data analysis",
      "avoid_if": "Complex multi-step workflows"
    },
    "consistency": {
      "score": "92%",
      "type": "deterministic",
      "note": "Produces reliable, repeatable results"
    },
    "tokens": {
      "description": 450,
      "avg_execution": 1200,
      "overhead": "+30%",
      "impact": "Low"
    },
    "context_safety": {
      "characters": 1200,
      "budget_pct": "8%",
      "status": "safe",
      "warning": null
    },
    "maintenance": {
      "last_update": "15 days ago",
      "status": "active",
      "activity": "8 commits in 90 days",
      "confidence": "high"
    }
  },
  "recommendation": "Highly recommended for data analysis tasks. Reliable activation and consistent output. Low token overhead.",
  "warnings": []
}
```

---

## Success Criteria

✅ **Speed:** Evaluate 20-50 skills in 2 days  
✅ **Accuracy:** Manual validation confirms automated scores ±1 point  
✅ **Utility:** Users can make informed decisions from scorecards  
✅ **Actionability:** Every metric includes specific recommendations  
✅ **Differentiation:** No competitor offers this level of testing  

---

## Next Steps

1. Build automation scripts for Phase 1 metrics
2. Create manual testing templates for Phase 2
3. Set up data collection and scorecard generation
4. Test methodology on 3-5 skills to validate approach
5. Refine and scale to full 20-50 skill set
