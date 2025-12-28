# Real-World Skill Usage Patterns

## Key Findings from Reddit Discussion

### How Many Skills Do Real Users Have?

**User 1:** "I have like 15 [skills]. They're all just replacements for mcp servers with api docs for different things (gmail, QuickBooks, iMessage, etc.)"

**User 2 (started with 250!):** "I'm working on a fairly large codebase - and I've mapped out 250-ish skills I could made"
- **Updated to:** "22 skills with consolidated reference and workflow files"
- **Lesson:** Started too granular, consolidated to ~22

**User 3:** "Claude can't see infinite skills... For that reason I feel the right answer is **no more skills than fits into system prompt context. For me that is about 85.**"

---

## Key Insights

### 1. **System Prompt Limit**
> "Claude can't see infinite skills. You can still tell Claude to invoke secret skills X, but other than that it won't use them."

**Implication:** There's a practical limit to how many skills Claude can "see" at once, estimated at ~85 skills max in system prompt.

### 2. **Token Management**
> "The benefit is the tokens for that skill are not loaded into context until/unless that skill is needed. Instead the name and description of the available skills is loaded along with CLAUDE.md."

**Implication:** Progressive disclosure works, but metadata for ALL skills is still loaded upfront.

### 3. **Typical Usage**
- **Small projects:** 5-15 skills
- **Large projects:** 20-30 skills (consolidated)
- **Maximum practical:** ~85 skills (system prompt limit)

### 4. **Best Practice: Consolidation**
User consolidated 250 skills → 22 skills by:
- Combining related skills
- Using reference files
- Creating workflow files

---

## Implications for Our Evaluation

**Real-world scenario:** Users have 10-30 skills installed

**For testing:**
- **2-3 skills per test** = Realistic for focused work
- **8 skills per test** = Upper bound of what users might have active
- **1 skill per test** = Not realistic (no competition)

**Recommendation:** Test with **2-3 skills** to match typical real-world usage.
