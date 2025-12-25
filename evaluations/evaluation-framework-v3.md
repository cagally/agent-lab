# Agent Skills Evaluation Framework v3.0

**Date:** Dec 25, 2025  
**Status:** Proposed, Ready for Review  
**Authors:** Manus AI & Oscar Wiren

---

## 1. Introduction: Our Mission & Core Philosophy

The agent skills ecosystem is a chaotic, high-potential space suffering from a critical lack of trust and quality assurance. Users are unable to reliably discover, activate, or evaluate skills, leading to frustration and abandonment. Existing marketplaces are mere aggregators, failing to address the fundamental user pain point: **"Does this skill actually work, and can I trust it?"**

Our mission is to solve this problem by becoming the definitive, trusted evaluation platform for agent skills. We are not building another aggregator; we are building the **"Surge AI for Skills"**—a rigorous, transparent, and user-centric quality assurance layer for the entire ecosystem.

Our core philosophy, inspired by the methodologies of industry leaders like Surge AI and Mercor AI, is that **rigorous, rubric-based evaluation is the new frontier** [1][2]. While others focus on quantity, we will differentiate through quality, providing the actionable insights that both skill creators and end-users desperately need. We will move beyond simple "it works" checks to document *how* it works, *when* it fails, and *why* it matters.

This document outlines our comprehensive framework for achieving this mission, balancing the need for immediate, high-impact results (MVP) with a long-term vision to become the central nervous system for skill quality and improvement.

---

## 2. The Evaluation Methodology: A Hybrid, Rubric-Based Approach

We will employ a hybrid methodology that combines the scalability of **automated analysis** with the nuance and depth of **human-led, rubric-based testing**. Every skill will be subjected to a standardized evaluation process designed to be repeatable, scalable, and difficult to game.

Our approach is built on two core components:

1.  **The Evaluation Rubric:** A multi-dimensional rubric that breaks down skill quality into discrete, measurable criteria. This moves us from subjective opinion to objective, data-driven assessment.
2.  **The Testing Process:** A multi-phase process that includes static analysis, automated testing with AI-powered judges (autograders), and targeted manual testing to uncover nuanced failure modes.

### 2.1. The Evaluation Rubric

Our rubric is designed to directly address the user pain points identified in our research [3]. It is divided into two primary categories: **Hurdle Criteria** (non-negotiable, pass/fail gates) and **Quality Criteria** (graded on a 0-10 scale).

| Category | Metric | Type | Why It Matters (User Pain Point) |
| :--- | :--- | :--- | :--- |
| **Hurdle Criteria** | **Activation Rate** | Pass/Fail | Solves the #1 user complaint: "My skills won't activate." A skill that doesn't run is useless. |
| | **Task Completion** | Pass/Fail | Addresses core reliability. The skill must be able to complete its fundamental stated purpose. |
| **Quality Criteria** | **Output Consistency** | Scored (0-10) | Solves the "same prompt, different results" frustration, ensuring predictability. |
| | **Token Efficiency** | Scored (0-10) | Addresses explicit user complaints about cost and "burning through tokens." |
| | **Context Safety** | Scored (0-10) | Prevents silent failures from exceeding the context window, a hidden but critical issue. |
| | **Grounding & Faithfulness** | Scored (0-10) | Measures the rate of hallucination and factual inaccuracy, building user trust. |
| | **Failure Mode Resistance** | Scored (0-10) | Quantifies how gracefully a skill handles edge cases, ambiguity, and adversarial prompts. |
| **Metadata** | **Maintenance Status** | Informational | Addresses user concerns about stale or abandoned skills. |

#### **Hurdle Criteria Explained**

Inspired by Mercor AI's methodology [2], these are the absolute minimum requirements for a skill to be considered functional. A skill must pass both hurdles to receive a full evaluation and a final score.

*   **Activation Rate:** We test with a suite of 10 prompts (5 designed to activate, 5 designed to test for false positives). A skill must achieve a minimum activation success rate (e.g., 80% on correct prompts, <20% on incorrect prompts) to pass.
*   **Task Completion:** The skill must successfully complete a simple, canonical task from start to finish. Failure to do so indicates a fundamental flaw.

#### **Quality Criteria Explained**

These metrics are graded on a 0-10 scale using a combination of automated analysis and human-validated autograders (GPT-5). This is where we measure the *quality* of the skill in detail.

*   **Output Consistency:** We run the same prompt 3-5 times and measure the semantic similarity of the outputs. High scores are given for deterministic skills or generative skills with low, controlled variance.
*   **Token Efficiency:** We measure both the static cost (description length) and the dynamic cost (average execution tokens) against a no-skill baseline to calculate the true overhead.
*   **Context Safety:** A fully automated check of the skill's description length against the context window limit (e.g., 15k characters). Skills that consume a dangerous percentage of the budget are penalized heavily.
*   **Grounding & Faithfulness:** For skills that make factual claims or use external data, we measure the rate of hallucination. This is critical for building trust.
*   **Failure Mode Resistance:** We intentionally test the skill with ambiguous, complex, and adversarial prompts to see how it behaves. Does it ask clarifying questions, fail gracefully, or produce garbage output?

---

## 3. The Testing Process: From Static Analysis to Adversarial Testing

Our three-phase process ensures both breadth and depth in our evaluations.

**Phase 1: Static & Automated Analysis (The Triage)**
*   **Action:** Every skill is automatically analyzed upon ingestion.
*   **Metrics Checked:** Context Safety, Maintenance Status, SKILL.md quality (clarity, completeness).
*   **Output:** A preliminary safety and quality check. Skills with major red flags (e.g., massive context usage) are flagged immediately.

**Phase 2: Rubric-Based Autograding (The Scalable Evaluation)**
*   **Action:** Each skill is run through a standardized test suite of 20+ prompts, covering a spectrum of complexity and intent.
*   **The Judge:** A fine-tuned GPT-5 model acts as an "autograder," evaluating the skill's output against our detailed rubric. It scores each quality criterion and provides a rationale.
*   **Human-in-the-Loop:** A human expert reviews a random 10-20% of the autograder's results to ensure accuracy, calibrate the AI judge, and handle nuanced cases.

**Phase 3: Manual Deep Dive & Adversarial Testing (The Moat)**
*   **Action:** The top 10-20% of skills, or those with interesting failure modes, undergo a manual deep dive by a human expert.
*   **Goal:** To find the subtle failure modes, edge cases, and real-world limitations that automated systems miss. This is where we emulate the "Red Teaming" approach used by Surge AI [1].
*   **Output:** Rich, qualitative insights on when to use a skill, when to avoid it, and how to get the most out of it. This analysis will be our most valuable, defensible asset.

---

## 4. Implementation Roadmap: From MVP to Market Leader

We will execute this vision in three distinct horizons, ensuring we can move fast now while building a durable, long-term advantage.

### **Horizon 1: MVP (Next 3-5 Days)**

*   **Goal:** Launch with a core set of 12-20 rigorously evaluated skills.
*   **Focus:** Execute a "lite" version of the framework on our initial set of skills. We will manually perform the autograder's role to move faster.
*   **Process:**
    1.  **Finalize v3 Rubric:** Lock in the metrics and scoring for the MVP.
    2.  **Create Test Suites:** Develop the 20-prompt test suite for our initial skill categories (e.g., code generation, writing assistance).
    3.  **Execute Manual Evals:** Run all 12 downloaded skills through the full rubric manually.
    4.  **Generate v1 Scorecards:** Create detailed, user-facing scorecards for each skill, highlighting key findings and failure modes.
    5.  **Build MVP Website:** A simple, clean interface to display these scorecards.
*   **Outcome:** We launch as the first platform with genuinely tested skills, immediately establishing our authority and solving a real user need.

### **Horizon 2: Scale & Automation (First 2 Months)**

*   **Goal:** Scale our evaluation pipeline to hundreds of skills and automate the majority of the process.
*   **Process:**
    1.  **Build the Autograder:** Implement the GPT-5 based autograder to handle 80% of the evaluation workload.
    2.  **Develop Environment Generation:** Create standardized testing environments for different skill categories.
    3.  **Implement Adversarial Testing:** Systematically generate and test for common failure modes.
    4.  **Expand Coverage:** Scale up to the top 100-200 skills on the market.

### **Horizon 3: The Platform Vision (6-12 Months)**

*   **Goal:** Become the central, indispensable platform for skill quality and improvement.
*   **Process:**
    1.  **Training Data Generation:** Package our detailed failure mode analysis into training datasets that skill creators can use to fine-tune their skills.
    2.  **Creator-Facing Platform:** Offer a self-serve portal where developers can submit their skills for evaluation, receive a private quality report, and get actionable feedback for improvement.
    3.  **API & Integration:** Provide an API for our evaluation data, allowing other marketplaces and agent platforms to display our quality scores.
    4.  **Community & Benchmarking:** Establish industry-wide benchmarks for skill quality and host a community for best practices.

---

## 5. Next Steps

This document provides the strategic blueprint. The immediate next step is to review and finalize this framework. Upon approval, we will move directly into executing the MVP roadmap.

1.  **Review & Approve:** Does this framework align with our vision? Are there any gaps?
2.  **Finalize MVP Rubric:** Lock in the specific scoring for each metric for our initial launch.
3.  **Begin MVP Execution:** Start the manual evaluation of our first 12 skills.


## References

[1] Surge AI. (2023). *How Anthropic uses Surge AI to Train and Evaluate Claude*. [https://surgehq.ai/blog/anthropic-surge-ai-rlhf-platform-train-llm-assistant-human-feedback](https://surgehq.ai/blog/anthropic-surge-ai-rlhf-platform-train-llm-assistant-human-feedback)

[2] Mercor. (2025). *Introducing the AI Consumer Index*. [https://www.mercor.com/blog/introducing-the-ai-consumer-index/](https://www.mercor.com/blog/introducing-the-ai-consumer-index/)

[3] Manus AI. (2025). *Agent Skills Evaluation Framework v2.0 (FINAL)*. `/home/ubuntu/agent-lab/evaluations/framework-v2-final.md`
