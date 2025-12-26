# Skill Evaluation Results Template

**Instructions:** Copy this template for each skill you evaluate. Fill in all fields based on your testing.

---

## Skill Information

- **Skill Name:** `[skill-name]`
- **Repository:** `[github-url]`
- **Stars:** `[count]`
- **Last Updated:** `[date]`
- **Evaluator:** `[your-name]`
- **Evaluation Date:** `[date]`

---

## Evaluation Scores

### Hurdle Criteria (Pass/Fail)

| Dimension | Result | Notes |
|-----------|--------|-------|
| **1. Activation Rate** | ☐ Pass ☐ Fail | Activated on [X]/10 prompts |
| **2. Task Completion** | ☐ Pass ☐ Fail | [Brief description of completion] |

**Overall Hurdle:** ☐ PASS ☐ FAIL

---

### Quality Criteria (0-10 Scale)

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 3 | **Description Efficiency** | [X]/10 | Clarity: [X], Specificity: [X], Density: [X] |
| 4 | **Output Consistency** | [X]/10 | Similarity score: [X]% |
| 5 | **Token Efficiency** | [X]/10 | Desc: [X] chars, Body: [X] chars |
| 6 | **Grounding & Faithfulness** | [X]/10 | Hallucinations: [count], Verified claims: [X]/[Y] |
| 7 | **Failure Mode Resistance** | [X]/10 | Graceful failures: [X]/5 |
| 8 | **Security Audit** | [X]/10 | Rating: [Safe/Caution/Unsafe], Issues: [count] |
| 9 | **Multi-Skill Compatibility** | [X]/10 | Degradation: [X]%, Conflicts: [list] |
| 10 | **Tool Call Correctness** | [X]/10 | Correct calls: [X]/[Y] |

**Total Quality Score:** [X]/90

---

### Metadata

| Dimension | Value |
|-----------|-------|
| **11. Maintenance Status** | ☐ Active ☐ Stale ☐ Archived |
| Last Commit | [date] |
| Open Issues | [count] |
| Recent Activity | [description] |

---

## Overall Assessment

**Final Score:** [X]/100 (Hurdles + Quality)

**Rating:**
- 90-100: ⭐⭐⭐⭐⭐ Excellent
- 75-89: ⭐⭐⭐⭐ Very Good
- 60-74: ⭐⭐⭐ Good
- 45-59: ⭐⭐ Fair
- 0-44: ⭐ Poor

**Recommendation:**
- ☐ **Highly Recommended** - Production-ready, no major issues
- ☐ **Recommended** - Good quality, minor issues
- ☐ **Use with Caution** - Works but has notable limitations
- ☐ **Not Recommended** - Significant issues or failures

---

## Detailed Findings

### Strengths
1. [Strength 1]
2. [Strength 2]
3. [Strength 3]

### Weaknesses
1. [Weakness 1]
2. [Weakness 2]
3. [Weakness 3]

### Failure Modes Discovered
1. **[Failure Mode 1]:** [Description and reproduction steps]
2. **[Failure Mode 2]:** [Description and reproduction steps]

### Use Cases
**Best For:**
- [Use case 1]
- [Use case 2]

**Not Suitable For:**
- [Use case 1]
- [Use case 2]

### Compatibility Notes
**Works Well With:**
- [Skill 1]
- [Skill 2]

**Conflicts With:**
- [Skill 1]: [Description of conflict]

---

## Test Evidence

### Activation Test Results

| Prompt # | Type | Prompt | Activated? | Notes |
|----------|------|--------|------------|-------|
| 1 | Explicit | "[prompt]" | ☐ Yes ☐ No | |
| 2 | Explicit | "[prompt]" | ☐ Yes ☐ No | |
| 3 | Explicit | "[prompt]" | ☐ Yes ☐ No | |
| 4 | Explicit | "[prompt]" | ☐ Yes ☐ No | |
| 5 | Implicit | "[prompt]" | ☐ Yes ☐ No | |
| 6 | Implicit | "[prompt]" | ☐ Yes ☐ No | |
| 7 | Implicit | "[prompt]" | ☐ Yes ☐ No | |
| 8 | Implicit | "[prompt]" | ☐ Yes ☐ No | |
| 9 | Edge Case | "[prompt]" | ☐ Yes ☐ No | |
| 10 | Edge Case | "[prompt]" | ☐ Yes ☐ No | |

**Activation Rate:** [X]/10 = [X]%

### Consistency Test Results

| Run # | Output Summary | Similarity to Run 1 |
|-------|----------------|---------------------|
| 1 | [summary] | 100% (baseline) |
| 2 | [summary] | [X]% |
| 3 | [summary] | [X]% |

**Average Similarity:** [X]%

### Adversarial Test Results

| Test # | Prompt | Behavior | Score |
|--------|--------|----------|-------|
| 1 | Ambiguous request | [description] | [X]/2 |
| 2 | Conflicting requirements | [description] | [X]/2 |
| 3 | Out-of-scope | [description] | [X]/2 |
| 4 | Malicious intent | [description] | [X]/2 |
| 5 | Impossible task | [description] | [X]/2 |

**Total Adversarial Score:** [X]/10

---

## Recommendations for Improvement

1. **[Improvement 1]:** [Specific suggestion]
2. **[Improvement 2]:** [Specific suggestion]
3. **[Improvement 3]:** [Specific suggestion]

---

## Evaluator Notes

[Any additional observations, context, or notes that don't fit elsewhere]
