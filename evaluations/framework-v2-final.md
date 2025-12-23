# Agent Skills Evaluation Framework v2.0 (FINAL)

**Date:** Dec 23, 2025  
**Status:** Research-Validated, Ready for Implementation  
**Purpose:** Fast, actionable skill evaluation that solves real user pain points

---

## Executive Summary

After researching user complaints across Reddit, GitHub, blogs, and analyzing the competitive landscape (SkillsMP), we've designed an evaluation framework that addresses the **actual problems users face** with agent skills.

**Key Insight:** No one is actually testing skills. Existing marketplaces just aggregate and display. We will be the first to provide real, tested quality metrics.

**Our Moat:** Testing > Aggregating

---

## The 6 Metrics (Research-Validated)

### 🔴 CRITICAL METRICS (5)

1. **Activation Rate** - #1 user complaint
2. **Task Completion Rate** - Core reliability concern
3. **Output Consistency** - "Same prompt, different results" frustration
4. **Token Efficiency** - Explicit cost complaints
5. **Description Efficiency** - Silent failures from context limits

### 🟡 IMPORTANT METRIC (1)

6. **Maintenance Status** - Abandonment concerns

---

## Metric Definitions

### 1. Activation Rate (0-10)

**What:** Percentage of relevant prompts that successfully trigger the skill

**Why It Matters:** Most common user complaint - "skills won't activate"

**How We Test:**
- Automated: GPT analyzes description for activation triggers
- Manual: Run 10 test prompts, count successful activations
- Score: (Successes / 10) × 100% → 0-10 scale

**User Output:**
- Rate: 80%
- Method: Keyword-based
- Triggers: ["analyze data", "create chart"]
- Tips: "Use explicit keywords for reliable activation"

---

### 2. Task Completion Rate (0-10)

**What:** Does the skill successfully complete its stated task?

**Why It Matters:** Users need reliability for production work

**How We Test:**
- Automated: GPT reviews code for error handling, edge cases
- Manual: Execute 5-10 real tasks, count full successes
- Score: (Successes / Total) × 100% → 0-10 scale

**User Output:**
- Rate: 85%
- Tested: 10 tasks
- Best for: "Simple data analysis tasks"
- Avoid: "Complex multi-step workflows"

---

### 3. Output Consistency (0-10)

**What:** Does the skill produce similar outputs for the same input?

**Why It Matters:** "Perfect output one minute, garbage the next" is a core frustration

**How We Test:**
- Automated: GPT identifies if deterministic or generative
- Manual: Run 3-5 test cases 3 times each, compare outputs
- Score: Average similarity % → 0-10 scale

**User Output:**
- Consistency: 92%
- Type: Deterministic
- Variability: Low
- Note: "Produces reliable, repeatable results"

---

### 4. Token Efficiency (0-10)

**What:** Token consumption (description + execution) relative to value

**Why It Matters:** Users explicitly complain about "burning through tokens"

**How We Test:**
- Automated: Count description tokens (chars ÷ 4)
- Manual: Track execution tokens across 5 tasks
- Score: Combined efficiency rating

**User Output:**
- Description: 450 tokens (Excellent)
- Avg Execution: 1,200 tokens/task
- Overhead: +30% vs baseline (Good)
- Cost Impact: Low

---

### 5. Description Efficiency (0-10)

**What:** Will this skill fit within Claude's system prompt budget?

**Why It Matters:** Skills >15k chars are silently excluded - users have NO idea why skills don't work

**How We Test:**
- 100% Automated: Count chars, calculate % of 15k budget
- Flag if >75% of budget (critical warning)

**User Output:**
- Characters: 1,200 (8% of budget)
- Status: ✅ Safe
- Impact: Minimal

OR

- Characters: 12,000 (80% of budget)
- Status: ⚠️ WARNING
- Impact: May prevent other skills from loading
- Fix: "Use extended budget or remove other skills"

---

### 6. Maintenance Status (0-10)

**What:** Is this skill actively maintained or abandoned?

**Why It Matters:** Users ask "how often are skills updated?" and worry about stale skills

**How We Test:**
- 100% Automated: GitHub API for last commit, releases, activity
- Score based on recency

**User Output:**
- Last Updated: 15 days ago
- Status: ✅ Active
- Activity: 8 commits in 90 days
- Confidence: High

---

## Implementation Plan

### Phase 1: Automated Metrics (Day 1) - 4 hours

**Metrics:**
- Description Efficiency ✅
- Maintenance Status ✅
- Token Efficiency (description part) ✅

**Output:** All 20-50 skills with basic automated metrics

**Tools:**
- Python scripts for GitHub API
- Character/token counting
- GPT-4 for description analysis

---

### Phase 2: Manual Testing (Day 2) - 8 hours

**Metrics:**
- Activation Rate (top 10-15 skills)
- Task Completion Rate (top 10-15 skills)
- Output Consistency (top 10-15 skills)
- Token Efficiency (execution part, top 10-15 skills)

**Output:** Deep evaluation of priority skills

**Tools:**
- Claude Code for real testing
- Test case templates
- Token tracking

---

### Phase 3: Scorecard Generation (Day 3) - 4 hours

**Activities:**
- Validate automated predictions vs manual results
- Adjust scoring thresholds
- Generate final JSON scorecards
- Create user-facing summaries

**Output:** Production-ready skill evaluations for website

---

## Scorecard Format

```json
{
  "skill_name": "data-analyzer",
  "skill_id": "anthropic/data-analyzer",
  "evaluation_date": "2025-12-23",
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
      "recommended_triggers": ["analyze data", "create chart"],
      "tips": "Use explicit keywords for best results"
    },
    "completion": {
      "rate": "90%",
      "tested_tasks": 10,
      "best_for": "Simple data analysis tasks",
      "avoid_if": "Complex multi-step workflows"
    },
    "consistency": {
      "score": "92%",
      "type": "deterministic",
      "variability": "low",
      "note": "Produces reliable, repeatable results"
    },
    "tokens": {
      "description_tokens": 450,
      "avg_execution_tokens": 1200,
      "overhead_vs_baseline": "+30%",
      "cost_impact": "low"
    },
    "context_safety": {
      "characters": 1200,
      "budget_percentage": "8%",
      "status": "safe",
      "warning": null
    },
    "maintenance": {
      "last_update": "15 days ago",
      "status": "active",
      "recent_activity": "8 commits in 90 days",
      "confidence": "high"
    }
  },
  
  "summary": {
    "recommendation": "Highly recommended for data analysis tasks. Reliable activation and consistent output. Low token overhead.",
    "strengths": [
      "High task completion rate (90%)",
      "Deterministic and consistent",
      "Actively maintained"
    ],
    "limitations": [
      "Keyword-based activation requires explicit triggers",
      "Best for simple tasks, not complex workflows"
    ],
    "warnings": []
  },
  
  "metadata": {
    "evaluation_method": "hybrid",
    "automated_metrics": 3,
    "manual_metrics": 3,
    "test_scenarios": 10,
    "confidence": "high"
  }
}
```

---

## Competitive Differentiation

### What SkillsMP Offers:
- GitHub stars (popularity)
- Last update timestamp
- Basic filtering
- **NO TESTING**

### What We Offer:
✅ Actual activation testing  
✅ Task completion validation  
✅ Consistency measurement  
✅ Token cost profiling  
✅ Context limit warnings  
✅ Actionable recommendations  

**We are the ONLY platform that actually tests skills.**

---

## Success Criteria

✅ Evaluate 20-50 skills in 3 days  
✅ Manual validation confirms automated scores ±1 point  
✅ Users can make informed decisions from scorecards  
✅ Every metric includes specific recommendations  
✅ Solve real user pain points (validated by research)  
✅ Create defensible competitive moat through testing  

---

## Next Actions

1. ✅ Research user pain points - COMPLETE
2. ✅ Validate metrics - COMPLETE
3. ✅ Design testing methodology - COMPLETE
4. 🚧 Build automation scripts
5. 🚧 Create manual testing templates
6. 🚧 Pull 20-50 skills from Anthropic GitHub
7. 🚧 Run evaluations
8. 🚧 Generate scorecards
9. 🚧 Build website with skill cards

**Ready to execute.**
