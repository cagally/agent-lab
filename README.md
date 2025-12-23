# Agent Lab - Knowledge Base

**Mission:** Build the #1 hub for Agent Skills. Make skills discoverable, evaluable, and usable for everyone.

**Current Phase:** Phase 1 - MVP Launch (Days 1-3)

---

## 📁 Repository Structure

```
agent-lab/
├── skills-data/          # Raw skill data, scraped content, skill metadata
├── evaluations/          # Evaluation framework, scorecards, test results
│   ├── framework-v2-final.md          # ⭐ FINAL research-validated framework
│   ├── metrics-validation.md          # User research analysis
│   ├── testing-methodology.md         # Practical testing guide
│   └── user-research-notes.md         # Raw research findings
├── website/              # Website code, designs, deployment configs
├── branding/             # Brand guidelines, visual assets, messaging
├── gtm/                  # Go-to-market strategy, content, campaigns
├── operations/           # SOPs, workflows, business operations
└── README.md            # This file - project status and navigation
```

---

## 🎯 Current Status

**Last Updated:** Dec 23, 2025 - Session 2

### ✅ Completed
- Repository structure established with organized folders
- Project vision documented
- Knowledge base protocol defined
- **Evaluation framework v1.0 designed** (5 dimensions: Clarity, Activation Reliability, Performance, Hallucination Risk, Use Case Fit)
- **Deep user research conducted** (Reddit, GitHub, blogs, competitive analysis)
- **Evaluation framework v2.0 finalized** (6 research-validated metrics)
- **Testing methodology designed** (3-day implementation plan)
- GitHub authentication configured and working

### 🚧 In Progress
- Ready to build automation scripts for Phase 1 metrics
- Ready to pull 20-50 skills from Anthropic's GitHub

### 📋 Next Steps
1. Build automation scripts (Description Efficiency, Maintenance Status, Token Efficiency)
2. Pull 20-50 skills from Anthropic's public GitHub repository
3. Run Phase 1 automated evaluations (Day 1)
4. Conduct Phase 2 manual testing on top 10-15 skills (Day 2)
5. Generate final scorecards (Day 3)
6. Design and build MVP website (discovery interface + skill cards)
7. Deploy and launch

---

## 🔬 Research Insights (NEW)

### Key Findings:
- **#1 User Complaint:** Skills won't activate (Activation Rate is critical)
- **#2 User Complaint:** Token waste and cost inefficiency
- **#3 User Complaint:** Unpredictable/inconsistent outputs
- **Hidden Issue:** Context limit (15k chars) silently breaks skills - users have NO idea
- **Competitive Gap:** SkillsMP (31,767 skills) just aggregates - NO ONE tests skills
- **Our Moat:** We will be the FIRST to actually test and validate skills

### Final Metrics (6):
1. **Activation Rate** (0-10) - Does it trigger when needed?
2. **Task Completion Rate** (0-10) - Does it work reliably?
3. **Output Consistency** (0-10) - Same input = same output?
4. **Token Efficiency** (0-10) - Cost-effective?
5. **Description Efficiency** (0-10) - Fits in context budget?
6. **Maintenance Status** (0-10) - Actively maintained?

---

## 🧠 Knowledge Base Protocol

### Session Start
1. Read this README for latest status
2. Navigate to relevant project folder for your task
3. Review existing files before creating new ones

### During Session
- Create and update files in appropriate folders
- Build on existing context - no reinventing
- Keep files organized and well-named

### Session End
1. Update this README with:
   - **Completed:** What you accomplished
   - **In-Progress:** Current status
   - **Next Steps:** What happens next
2. Commit and push all changes with clear message

---

## 🚀 Quick Links

- **Vision Doc:** `/home/ubuntu/projects/agent-lab-6ac8daa1/Agent Skills Platform V.0001.md`
- **Evaluation Framework v2.0:** `/evaluations/framework-v2-final.md` ⭐
- **Testing Methodology:** `/evaluations/testing-methodology.md`
- **User Research:** `/evaluations/user-research-notes.md`
- **Anthropic Skills:** https://github.com/anthropics/skills
- **Claude Skills Docs:** https://code.claude.com/docs/en/skills
- **Competitor (SkillsMP):** https://skillsmp.com/

---

## 📊 Key Metrics & Goals

- **Target:** 20-50 evaluated skills at launch
- **Timeline:** 3 days to MVP
- **Quality Bar:** Non-technical users can understand and use every skill
- **First Mover Advantage:** Speed is critical
- **Competitive Moat:** Testing > Aggregating

---

*This is our shared brain. Any agent can pick up where another left off.*
