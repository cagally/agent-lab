# Agent Skills Evaluation: Implementation Guide

**Date:** Dec 25, 2025  
**Goal:** Provide a step-by-step playbook for executing our 11-dimension evaluation framework, detailing the process, difficulty, automation, and time required for each dimension.

---

## Evaluation Workflow Overview

This guide outlines the practical steps to test each skill against our 11-dimension rubric. The process is designed to be rigorous yet efficient, blending automated analysis with expert manual testing. The total estimated time to evaluate a single skill is approximately **90-130 minutes**.

### Summary of Evaluation Dimensions

| #  | Dimension                  | Difficulty | Automation       | Time/Skill (mins) |
|----|----------------------------|------------|------------------|-------------------| 
| 1  | Activation Rate            | Easy       | Manual           | 5-10              |
| 2  | Task Completion            | Easy       | Manual           | 5-10              |
| 3  | Description Efficiency     | Medium     | Semi-Automated   | 5                 |
| 4  | Output Consistency         | Medium     | Semi-Automated   | 10-15             |
| 5  | Token Efficiency           | Easy       | Fully Automated  | <1                |
| 6  | Grounding & Faithfulness   | Hard       | Manual           | 15-20             |
| 7  | Failure Mode Resistance    | Medium     | Manual           | 10-15             |
| 8  | Security Audit             | Medium     | Semi-Automated   | 5-10              |
| 9  | Multi-Skill Compatibility  | Hard       | Manual           | 20-30             |
| 10 | Tool Call Correctness      | Medium     | Manual           | 10-15             |
| 11 | Maintenance Status         | Easy       | Fully Automated  | <1                |
|    | **Total Estimated Time**   |            |                  | **~90-130 mins**  |

---

## Detailed Execution Steps

### Hurdle Criteria (Pass/Fail)

#### 1. Activation Rate
- **Difficulty:** Easy
- **Automation:** Manual
- **Process:**
  1. Load the single skill into a clean Claude Code environment.
  2. Execute a pre-defined suite of 10 test prompts designed to cover explicit, implicit, and edge-case triggers.
  3. Record the number of successful activations.
  4. **Scoring:** Pass if activation rate is ≥ 80% (8/10 prompts); Fail otherwise.
- **Tools:** Claude Code, Test Prompt Suite (to be created).

#### 2. Task Completion
- **Difficulty:** Easy
- **Automation:** Manual
- **Process:**
  1. For the prompts that successfully activated the skill, proceed with the interaction.
  2. Determine if the skill achieves its core stated purpose for at least one of the successful activations.
  3. This is a simple, binary check: "Did it do the job?"
  4. **Scoring:** Pass if the core task is completed at least once; Fail otherwise.
- **Tools:** Claude Code.

### Quality Criteria (0-10 Scale)

#### 3. Description Efficiency
- **Difficulty:** Medium
- **Automation:** Semi-Automated (GPT-5 Judge)
- **Process:**
  1. Extract the `name` and `description` from the skill's YAML frontmatter.
  2. Feed the description into a GPT-5-powered evaluation script.
  3. The script will score the description on **Clarity**, **Specificity**, and **Information Density** based on a pre-defined rubric.
  4. **Scoring:** The final score is an average of the three sub-scores.
- **Tools:** Python script using OpenAI API, GPT-5, Evaluation Rubric.

#### 4. Output Consistency
- **Difficulty:** Medium
- **Automation:** Semi-Automated
- **Process:**
  1. Select one standard, non-trivial prompt from the test suite.
  2. Run the same prompt through the skill 3 times in separate, clean sessions.
  3. Use a semantic similarity script (e.g., using sentence transformers) to compare the three outputs.
  4. **Scoring:** Score is based on the average similarity score. Higher similarity = higher score.
- **Tools:** Claude Code, Python script for semantic similarity.

#### 5. Token Efficiency
- **Difficulty:** Easy
- **Automation:** Fully Automated
- **Process:**
  1. A script will parse the skill's `SKILL.md` file.
  2. It will measure the character count of the YAML `description` (static cost).
  3. It will measure the character count of the entire `SKILL.md` body (dynamic cost).
  4. **Scoring:** Score is on a curve. Shorter, more efficient skills get higher scores.
- **Tools:** Python script for file parsing.

#### 6. Grounding & Faithfulness
- **Difficulty:** Hard
- **Automation:** Manual
- **Process:**
  1. During manual testing, actively check for hallucinations or fabricated information.
  2. If the skill cites sources or provides data, manually verify the accuracy of 3-5 claims.
  3. For skills that summarize content, compare the summary to the source material for faithfulness.
  4. **Scoring:** Start at 10 and deduct points for each instance of hallucination or factual inaccuracy.
- **Tools:** Claude Code, Web Browser for fact-checking.

#### 7. Failure Mode Resistance
- **Difficulty:** Medium
- **Automation:** Manual
- **Process:**
  1. Execute a suite of 5 adversarial prompts designed to break the skill (e.g., ambiguous requests, conflicting requirements, out-of-scope tasks).
  2. Observe how the skill behaves. Does it fail gracefully, ask for clarification, or produce garbage?
  3. **Scoring:** Score based on a rubric that rewards graceful failure and penalizes catastrophic failure.
- **Tools:** Claude Code, Adversarial Prompt Suite.

#### 8. Security Audit
- **Difficulty:** Medium
- **Automation:** Semi-Automated
- **Process:**
  1. Run an automated script to scan the skill's files for dangerous patterns (e.g., `rm -rf`, `eval()`, hardcoded secrets).
  2. Manually review any flagged code for context and actual risk.
  3. Check for any external API calls to untrusted endpoints.
  4. **Scoring:** Safe (10), Caution (5), Unsafe (0). Any high-risk finding results in an automatic score of 0.
- **Tools:** Python script with regex for pattern matching, Manual code review.

#### 9. Multi-Skill Compatibility
- **Difficulty:** Hard
- **Automation:** Manual
- **Process:**
  1. Install the target skill alongside the 3 other most popular, unrelated skills.
  2. Run the activation test suite for the target skill again. Did the presence of other skills reduce its activation rate?
  3. Run the activation test suite for the other 3 skills. Does the target skill interfere with them?
  4. **Scoring:** Score based on the degradation in activation rate. No degradation = 10/10.
- **Tools:** Claude Code, Test Prompt Suite.

#### 10. Tool Call Correctness
- **Difficulty:** Medium
- **Automation:** Manual
- **Process:**
  1. For skills that use tools (e.g., Bash, Read), monitor the tool calls during testing.
  2. Verify if the correct tool was chosen for the task.
  3. Verify if the parameters passed to the tool were correct and well-formed.
  4. **Scoring:** Start at 10 and deduct points for each incorrect tool call or parameter.
- **Tools:** Claude Code (observing tool usage).

### Metadata

#### 11. Maintenance Status
- **Difficulty:** Easy
- **Automation:** Fully Automated
- **Process:**
  1. A script will use the GitHub API to fetch repository metadata.
  2. It will collect the date of the last commit, number of open issues, and recent commit activity.
  3. **Scoring:** This is not a 0-10 score but a status rating: Actively Maintained, Stale, or Archived.
- **Tools:** Python script using GitHub API.
