# Anthropic API Skills Support - Research Findings

**Date:** Dec 26, 2025  
**Source:** https://platform.claude.com/docs/en/build-with-claude/skills-guide

---

## ✅ YES - Skills Work with Anthropic API!

**Key Finding:** Agent Skills can be used directly with the Anthropic Messages API through the code execution tool.

---

## How It Works

### **Integration Method:**
Skills integrate with the Messages API through the **`container` parameter** and require the **code execution tool** to be enabled.

### **Two Types of Skills:**

| Type | Value | Skill IDs | Version Format | Management |
|------|-------|-----------|----------------|------------|
| **Anthropic Skills** | `anthropic` | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Date-based: `20251013` or `latest` | Pre-built by Anthropic |
| **Custom Skills** | `custom` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv` | Epoch timestamp or `latest` | Upload via Skills API |

---

## Code Example

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",  # or "custom"
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a presentation about renewable energy"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

---

## Requirements

1. **Anthropic API key** from Console
2. **Beta headers:**
   - `code-execution-2025-08-25` (required for Skills)
   - `skills-2025-10-02` (enables Skills API)
   - `files-api-2025-04-14` (for file upload/download)
3. **Code execution tool** enabled in requests

---

## Key Features

### **1. Custom Skills Upload**
- Upload your own skills via Skills API
- Private to your workspace
- Manage versions programmatically

### **2. Multi-Turn Conversations**
- Reuse same container across messages
- Container persists state between turns

### **3. File Generation**
- Skills can create files (Excel, PowerPoint, PDF, Word)
- Response includes `file_id` for each created file
- Download via Files API

### **4. Long-Running Operations**
- Skills support `pause_turn` for operations requiring multiple turns
- Handle with retry logic

---

## What This Means for Our Evaluation

### **✅ We CAN Use Anthropic API for Testing!**

**Advantages:**
1. **Programmatic access** - Automate everything
2. **Response metadata** - See exactly what happened
3. **Tool use logging** - Track which tools were called
4. **File handling** - Automated file download
5. **Container reuse** - Multi-turn testing

**Limitations:**
1. **Not exactly Claude Code** - Different environment
2. **Requires code execution tool** - Skills need this enabled
3. **Beta features** - Requires beta headers

---

## Impact on Our Automation Plan

### **What We Can Now Automate:**

1. **Activation Rate** ✅
   - Make API calls with skills
   - Check if skill was invoked in response
   - Parse tool use metadata

2. **Output Consistency** ✅
   - Run same prompt 3x via API
   - Get structured responses
   - Calculate semantic similarity

3. **Tool Call Correctness** ✅
   - API responses include tool use metadata
   - See which tools were called
   - Verify parameters

4. **Task Completion** ⚠️
   - Can automate the execution
   - Still need human judgment for "did it work?"

---

## Recommendation

**Use Anthropic API for automated testing with a caveat:**

- ✅ **Test via API** for automation and tracing
- ⚠️ **Note the limitation** - "Tested via Anthropic API, not Claude Code"
- 🔄 **Spot-check in Claude Code** - Validate a few skills manually to ensure parity

This gives us the best of both worlds:
- **Speed:** Automate 90% of testing
- **Accuracy:** Validate with real Claude Code when needed
- **Tracing:** Full visibility into skill activation and tool calls

---

## Next Steps

1. **Build API-based automation scripts:**
   - `eval-activation-rate-api.py` - Test skill activation via API
   - `eval-output-consistency-api.py` - Run 3x and compare
   - `eval-tool-calls-api.py` - Analyze tool use metadata

2. **Upload our downloaded skills as custom skills** (if needed)

3. **Run automated evaluations** on all 12 skills

4. **Spot-check 2-3 skills in Claude Code** to validate parity
