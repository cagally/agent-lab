# User Research Notes - Agent Skills Pain Points

**Research Date:** Dec 23, 2025  
**Purpose:** Validate evaluation metrics against real user complaints and needs

---

## Initial Search Results - Key Findings

### Top User Pain Points Identified:

1. **Activation Issues (CRITICAL)**
   - "Skills invocation unreliable" - Reddit r/ClaudeCode
   - "Skills don't auto-activate in spawned agents" - GitHub issue #14016
   - "The activation of the Claude Skill is extremely unstable" - GitHub community
   - "Can't get Skills to be used in anyway" - Reddit
   - "Claude Code skills not triggering? It might not see them" - blog post
   - **Quote:** "You have to put explicit instructions in CLAUDE.md for WHEN to use the specific skills. Doing this I've had 100% reliability so far"

2. **Token/Cost Issues (CRITICAL)**
   - "It struggles to digest context efficiently, burns through tokens, and often still fails to act correctly" - LinkedIn
   - Skills with long descriptions cause system prompt bloat

3. **Context/Performance Issues**
   - "Having serious issues since started playing with skills" - Reddit
   - "As soon as you enable skills, it DISABLED the analysis tool function which kills file processing"
   - Too many skills or long descriptions break the system

4. **Unclear Instructions/Documentation**
   - "I struggled with this a lot. The issues were mostly weak or unclear descriptions where Claude would read the desc and decide it wasn't necessary"
   - "Skills aren't documentation. They're active instructions for a specific task"

5. **Discovery/Recognition Issues**
   - "Claude Code Skills Not Recognised? Here's the Fix!" - blog post
   - "Skills not showing up in Claude Code?" - Reddit
   - "Platform packaging confusion. Skills have one format but three completely different distribution modes"

---

## URLs to Deep Dive:

1. https://natesnewsletter.substack.com/p/i-watched-100-people-hit-the-same (100+ people hitting same issues)
2. https://www.reddit.com/r/ClaudeAI/comments/1oevdmg/having_serious_issues_since_started_playing_with/
3. https://scottspence.com/posts/claude-code-skills-not-recognised
4. https://blog.fsck.com/2025/12/17/claude-code-skills-not-triggering/
5. https://www.reddit.com/r/ClaudeCode/comments/1prpe7j/skills_invocation_unreliable/
6. https://github.com/anthropics/claude-code/issues/14016

---

## Preliminary Metric Validation:

✅ **Activation Rate** - CONFIRMED CRITICAL (most common complaint)  
✅ **Speed/Cost (Tokens)** - CONFIRMED CRITICAL (major user pain)  
🟡 **Task Completion Rate** - Need to validate if users complain about this  
🟡 **Output Accuracy** - Need to validate  
🟡 **Maintenance Status** - Not seeing complaints yet  

---

## Next Steps:
- Read top 5-6 URLs in detail
- Look for more specific complaints about accuracy/reliability
- Check for maintenance/abandonment issues


---

## Deep Dive #1: Context Limits Breaking Skills

**Source:** https://blog.fsck.com/2025/12/17/claude-code-skills-not-triggering/

### Key Finding: THE INVISIBLE LIMIT

**The Problem:**
- Claude Code has a 15,000 character limit (≈4000 tokens) for skill descriptions in system prompt
- When you exceed this, skills are **silently excluded** from the system prompt
- No warning, no error - skills just don't work
- System prompt explicitly tells Claude NOT to use skills that aren't listed
- Result: Skills become completely invisible to Claude

**Quote:** "The way Claude knows about skills is that it builds a big list of skill names and descriptions and injects it into in the system prompt. The problems start when you've got too many skills or their description fields are too long."

**Workaround:** Set environment variable `SLASH_COMMAND_TOOL_CHAR_BUDGET=30000`

### Implications for Our Metrics:

✅ **Description Length/Efficiency** - NEW CRITICAL METRIC
- Users need to know if a skill has bloated descriptions
- This directly impacts whether skills work at all
- We should measure: character count, token efficiency

✅ **Activation Rate** - STILL CRITICAL
- But now we know WHY activation fails (context limits)
- We can test if skills fit within budget

---

## Deep Dive #2: The Common Problems (100+ Users)

**Source:** https://natesnewsletter.substack.com/p/i-watched-100-people-hit-the-same

### Top 5 Issues from Week One:

1. **Skills that won't trigger** (Most common)
2. **Issues with zip files**
3. **Context window overflows** (Confirms above finding)
4. **Security concerns** (Skills running code)
5. **How to evaluate Skills** (This is literally our business!)

### Tools Built to Solve These:

- **skill-debugging-assistant** - Fixes skills that won't trigger
- **skill-performance-profiler** - Shows which skills waste tokens ⭐
- **prompt-optimization-analyzer** - Catches bad descriptions ⭐
- **skill-testing-framework** - Runs automated tests ⭐
- **token-budget-advisor** - Tackles context limits ⭐

### Key Quote:
"Questions about how to evaluate Skills" - Users are explicitly asking for evaluation frameworks!



---

## Deep Dive #3: The Reliability Problem

**Source:** https://pub.towardsai.net/stop-using-claude-wrong-why-skills-are-the-solution-to-your-ai-reliability-problem-1e6466ed008d

### The Core User Frustration:

**Quote:** "You know that feeling when Claude gives you perfect output one minute, then complete garbage the next? Same prompt, wildly different results."

**The Problem:** UNPREDICTABILITY
- Users can't trust AI for actual work
- Same prompt = wildly different results
- "AI doesn't work for me" is the common complaint
- Skills solve this by providing deterministic frameworks

**Key Insight:** "This is the biggest shift in AI reliability since we figured out prompt engineering... it solves the exact problem that makes AI frustrating for actual work: unpredictability."

### Implications:

✅ **Consistency/Reliability** - This is THE pain point
- Users need to know if a skill produces consistent results
- "Does it work the same way every time?" is critical



---

## Competitive Analysis: SkillsMP (Existing Marketplace)

**Source:** https://skillsmp.com/

### What They Offer:

- **31,767 skills** indexed from GitHub
- AI-powered semantic search
- Category filtering
- Sort by: Stars (popularity) or Recent (recency)
- Filter by: marketplace.json presence
- Last update timestamps

### Quality Indicators They Use:

1. **GitHub Stars** - Primary quality signal
2. **Last Update Time** - Maintenance indicator
3. **marketplace.json** - Installation readiness
4. **Minimum 2 stars** - Basic quality filter

### What They DON'T Offer (Our Opportunity):

❌ No activation rate testing
❌ No performance/token cost metrics  
❌ No output accuracy validation
❌ No actual skill testing or evaluation
❌ No reliability/consistency metrics
❌ No user reviews or ratings
❌ No recommendations or comparisons

**Key Insight:** They're just aggregating and displaying. NO ONE is actually testing and evaluating these skills. This is our white space!

### User Pain Points from FAQ:

- "Are these skills safe to use?" - Security/trust concern
- "How often are skills updated?" - Maintenance concern
- Skills are "model-invoked" - activation is automatic, so reliability is critical

