# SkillsMP Skill Detail Page Structure

**Date:** Dec 25, 2025  
**Example Skill:** at-dispatch-v2 (pytorch/pytorch)  
**URL Pattern:** `https://skillsmp.com/skills/[author]-[repo]-[path]-[skill-name]`

---

## Available Data on Skill Detail Page

### 1. Metadata (Right Sidebar - package.json section)

**Key Fields:**
- **Author**: "pytorch"
- **Repository**: "pytorch/pytorch"
- **GitHub Link**: Direct link to repo with "$ gh browse" button
- **Star Count**: 95,362 stars
- **Fork Count**: 26,012 forks (visible in git log)
- **Last Updated**: "November 26, 2025 at 01:04"

### 2. Skill Content (Main Area)

**Full SKILL.md Content:**
- Complete skill description
- Usage instructions
- Code examples
- Step-by-step guides
- All markdown formatting preserved

**This is GOLD** - we get the entire SKILL.md file rendered on the page!

### 3. Download Options

**Available Downloads:**
- `$ download --local` - Download to local machine
- `man` button - View documentation
- `wget skill.zip` - Download complete skill directory including SKILL.md and all related files

### 4. Related Skills Section

**Shows related/similar skills with:**
- Skill name (e.g., "add-uint-support")
- Star count (e.g., ⭐ 95,362)
- Source repository (e.g., "pytorch")
- Import statement format

**Related skills visible:**
1. add-uint-support (95,362 stars)
2. docstring (95,362 stars)
3. memory-safety-patterns (23,399 stars)
4. pennylane (13,157 stars)
5. defense-in-depth-validation (713 stars)

### 5. Breadcrumb Navigation

- Home (~)
- Category (framework-internals)
- Skill name (at-dispatch-v2)

---

## URL Structure Analysis

**Pattern:** `https://skillsmp.com/skills/[slug]`

**Example:**
- URL: `https://skillsmp.com/skills/pytorch-pytorch-claude-skills-at-dispatch-v2-skill-md`
- Breakdown:
  - `pytorch` = GitHub username/org
  - `pytorch` = Repository name
  - `claude-skills` = Path in repo
  - `at-dispatch-v2` = Skill name
  - `skill-md` = File type indicator

---

## What We Can Extract

### From Homepage (List View)
✅ Skill name  
✅ Star count  
✅ Repository (author/repo)  
✅ Brief description  
✅ Link to detail page  

### From Detail Page
✅ Full SKILL.md content  
✅ Complete description and instructions  
✅ Star count (precise number)  
✅ Fork count  
✅ Last updated date  
✅ GitHub repository link  
✅ Related skills  
✅ Download link for skill.zip  

---

## Scraping Strategy Recommendation

### Phase 1: Get Top 100 Skills List
**Method:** Scrape homepage with "stars" sort
- Paginate through first ~8 pages (12 skills per page)
- Extract: skill name, stars, repo, detail page URL
- Store in JSON/CSV

### Phase 2: Get Detailed Skill Data
**Method:** Visit each skill's detail page
- Extract full SKILL.md content
- Extract metadata (stars, forks, last updated)
- Extract GitHub repo URL
- Store complete data

### Phase 3: Download Skill Files
**Method:** Use `skill.zip` download link or GitHub API
- Download actual skill files for Claude Code installation
- Store in organized directory structure
- Prepare for evaluation

---

## Key Observations

1. **No API visible** - Will need to scrape HTML
2. **Clean URL structure** - Predictable and parseable
3. **Complete data available** - Everything we need is on the page
4. **Download functionality** - Can get actual skill files via wget
5. **Related skills** - Could expand our dataset beyond top 100
6. **Pagination** - Need to handle 2,761 pages for full dataset (but top 100 is sufficient for MVP)

---

## Rate Limiting Considerations

- No visible rate limit warnings
- Should implement polite scraping:
  - 1-2 second delay between requests
  - User-agent header
  - Respect robots.txt
- Consider caching results for future use
- Build for repeatability (will need to re-scrape weekly/monthly)

---

## Next Steps

1. ✅ Understand page structure
2. 🔲 Build scraper for homepage (top 100)
3. 🔲 Build scraper for detail pages
4. 🔲 Download skill files
5. 🔲 Install in Claude Code
6. 🔲 Begin evaluation
