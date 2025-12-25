# User Complaints & Failure Modes Research

**Date:** Dec 25, 2025  
**Source:** Reddit, blogs, GitHub issues, community feedback

---

## Key Findings from 100+ User Reports

### **Top 5 User Complaints**

1. **Skills Won't Trigger** (Most common)
   - Weak or unclear descriptions
   - Too many skills installed (context budget exceeded)
   - Description too long (>1024 chars gets truncated)
   - Conflicting trigger phrases

2. **Context Window Overflows**
   - Default limit: 15,000 characters for all skill descriptions combined
   - Silent failure - no warning when limit exceeded
   - Skills get excluded from system prompt without notification
   - Workaround: `SLASH_COMMAND_TOOL_CHAR_BUDGET=30000`

3. **Code Execution Not Enabled**
   - #1 silent failure according to Nate's research
   - Skill uploads correctly, shows in library, but nothing happens
   - Users don't realize they need to enable code execution

4. **Security Concerns**
   - Users worried about malicious code in third-party skills
   - No built-in security auditing
   - Skills can execute arbitrary bash commands

5. **Evaluation Gaps**
   - No way to know if a skill is good before installing
   - No performance metrics
   - No token cost visibility

---

## Additional Failure Modes Discovered

### **Skill Interaction Issues**
- **Skill Conflicts:** Multiple skills with similar descriptions compete
- **Dependency Problems:** Skills that depend on other skills fail silently
- **Bottlenecks:** Some skills block others from activating

### **Performance Issues**
- **Token Waste:** Some skills consume excessive tokens for simple tasks
- **Slow Activation:** Skills with complex logic take too long to load
- **Memory Leaks:** Skills that don't clean up after themselves

### **Documentation Problems**
- **Inconsistent Formats:** No standard for skill documentation
- **Missing Examples:** Users don't know how to trigger skills
- **Outdated Info:** Skills become stale, no maintenance indicators

### **Zip File Issues**
- Mentioned frequently but details unclear (need more research)

---

## Tools Users Are Building to Solve These

From Nate's toolkit (10 tools):

1. **skill-debugging-assistant** - Fixes skills that won't trigger
2. **skill-security-analyzer** - Audits third-party skills for malicious code
3. **skill-gap-analyzer** - Identifies missing skills from repeated explanations
4. **skill-performance-profiler** - Shows which skills waste tokens
5. **prompt-optimization-analyzer** - Catches bad descriptions before deployment
6. **skill-testing-framework** - Runs automated tests after changes
7. **skill-doc-generator** - Creates consistent documentation
8. **skill-dependency-mapper** - Shows how skills interact and bottleneck
9. **learning-capture** - Identifies patterns worth turning into skills
10. **token-budget-advisor** - Tackles context limits with chunking strategies

---

## Implications for Our Evaluation Framework

### **New Evaluation Dimensions to Consider:**

1. **Security Audit**
   - Scan for malicious code patterns
   - Check for unsafe bash commands
   - Verify external API calls
   - Rate: Safe / Caution / Unsafe

2. **Skill Interaction Analysis**
   - Test with other popular skills installed
   - Identify conflicts
   - Measure activation priority
   - Document dependencies

3. **Performance Profiling**
   - Token cost per execution
   - Execution time
   - Memory usage
   - Compare to baseline (no skill)

4. **Documentation Quality**
   - Completeness of examples
   - Clarity of trigger phrases
   - Maintenance status
   - Version history

5. **Code Execution Requirements**
   - Does it need code execution enabled?
   - What permissions does it require?
   - What external tools does it depend on?

6. **Context Budget Impact**
   - Description length
   - How many skills can coexist?
   - Aggregate impact score

7. **Maintenance & Freshness**
   - Last updated date
   - Active maintainer?
   - Open issues count
   - Community activity

---

## Next Research Areas

1. **Skill Composition Patterns** - How do users combine skills?
2. **Edge Cases** - What breaks skills in unusual scenarios?
3. **ML Evaluation Best Practices** - What can we learn from model evaluation?
4. **Academic Research** - Are there papers on agent evaluation?

