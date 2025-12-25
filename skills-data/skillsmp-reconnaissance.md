# SkillsMP Reconnaissance Report

**Date:** Dec 25, 2025  
**URL:** https://skillsmp.com  
**Total Skills:** 33,132

---

## Key Observations

### 1. Massive Scale
- **33,132 skills** available (up from 31,767 mentioned in our research)
- Growing rapidly (trend chart shows exponential growth in Dec 2025)
- This is THE marketplace for agent skills

### 2. Sorting & Filtering Options

**Available Sorts:**
- ⭐ **Stars** (most popular) - THIS IS WHAT WE WANT
- 🕐 **Recent** (newest first)

**Available Filters:**
- Skills with `marketplace.json` (one-command installation)
- AI semantic search (natural language queries)
- Category filtering (12 categories)

### 3. Homepage Shows Top Skills

Current top skills by stars visible on homepage:
1. `at-dispatch-v2.md` - 95.4k stars (pytorch/pytorch)
2. `add-uint-support.md` - 95.4k stars (pytorch/pytorch)
3. `skill-writer.md` - 95.4k stars (pytorch/pytorch)
4. `docstring.md` - 95.4k stars (pytorch/pytorch)
5. `skill-creator.md` - 54.5k stars (openai/codex)
6. `skill-installer.md` - 54.5k stars (openai/codex)
7. `frontend-design.md` - 47.9k stars (anthropics/claude-code)
8. `hook-development.md` - 47.9k stars (anthropics/claude-code)
9. `command-development.md` - 47.9k stars (anthropics/claude-code)
10. `agent-identifier.md` - 47.9k stars (anthropics/claude-code)

### 4. Pagination
- 2,761 pages total
- 12 skills per page
- Can navigate to specific page numbers
- "Go to page" functionality available

### 5. Categories Available
1. **Tools** - 10,575 skills
2. **Development** - 10,349 skills
3. **Data & AI** - 6,562 skills
4. **Business** - 5,529 skills
5. **DevOps** - 5,132 skills
6. **Testing & Security** - 3,764 skills
7. **Documentation** - 2,803 skills
8. **Content & Media** - 2,752 skills
9. **Lifestyle** - 2,213 skills
10. **Research** - 1,227 skills
11. **Databases** - 763 skills
12. **Blockchain** - 201 skills

---

## Data Available Per Skill (from homepage view)

Each skill card shows:
- **Skill name** (e.g., `skill-creator.md`)
- **Star count** (e.g., 54.5k)
- **Source repository** (e.g., "openai/codex")
- **Export statement** (shows skill name and source)
- **Brief description** (truncated)
- **Numbered badges** (1, 2, 3, 4 - unclear what these mean yet)

---

## Next Steps for Reconnaissance

1. ✅ Understand homepage structure
2. 🔲 Click into individual skill to see full detail page
3. 🔲 Check if there's an API or structured data endpoint
4. 🔲 Understand URL structure for programmatic access
5. 🔲 Determine best scraping approach (pagination vs API)
6. 🔲 Identify rate limits or anti-scraping measures

---

## Initial Strategy Thoughts

**Option A: Scrape Homepage (Top 100)**
- Pros: Fast, gets most popular skills
- Cons: Limited to 12 per page, need to paginate ~8 pages
- Method: Parse HTML, extract skill data

**Option B: Use Search/Filter API**
- Pros: Potentially faster, structured data
- Cons: Need to verify API exists and is accessible
- Method: API calls with sorting by stars

**Option C: Scrape All Pages**
- Pros: Complete dataset
- Cons: 2,761 pages = slow, likely to hit rate limits
- Method: Not recommended for MVP

**Recommendation:** Start with Option A (top 100 via pagination), then explore Option B if API exists.
