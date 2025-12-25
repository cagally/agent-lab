# Context Safety Clarification - Progressive Disclosure

**Date:** Dec 25, 2025  
**Status:** Critical Finding - Framework Update Required

---

## The User Was Right

After reviewing Anthropic's official engineering blog on Agent Skills, I need to correct my understanding of the "context safety" problem.

## How Skills Actually Work: Progressive Disclosure

Skills use a **three-level progressive disclosure system**:

### **Level 1: Metadata (Always Loaded)**
- Only the `name` and `description` fields from YAML frontmatter
- Loaded into system prompt at startup
- **This is what counts against the context budget initially**
- Description field has a **1024 character limit** (enforced by Claude Code)

### **Level 2: SKILL.md Body (Loaded On-Demand)**
- The full markdown content of SKILL.md
- **Only loaded when Claude decides the skill is relevant**
- Claude invokes a tool (Bash/Read) to load the file into context
- This happens dynamically during the conversation

### **Level 3: Supporting Files (Loaded As-Needed)**
- Additional files referenced in SKILL.md (e.g., `forms.md`, `reference.md`)
- **Only loaded when Claude navigates to them**
- Can be effectively unbounded in size
- Code files can be executed without loading into context

---

## What This Means for Context Safety

### **The Real Constraint: Description Length**

The actual constraint is **NOT** the total SKILL.md file size. It's the **description field** in the YAML frontmatter.

**Hard Limit:** 1024 characters per description

**Aggregate Concern:** If you have 100 skills installed, you have 100 descriptions loaded at startup. At maximum, this is:
- 100 skills × 1024 chars = 102,400 characters
- This WOULD exceed the context window

**But in practice:**
- Most descriptions are 100-300 characters
- Realistic aggregate: 20 skills × 200 chars = 4,000 characters (safe)

### **The Real Problem: Description Quality, Not Size**

The actual issue is **not** context budget exhaustion. It's:

1. **Vague Descriptions** - Claude doesn't know when to activate the skill
2. **Overly Long Descriptions** - Waste context budget for no benefit
3. **Poor Trigger Phrases** - Skill doesn't activate when it should
4. **Conflicting Descriptions** - Multiple skills compete for the same triggers

---

## Updated Evaluation Metric: "Description Efficiency"

We need to replace "Context Safety" with a more accurate metric:

### **New Metric: Description Efficiency**

**What We Measure:**
1. **Description Length** (0-1024 chars)
2. **Clarity Score** (GPT-5 judge: 0-10)
3. **Trigger Specificity** (GPT-5 judge: 0-10)
4. **Context Efficiency** (information density: chars per concept)

**Scoring Rubric:**

| Description Length | Clarity | Specificity | Score | Status |
|-------------------|---------|-------------|-------|--------|
| 50-200 chars | High | High | 10 | ✅ Optimal |
| 200-400 chars | High | Medium | 8 | ✅ Good |
| 400-600 chars | Medium | Medium | 6 | ⚠️ Verbose |
| 600-1024 chars | Low | Low | 3 | ⚠️ Poor |
| >1024 chars | N/A | N/A | 0 | ❌ Invalid |

**Example Analysis:**

**Bad Description (Vague, 45 chars):**
```yaml
description: Helps with documents
```
- **Score: 2/10** - Too vague, won't activate reliably

**Good Description (Clear, 180 chars):**
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```
- **Score: 9/10** - Clear capabilities, explicit triggers

**Verbose Description (Wasteful, 850 chars):**
```yaml
description: This skill is designed to help you work with PDF files in a variety of ways. It can extract text content from PDFs, including tables and forms. It can also fill out PDF forms programmatically. Additionally, it supports merging multiple PDF files into a single document. You should use this skill whenever you encounter a PDF file, or when the user asks about PDFs, forms, or document extraction. It's particularly useful for automating document workflows and processing large batches of PDFs. The skill includes helper scripts for common operations and supports both simple and complex PDF manipulation tasks.
```
- **Score: 4/10** - Contains useful info but wastes 670 characters on fluff

---

## Implications for Our Framework

### **What We Got Wrong:**

1. ❌ **Assumption:** All SKILL.md content is loaded upfront
2. ❌ **Metric:** "Context Safety" measuring total file size
3. ❌ **Concern:** Skills exceeding 15k character limit

### **What We Should Actually Measure:**

1. ✅ **Description Efficiency** - Is the description concise and clear?
2. ✅ **Activation Reliability** - Does the skill activate when it should?
3. ✅ **Progressive Disclosure Quality** - Is content properly split across levels?
4. ✅ **Code Efficiency** - Are scripts executable tools vs context bloat?

---

## Updated Framework Changes Required

### **Remove:**
- "Context Safety" metric (based on false assumption)

### **Add:**
- **Description Efficiency** (0-10 score)
  - Length analysis
  - Clarity assessment (GPT-5)
  - Trigger specificity (GPT-5)
  - Information density calculation

### **Enhance:**
- **Activation Rate Testing**
  - Now even more critical since description is the primary trigger
  - Test with 20+ prompts (explicit, implicit, edge cases)
  
- **Progressive Disclosure Analysis**
  - Is SKILL.md lean or bloated?
  - Are supporting files properly separated?
  - Is code executable vs loaded into context?

---

## Key Insight

The user's intuition was correct: **Claude dynamically loads skills on-demand**, not all at once. The real constraint is the **quality and efficiency of the description field**, not the total size of the skill.

This is actually **better news** for our platform:
- Skills can be arbitrarily large (via supporting files)
- The bottleneck is description quality, which we can measure and improve
- Our evaluation can focus on **activation reliability** and **description optimization**

---

## Next Steps

1. Update evaluation-framework-v3.md to replace "Context Safety" with "Description Efficiency"
2. Build GPT-5 based description analyzer
3. Create description optimization recommendations
4. Test our 12 skills with the corrected understanding

---

## Sources

- Anthropic Engineering Blog: "Equipping agents for the real world with Agent Skills"
- Claude Code Documentation: Agent Skills
- Direct observation of skill loading behavior in Claude Code
