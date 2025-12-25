# Mercor AI Research Notes

**Date:** Dec 25, 2025  
**Purpose:** Understand Mercor's evaluation methodology to inform our skill evaluation framework

---

## Key Findings

### Mercor's Core Methodology

**What They Do:**
- Build evaluations (evals) for AI models
- Focus on real-world consumer and enterprise tasks
- Pioneer environment generation using autograders
- Create RL (Reinforcement Learning) environments for training

**Their Philosophy:**
> "Evals are the new PRD. Progress in accelerating knowledge work will converge on building environments and evaluations that map real workspaces and deliverables."

---

## AI Consumer Index (ACE) - Rubric-Based Evaluation

### Methodology:

**1. Rubric-Based Grading**
- Each task has a rubric of prompt-specific criteria
- Scalable grading of model responses
- Fine-grained insight into model performance

**2. Hurdle Criteria**
- Must be passed before further rewards can be unlocked
- Ensures model meets user's core objective
- Examples:
  - Shopping: Return the requested type of product
  - DIY: Provide a solution to the user's problem
- **Purpose:** Minimize reward hacking (prevent irrelevant responses from scoring)

**3. Grounding Criteria**
- Penalize models for hallucinating (claims not supported by sources)
- Penalize non-working links
- Account for 42% of Gaming criteria, 74% of Shopping criteria
- Measure: % of grounding criteria failed

**4. Criteria Tagging**
- Every rubric item tagged with criteria type
- Enables loss analysis of model performance
- Examples:
  - Quantity requirements (easy - 80% success)
  - Compatibility requirements (hard - <40% success)
  - Safety warnings (hard - <50% success)
  - Working links (very hard - negative mean score)

---

## The Era of Evals - Training Philosophy

### Key Concepts:

**1. Training on Verifiable Rewards**
- RL environments reward outcomes and intermediate steps
- Models take many attempts, using test-time compute to "think"
- Human-created autograders reward "good" attempts
- Reinforces correct chains of thought

**2. Spectrum of Rigidity**

| Objective Domains | Subjective Domains |
|-------------------|-------------------|
| Clear state spaces, action spaces | Difficult to measure accuracy |
| Games, math, code, biology | Investment memos, legal briefs, therapy |
| Near game-like verifiability | Multiple valid expert opinions |
| Early RL success (AlphaProof, DeepSeek R1) | Rubric-based rewards needed |

**3. Rubric-Based Rewards**
- Way to learn from messiness of expert human opinions
- Roots in Constitutional AI and RLAIF (Anthropic)
- Exciting area of research

**4. Environments Create Experience**
- Durable sources of experiential data
- Serve to train AND evaluate models
- Humans remain integral part of learning loop

---

## Application to Our Skills Framework

### What "Mercor for Skills" Means:

**Core Insight:** Skills are like "subjective domain" tasks - multiple valid approaches, expert opinions vary, hard to measure objectively.

**Rubric-Based Evaluation for Skills:**

1. **Hurdle Criteria** (Must Pass)
   - Does the skill activate when it should?
   - Does it complete the stated task?
   - Is the output relevant to the prompt?

2. **Quality Criteria** (Graded)
   - Output consistency (deterministic vs variable)
   - Token efficiency (cost-effectiveness)
   - Context budget usage (will it load?)
   - Grounding (hallucination rate)

3. **Criteria Tagging** (Loss Analysis)
   - Tag each test by:
     - Task complexity (simple, medium, complex)
     - Prompt type (explicit, implicit, ambiguous)
     - Domain (code, writing, analysis, etc.)
     - Failure mode (activation, completion, quality)

4. **Autograders** (Automated Testing)
   - GPT-5 as judge for quality criteria
   - Automated checks for objective criteria
   - Human validation for edge cases

---

## Mercor's Results - What We Can Learn

### ACE Results:
- Top model (GPT 5.1) scored only 56.1%
- Models routinely fail on consumer tasks
- No models score over 50% on Shopping tasks
- Substantial differences across domains

**Lesson:** Even frontier models fail frequently on real-world tasks. Skills will fail too. Our value is in documenting WHEN and WHY they fail.

### Loss Analysis Insights:
- Models perform well at simple requirements (80%+)
- Models struggle with nuanced requests (<40%)
- Some criteria types have negative mean scores (so difficult models score worse than baseline)

**Lesson:** We need to test skills across difficulty spectrum and document where they break down.

---

## Framework Design Implications

### MVP (Now):

**Rubric Structure:**
```
For each skill:
  Hurdle Criteria (Pass/Fail):
    - Activation (10 prompts)
    - Task Completion (5 tasks)
  
  Quality Criteria (0-10 scale):
    - Output Consistency
    - Token Efficiency
    - Context Safety
    - Grounding (no hallucinations)
  
  Criteria Tags:
    - Task complexity
    - Prompt type
    - Failure mode
```

**Autograders:**
- GPT-5 judges quality criteria
- Python scripts for objective metrics
- Human validation for 10-20% of tests

**Loss Analysis:**
- Tag every test result
- Identify patterns: "Fails on complex multi-step tasks"
- Document: "Works best for simple, explicit prompts"

### V2 (Month 1):

**Environment Generation:**
- Create test environments for each skill category
- Standardized test suites
- Automated regression testing

**Adversarial Testing:**
- Red team approach to find edge cases
- Deliberately try to break skills
- Document failure modes

**Comparative Benchmarking:**
- Test skill vs no-skill baseline
- Measure actual value added
- Cost-benefit analysis

### Vision (6-12 months):

**Training Data Generation:**
- Failure modes → improvement recommendations
- Synthetic test case generation
- Skill quality improvement loop

**Platform for Skill Creators:**
- Test before publishing
- Get quality score
- Improvement suggestions

---

## Key Takeaways

1. **Rubrics > Ad-hoc Testing** - Structured, repeatable evaluation frameworks
2. **Hurdle Criteria** - Prevent reward hacking, ensure core objectives met
3. **Criteria Tagging** - Enable loss analysis and pattern recognition
4. **Autograders** - Scale evaluation with AI judges + human validation
5. **Failure Documentation** - The value is in knowing WHEN and WHY things fail
6. **Spectrum of Difficulty** - Test across simple → complex tasks

**Our Moat:** Be the "Mercor of Skills" - rigorous, rubric-based evaluation that documents failure modes and provides actionable insights.

---

## Sources

- https://www.mercor.com/blog/introducing-the-ai-consumer-index/
- https://www.mercor.com/blog/welcome-to-the-era-of-evals/
