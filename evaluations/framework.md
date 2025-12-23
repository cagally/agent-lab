# Agent Skills Evaluation Framework v1.0

**Purpose:** Provide fast, actionable quality assessments for agent skills that help users discover, evaluate, and activate skills effectively.

**Design Principle:** Optimize for speed and practical utility. We need to evaluate 20-50 skills quickly while maintaining enough rigor to be genuinely useful.

---

## Evaluation Methodology

### Two-Track Approach

**Track 1: Automated Analysis (GPT-Based)**  
We run each skill through a specialized GPT prompt that analyzes the skill's description, body, parameters, and documentation. This provides consistent, scalable baseline assessments across all dimensions.

**Track 2: Manual Testing (Limited)**  
We conduct selective manual testing in Claude Code for high-priority skills or where automated analysis needs validation. This provides real-world activation data and performance insights.

---

## Evaluation Dimensions

### 1. Clarity Score (0-10)

**What it measures:** How well the skill communicates its purpose, usage, and value to users.

**Automated Analysis:**
- Description quality and completeness
- Parameter documentation clarity
- Use case examples provided
- Technical jargon vs. plain language ratio

**Manual Testing:**
- User comprehension (can a non-technical person understand what this does?)
- Discoverability (would users find this when they need it?)

**Output:** Numerical score + specific improvement recommendations

---

### 2. Activation Reliability (0-10)

**What it measures:** How consistently and easily the skill activates when needed.

**Automated Analysis:**
- Keyword clarity and specificity
- Potential for false positives/negatives
- Activation trigger design (explicit vs. organic)
- Conflict potential with other skills

**Manual Testing:**
- Real activation rate across 5-10 test scenarios
- Activation method (keyword vs. organic description)
- Debugging difficulty when activation fails

**Output:** Numerical score + activation method + recommended keywords/phrases

---

### 3. Performance Quality (0-10)

**What it measures:** How well the skill executes its intended function and delivers value.

**Automated Analysis:**
- Code quality indicators (error handling, edge cases)
- Scope appropriateness (not too narrow, not too broad)
- Dependencies and external requirements
- Maintenance signals (last updated, version info)

**Manual Testing:**
- Output accuracy and usefulness
- Speed and efficiency
- Error handling in practice
- Edge case performance

**Output:** Numerical score + performance notes + limitations

---

### 4. Hallucination Risk (Low/Medium/High)

**What it measures:** Likelihood the skill will produce incorrect, misleading, or fabricated outputs.

**Automated Analysis:**
- Deterministic vs. generative nature
- External data dependencies
- Verification mechanisms present
- Scope for creative interpretation

**Manual Testing:**
- Observed hallucination instances
- Output consistency across runs
- Accuracy validation where possible

**Output:** Risk level + specific risk factors + mitigation suggestions

---

### 5. Use Case Fit (Primary/Secondary/Niche)

**What it measures:** How broadly applicable and valuable the skill is to users.

**Automated Analysis:**
- Problem space size and frequency
- Target user breadth
- Competitive alternatives
- Skill category and domain

**Manual Testing:**
- Real-world applicability assessment
- User demand signals

**Output:** Category + target user profile + common use cases

---

## Scorecard Output Format

Each evaluated skill produces a structured scorecard in JSON format:

```json
{
  "skill_name": "string",
  "skill_id": "string",
  "evaluation_date": "YYYY-MM-DD",
  "version": "string",
  "source": "anthropic|skillsmp|community",
  
  "scores": {
    "clarity": 8,
    "activation_reliability": 6,
    "performance": 9,
    "overall": 7.7
  },
  
  "ratings": {
    "hallucination_risk": "low|medium|high",
    "use_case_fit": "primary|secondary|niche"
  },
  
  "activation": {
    "method": "keyword|organic|hybrid",
    "recommended_triggers": ["keyword1", "phrase2"],
    "activation_rate": "70%",
    "notes": "string"
  },
  
  "insights": {
    "strengths": ["string", "string"],
    "limitations": ["string", "string"],
    "best_for": "string",
    "avoid_if": "string"
  },
  
  "recommendations": {
    "activation_tips": "string",
    "usage_guidance": "string",
    "improvement_suggestions": "string"
  },
  
  "metadata": {
    "evaluation_method": "automated|manual|hybrid",
    "test_scenarios": 5,
    "last_updated": "YYYY-MM-DD"
  }
}
```

---

## Implementation Plan

### Phase 1: Automated Pipeline (Days 1-2)

We build a GPT-based evaluation pipeline that processes skill files and generates scorecards. The system uses a specialized prompt that embodies our evaluation criteria, outputs structured JSON for each skill, and processes 20-50 skills rapidly with consistent methodology.

### Phase 2: Manual Validation (Days 2-3)

We conduct selective manual testing for high-priority skills (top 10-15), validate automated scores with real-world data, and refine the automated prompt based on discrepancies.

### Phase 3: Continuous Improvement (Post-Launch)

We collect user feedback on accuracy, iterate on evaluation criteria, and expand manual testing coverage as we scale.

---

## Success Criteria

**Speed:** Evaluate 20-50 skills within 2 days  
**Utility:** Users can make informed decisions based on scorecards  
**Accuracy:** Manual validation confirms automated scores within ±1 point  
**Actionability:** Every scorecard includes specific usage recommendations  

---

## Next Steps

1. Build the GPT evaluation prompt
2. Create automation script to process skills
3. Define the initial skill set (20-50 from Anthropic)
4. Run automated evaluations
5. Conduct manual testing for validation
6. Generate final scorecards for website integration
