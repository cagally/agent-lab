# Anthropic Skills Repository - Available Skills

**Date:** Dec 25, 2025  
**Source:** https://github.com/anthropics/skills  
**Total Skills:** 16

---

## Skills List

### Creative & Design Skills

1. **algorithmic-art** - Algorithmic art generation
2. **canvas-design** - Canvas design capabilities
3. **frontend-design** - Frontend design and development
4. **slack-gif-creator** - Create GIFs for Slack
5. **theme-factory** - Theme creation and customization

### Document Skills (Source-Available, Production-Ready)

6. **docx** - Word document creation and editing
7. **pdf** - PDF creation and manipulation
8. **pptx** - PowerPoint presentation creation
9. **xlsx** - Excel spreadsheet creation and editing

### Enterprise & Communication Skills

10. **brand-guidelines** - Apply brand guidelines to content
11. **doc-coauthoring** - Collaborative document creation
12. **internal-comms** - Internal communications workflows

### Development & Technical Skills

13. **mcp-builder** - MCP (Model Context Protocol) server generation
14. **skill-creator** - Create new skills
15. **web-artifacts-builder** - Build web artifacts
16. **webapp-testing** - Test web applications

---

## Skills Categories

### High Priority for Testing (Popular/Useful)
- **docx** - Most commonly used, production-ready
- **pdf** - High demand, production-ready
- **xlsx** - Data analysis, production-ready
- **pptx** - Presentations, production-ready
- **webapp-testing** - Developer tool
- **mcp-builder** - Technical, emerging use case
- **skill-creator** - Meta-skill, useful for platform

### Medium Priority
- **brand-guidelines** - Enterprise use case
- **frontend-design** - Developer tool
- **doc-coauthoring** - Collaboration tool
- **internal-comms** - Enterprise communications

### Lower Priority (Niche)
- **algorithmic-art** - Creative/niche
- **canvas-design** - Creative/niche
- **slack-gif-creator** - Very specific use case
- **theme-factory** - Creative/niche
- **web-artifacts-builder** - Overlaps with other skills

---

## Initial Selection for MVP (20 Skills Target)

Since we only have 16 skills in Anthropic's repo, we should:

1. **Test ALL 16 skills** - This gives us comprehensive coverage
2. **Look for additional skills** from:
   - Community contributions
   - Partner skills (e.g., Notion)
   - Other skill repositories

---

## Next Steps

1. Clone the entire skills repository
2. Set up automated analysis for all 16 skills
3. Prioritize manual testing based on:
   - Production readiness (docx, pdf, pptx, xlsx = highest priority)
   - Popularity/demand (webapp-testing, mcp-builder)
   - Unique value proposition (skill-creator)

---

## Repository Structure

```
anthropics/skills/
├── skills/
│   ├── algorithmic-art/
│   ├── brand-guidelines/
│   ├── canvas-design/
│   ├── doc-coauthoring/
│   ├── docx/
│   ├── frontend-design/
│   ├── internal-comms/
│   ├── mcp-builder/
│   ├── pdf/
│   ├── pptx/
│   ├── skill-creator/
│   ├── slack-gif-creator/
│   ├── theme-factory/
│   ├── web-artifacts-builder/
│   ├── webapp-testing/
│   └── xlsx/
├── spec/ (Agent Skills specification)
└── template/ (Skill template)
```

---

## Notes

- Document skills (docx, pdf, pptx, xlsx) are **source-available** (not open source)
- These are the actual skills powering Claude's document capabilities
- All other skills are **Apache 2.0 licensed** (open source)
- Skills are actively maintained (last update: Dec 4, 2025)
