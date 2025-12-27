# Agent Skills Evaluation - Google Sheets Schema

**Date:** Dec 26, 2025  
**Purpose:** Data structure for storing and analyzing skills evaluation data

---

## Sheet Structure

### **Tab 1: Skills Master List**

**Purpose:** Central registry of all skills being evaluated

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Skill ID | Text | Unique identifier | `pytorch-skill-writer` |
| Skill Name | Text | Human-readable name | `PyTorch Skill Writer` |
| Repository | URL | GitHub repo | `https://github.com/pytorch/pytorch` |
| Stars | Number | SkillsMP stars | `95362` |
| Category | Dropdown | Skill category | `Development`, `Documentation`, `Design` |
| Source | Dropdown | Skill source | `PyTorch`, `Anthropic`, `OpenAI` |
| Last Updated | Date | Last modification date | `2025-11-26` |
| Status | Dropdown | Evaluation status | `Not Started`, `In Progress`, `Complete` |
| SKILL.md Path | Text | Local file path | `skills-data/raw-skills/pytorch-skill-writer/SKILL.md` |
| Notes | Long Text | General notes | |

**Total Rows:** 12 skills

---

### **Tab 2: Test Prompts**

**Purpose:** All test prompts for activation and failure mode testing

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Prompt ID | Text | Unique identifier | `pytorch-skill-writer-act-01` |
| Skill ID | Dropdown (linked to Tab 1) | Which skill to test | `pytorch-skill-writer` |
| Prompt Type | Dropdown | Type of test | `Activation-Explicit`, `Activation-Implicit`, `Adversarial`, `Edge Case` |
| Prompt Text | Long Text | The actual prompt | `Help me create a new skill for analyzing Python code quality` |
| Expected Behavior | Long Text | What should happen | `Skill should activate and guide user through creation process` |
| Run Count | Number | How many times to run | `3` (for consistency testing) |
| Created Date | Date | When prompt was created | `2025-12-26` |
| Status | Dropdown | Testing status | `Not Tested`, `In Progress`, `Complete` |

**Total Rows:** ~180 prompts (15 per skill × 12 skills)

**Breakdown per skill:**
- 4 Activation-Explicit
- 4 Activation-Implicit
- 2 Edge Cases
- 5 Adversarial

---

### **Tab 3: API Responses**

**Purpose:** Raw outputs from API testing for analysis

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Response ID | Text | Unique identifier | `resp-001` |
| Prompt ID | Dropdown (linked to Tab 2) | Which prompt was run | `pytorch-skill-writer-act-01` |
| Skill ID | Dropdown (linked to Tab 1) | Which skill was tested | `pytorch-skill-writer` |
| Run Number | Number | Which run (1-3) | `1` |
| Timestamp | DateTime | When test was run | `2025-12-26 11:30:45` |
| Model | Text | Which model used | `claude-sonnet-4-5-20250929` |
| Skill Activated | Boolean | Did skill activate? | `TRUE` |
| Response Text | Long Text | Full response | `I'll help you create...` |
| Tool Calls | Long Text (JSON) | Tools used | `[{"type": "glob", "pattern": "*.py"}]` |
| Token Count | Number | Tokens used | `1250` |
| File IDs | Text | Generated file IDs | `file_01abc...` |
| Container ID | Text | API container ID | `container_01xyz...` |
| Error | Text | Any errors | |
| Notes | Long Text | Observations | |

**Total Rows:** ~540 responses (180 prompts × 3 runs)

---

### **Tab 4: Automated Scores**

**Purpose:** Results from automated evaluation scripts

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Score ID | Text | Unique identifier | `score-001` |
| Skill ID | Dropdown (linked to Tab 1) | Which skill | `pytorch-skill-writer` |
| Dimension | Dropdown | Evaluation dimension | `Activation Rate`, `Token Efficiency`, etc. |
| Score | Number (0-10) | Numerical score | `9.5` |
| Raw Data | Long Text (JSON) | Detailed results | `{"attempts": 10, "successes": 9}` |
| Timestamp | DateTime | When evaluated | `2025-12-26 12:00:00` |
| Script Version | Text | Which script version | `v1.0` |
| Notes | Long Text | Additional findings | |

**Dimensions:**
1. Token Efficiency
2. Security Audit
3. Description Efficiency
4. Activation Rate
5. Output Consistency
6. Multi-Skill Compatibility
7. Failure Mode Resistance

**Total Rows:** ~84 scores (7 dimensions × 12 skills)

---

### **Tab 5: Manual Evaluations**

**Purpose:** Manual scoring workspace for human judgment

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Evaluation ID | Text | Unique identifier | `manual-001` |
| Skill ID | Dropdown (linked to Tab 1) | Which skill | `pytorch-skill-writer` |
| Dimension | Dropdown | Evaluation dimension | `Task Completion`, `Grounding & Faithfulness` |
| Score | Number (0-10) | Numerical score | `10` |
| Test Case | Long Text | What was tested | `Created Python code quality skill` |
| Observations | Long Text | Detailed findings | `Skill activated immediately, guided through questionnaire...` |
| Strengths | Long Text | What worked well | `Clear UX, structured output, proper validation` |
| Weaknesses | Long Text | What didn't work | `None observed` |
| Evaluator | Text | Who evaluated | `Oscar` |
| Timestamp | DateTime | When evaluated | `2025-12-26 13:00:00` |
| Status | Dropdown | Evaluation status | `Draft`, `Final` |

**Dimensions:**
1. Task Completion
2. Grounding & Faithfulness

**Total Rows:** ~24 evaluations (2 dimensions × 12 skills)

---

### **Tab 6: Final Scorecards**

**Purpose:** Aggregated results and final ratings

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Skill ID | Dropdown (linked to Tab 1) | Which skill | `pytorch-skill-writer` |
| Skill Name | Formula (lookup) | Display name | `PyTorch Skill Writer` |
| **AUTOMATED SCORES** | | | |
| Token Efficiency | Formula (lookup) | Score 0-10 | `9.0` |
| Security Audit | Formula (lookup) | Score 0-10 | `10.0` |
| Description Efficiency | Formula (lookup) | Score 0-10 | `8.5` |
| Activation Rate | Formula (lookup) | Score 0-10 | `10.0` |
| Output Consistency | Formula (lookup) | Score 0-10 | `9.5` |
| Multi-Skill Compatibility | Formula (lookup) | Score 0-10 | `9.0` |
| Failure Mode Resistance | Formula (lookup) | Score 0-10 | `8.0` |
| **MANUAL SCORES** | | | |
| Task Completion | Formula (lookup) | Score 0-10 | `10.0` |
| Grounding & Faithfulness | Formula (lookup) | Score 0-10 | `9.0` |
| **AGGREGATED** | | | |
| Total Score | Formula (sum) | Sum of all scores | `93.0` |
| Max Score | Number | Maximum possible | `90` |
| Percentage | Formula (%) | Total/Max × 100 | `103%` (if bonus points) |
| Rating | Formula (IF) | Letter grade | `A+`, `A`, `B+`, etc. |
| **QUALITATIVE** | | | |
| Recommendation | Dropdown | Usage recommendation | `Highly Recommended`, `Recommended`, `Use with Caution`, `Not Recommended` |
| Best For | Long Text | Ideal use cases | `Creating new skills, understanding skill structure` |
| Avoid For | Long Text | Poor use cases | `None identified` |
| Strengths | Long Text | Key strengths | `Excellent UX, production-ready, clear guidance` |
| Weaknesses | Long Text | Key weaknesses | `None significant` |
| Alternatives | Text | Similar skills | `openai-skill-creator` |
| Last Updated | Formula (lookup) | When evaluated | `2025-12-26` |
| Status | Formula (lookup) | Evaluation status | `Complete` |

**Total Rows:** 12 skills

---

### **Tab 7: Dashboard**

**Purpose:** Executive summary with charts and key metrics

**Sections:**

1. **Summary Stats**
   - Total Skills Evaluated
   - Average Score
   - Highest Rated Skill
   - Lowest Rated Skill
   - Skills by Rating (A+, A, B+, etc.)

2. **Dimension Averages**
   - Bar chart showing average score per dimension
   - Identifies which dimensions are strongest/weakest across all skills

3. **Skills Ranking**
   - Table sorted by total score
   - Quick view of best → worst

4. **Category Breakdown**
   - Average scores by category (Development, Documentation, Design)
   - Pie chart of skill distribution

5. **Evaluation Progress**
   - How many skills complete vs in progress
   - Progress bar

6. **Top Recommendations**
   - Top 5 skills to use
   - Top 5 skills to avoid

---

## Formulas & Automation

### **Lookups (Tab 6):**
```
=VLOOKUP(A2,'Automated Scores'!A:D,4,FALSE)
```

### **Total Score (Tab 6):**
```
=SUM(C2:K2)
```

### **Rating (Tab 6):**
```
=IF(M2>=90,"A+",IF(M2>=85,"A",IF(M2>=80,"B+",IF(M2>=75,"B",IF(M2>=70,"C+","C")))))
```

### **Dashboard Averages:**
```
=AVERAGE('Final Scorecards'!M:M)
```

---

## Data Validation

### **Dropdowns:**
- **Status:** `Not Started`, `In Progress`, `Complete`
- **Category:** `Development`, `Documentation`, `Design`, `Integration`, `Analysis`
- **Prompt Type:** `Activation-Explicit`, `Activation-Implicit`, `Adversarial`, `Edge Case`
- **Dimension:** All 9 evaluation dimensions
- **Rating:** `A+`, `A`, `B+`, `B`, `C+`, `C`, `D`, `F`
- **Recommendation:** `Highly Recommended`, `Recommended`, `Use with Caution`, `Not Recommended`

### **Conditional Formatting:**
- Scores 9-10: Green
- Scores 7-8.9: Yellow
- Scores <7: Red

---

## Sample Data

Will populate with:
- All 12 skills in Tab 1
- 15 sample prompts for `pytorch-skill-writer` in Tab 2
- 3 sample responses in Tab 3
- Sample scores in Tab 4
- 1 sample manual evaluation in Tab 5
- 1 complete scorecard in Tab 6

---

## Next Steps

1. Create Google Sheet with this structure
2. Populate with sample data
3. Share with user for review
4. Build Python scripts to populate from automation
