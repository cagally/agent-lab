# Google Sheets Setup Instructions

## Quick Start

I've created 7 CSV files that you can import into Google Sheets to set up the complete evaluation structure.

---

## Step 1: Create New Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Click **"Blank"** to create a new spreadsheet
3. Name it: **"Agent Skills Evaluation - MVP"**

---

## Step 2: Import CSV Files

For each of the 7 CSV files, do the following:

### **Import Process:**

1. **Click the "+" button** at the bottom to create a new tab
2. **File → Import**
3. **Upload** the CSV file
4. **Import location:** Select "Replace current sheet"
5. **Separator type:** Comma
6. **Convert text to numbers:** Yes
7. Click **"Import data"**
8. **Rename the tab** to match the CSV filename (without .csv)

### **Files to Import (in order):**

1. `01-skills-master-list.csv` → Rename tab to **"Skills Master List"**
2. `02-test-prompts.csv` → Rename tab to **"Test Prompts"**
3. `03-api-responses.csv` → Rename tab to **"API Responses"**
4. `04-automated-scores.csv` → Rename tab to **"Automated Scores"**
5. `05-manual-evaluations.csv` → Rename tab to **"Manual Evaluations"**
6. `06-final-scorecards.csv` → Rename tab to **"Final Scorecards"**
7. `07-dashboard.csv` → Rename tab to **"Dashboard"**

**Delete the original "Sheet1"** that was created by default.

---

## Step 3: Set Up Data Validation (Dropdowns)

### **Tab 1: Skills Master List**

**Column E (Category):**
- Select column E (click the column header)
- Data → Data validation
- Criteria: List of items
- Items: `Development, Documentation, Design, Integration, Analysis`
- Show dropdown list in cell: ✓
- Click "Save"

**Column H (Status):**
- Select column H
- Data → Data validation
- Items: `Not Started, In Progress, Complete`

### **Tab 2: Test Prompts**

**Column C (Prompt Type):**
- Select column C
- Data → Data validation
- Items: `Activation-Explicit, Activation-Implicit, Adversarial, Edge Case`

**Column H (Status):**
- Select column H
- Data → Data validation
- Items: `Not Tested, In Progress, Complete`

### **Tab 4: Automated Scores**

**Column C (Dimension):**
- Select column C
- Data → Data validation
- Items: `Token Efficiency, Security Audit, Description Efficiency, Activation Rate, Output Consistency, Multi-Skill Compatibility, Failure Mode Resistance`

### **Tab 5: Manual Evaluations**

**Column C (Dimension):**
- Select column C
- Data → Data validation
- Items: `Task Completion, Grounding & Faithfulness`

**Column K (Status):**
- Select column K
- Data → Data validation
- Items: `Draft, Final`

### **Tab 6: Final Scorecards**

**Column O (Recommendation):**
- Select column O
- Data → Data validation
- Items: `Highly Recommended, Recommended, Use with Caution, Not Recommended`

---

## Step 4: Set Up Conditional Formatting

### **Tab 4: Automated Scores - Column D (Score)**

1. Select column D (from D2 downward)
2. Format → Conditional formatting
3. Add 3 rules:

**Rule 1 (Green for 9-10):**
- Format cells if: Greater than or equal to
- Value: 9
- Formatting style: Green background

**Rule 2 (Yellow for 7-8.9):**
- Format cells if: Between
- Value: 7 and 8.99
- Formatting style: Yellow background

**Rule 3 (Red for <7):**
- Format cells if: Less than
- Value: 7
- Formatting style: Red background

### **Tab 5: Manual Evaluations - Column D (Score)**

Repeat the same 3 rules for column D in this tab.

### **Tab 6: Final Scorecards - Columns C-K (All Score Columns)**

Repeat the same 3 rules for columns C through K (all the score columns).

---

## Step 5: Set Up Formulas (Tab 6: Final Scorecards)

The Final Scorecards tab should pull data from Automated Scores and Manual Evaluations.

### **For Each Score Column (C-K):**

**Example for Cell C2 (Token Efficiency):**
```
=IFERROR(VLOOKUP($A2,'Automated Scores'!$B:$D,3,FALSE),"")
```

This looks up the Skill ID in column A, finds it in the Automated Scores tab, and returns the score.

**Apply similar formulas for:**
- C2: Token Efficiency
- D2: Security Audit
- E2: Description Efficiency
- F2: Activation Rate
- G2: Output Consistency
- H2: Multi-Skill Compatibility
- I2: Failure Mode Resistance
- J2: Task Completion (from Manual Evaluations tab)
- K2: Grounding & Faithfulness (from Manual Evaluations tab)

**Adjust the VLOOKUP column index** for each dimension.

### **Total Score (Column L):**
```
=SUM(C2:K2)
```

### **Percentage (Column N):**
```
=IF(M2>0,L2/M2*100,"")
```

### **Rating (Column O):**
```
=IF(N2>=90,"A+",IF(N2>=85,"A",IF(N2>=80,"B+",IF(N2>=75,"B",IF(N2>=70,"C+",IF(N2>=60,"C","D"))))))
```

**Copy these formulas down** for all 12 skills.

---

## Step 6: Set Up Dashboard (Tab 7)

### **Summary Stats:**

**Cell B1 (Total Skills Evaluated):**
```
=COUNTIF('Skills Master List'!H:H,"Complete")
```

**Cell B2 (Average Score):**
```
=AVERAGE('Final Scorecards'!L:L)
```

**Cell B3 (Highest Rated Skill):**
```
=INDEX('Final Scorecards'!B:B,MATCH(MAX('Final Scorecards'!L:L),'Final Scorecards'!L:L,0))&" ("&MAX('Final Scorecards'!L:L)&")"
```

### **Dimension Averages (B10-B18):**

For each dimension, calculate the average from the Automated Scores tab:

**Example for B10 (Token Efficiency):**
```
=AVERAGEIF('Automated Scores'!C:C,"Token Efficiency",'Automated Scores'!D:D)
```

Repeat for all 9 dimensions.

---

## Step 7: Create Charts (Optional)

### **Dashboard - Dimension Averages Bar Chart:**

1. Select cells A10:B18 (dimension names and averages)
2. Insert → Chart
3. Chart type: Bar chart
4. Customize: Add title "Average Scores by Dimension"

### **Dashboard - Skills Ranking:**

1. Go to Final Scorecards tab
2. Select columns A, B, L (Skill ID, Name, Total Score)
3. Insert → Chart
4. Chart type: Bar chart (horizontal)
5. Sort by Total Score descending

---

## Step 8: Share & Collaborate

1. Click **"Share"** button (top right)
2. Add collaborators or get shareable link
3. Set permissions: **"Editor"** for collaboration
4. Copy the link and share it

---

## Next Steps

Once the sheet is set up:

1. **Share the link** with me
2. **I'll build Python scripts** to automatically populate:
   - Test Prompts (all 180)
   - API Responses (from automated testing)
   - Automated Scores (from evaluation scripts)
3. **You'll manually fill:**
   - Manual Evaluations (Task Completion, Grounding & Faithfulness)
   - Comments and notes

---

## Files Location

All CSV files are in:
```
agent-lab/evaluations/google-sheets-templates/
```

Or download the zip:
```
agent-lab/evaluations/google-sheets-templates.zip
```

---

## Need Help?

If you run into issues:
1. Check that all tabs are named correctly
2. Verify formulas reference the correct tab names
3. Make sure data validation is set up for dropdowns
4. Test conditional formatting with sample scores

Let me know if you need any adjustments!
