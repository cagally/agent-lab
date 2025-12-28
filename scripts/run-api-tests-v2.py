#!/usr/bin/env python3
"""
Run test prompts through Anthropic API WITH SKILLS and write responses to Google Sheets.

This script:
1. Reads prompts from "Test Prompts" tab
2. Runs each prompt through Anthropic API with skills enabled (3 times per prompt)
3. Writes responses to "API Responses" tab
4. Tracks skill activation, tool calls, and errors
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import anthropic
import os
import time
import json
from datetime import datetime

# Configuration
SPREADSHEET_ID = '12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY'
CREDENTIALS_FILE = '/home/ubuntu/agent-lab/credentials.json'
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
MODEL = 'claude-sonnet-4-20250514'

# Sheets configuration
TEST_PROMPTS_TAB = 'Test Prompts'
API_RESPONSES_TAB = 'API Responses'

# Rate limiting
RATE_LIMIT_DELAY = 3.0  # seconds between API calls (to avoid 30k tokens/min limit)

# Load skill ID mapping from file
with open('/home/ubuntu/agent-lab/skills-data/skill-ids-map.json', 'r') as f:
    SKILL_ID_MAP = json.load(f)


def connect_to_sheets():
    """Connect to Google Sheets."""
    print("Connecting to Google Sheets...")
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    print(f"✓ Connected to: {spreadsheet.title}")
    return spreadsheet


def read_test_prompts(spreadsheet, limit=None):
    """Read test prompts from the Test Prompts tab."""
    print(f"\nReading prompts from '{TEST_PROMPTS_TAB}' tab...")
    worksheet = spreadsheet.worksheet(TEST_PROMPTS_TAB)
    
    # Get all records
    records = worksheet.get_all_records()
    
    if limit:
        records = records[:limit]
    
    print(f"✓ Read {len(records)} prompts")
    return records


def run_prompt_with_skill(client, prompt_text, expected_skill_id, max_retries=3):
    """Run a prompt with a specific skill enabled."""
    
    import time
    
    for attempt in range(max_retries):
        try:
        import random
        
        # Get the expected skill's API ID
        expected_skill_api_id = SKILL_ID_MAP.get(expected_skill_id, expected_skill_id)
        
        # Get all other skill IDs (excluding expected and duplicates)
        all_skill_ids = list(set(SKILL_ID_MAP.values()))  # Remove duplicates
        other_skill_ids = [sid for sid in all_skill_ids if sid != expected_skill_api_id]
        
        # Select 7 random competitors
        random.seed()  # Ensure randomness across calls
        competitor_ids = random.sample(other_skill_ids, min(7, len(other_skill_ids)))
        
        # Build skill list: expected + 7 competitors (max 8 total)
        all_skills = [{"type": "custom", "skill_id": expected_skill_api_id, "version": "latest"}]
        all_skills.extend([{"type": "custom", "skill_id": sid, "version": "latest"} for sid in competitor_ids])
        
            # Call API with ALL skills enabled (with timeout)
            response = client.beta.messages.create(
                model=MODEL,
                max_tokens=4096,
                timeout=60.0,  # 60 second timeout
                betas=["code-execution-2025-08-25", "skills-2025-10-02"],
                container={
                    "skills": all_skills
                },
                messages=[{
                    "role": "user",
                    "content": prompt_text
                }],
                tools=[{
                    "type": "code_execution_20250825",
                    "name": "code_execution"
                }]
            )
        
        # Extract response data
        response_text = ""
        skill_activated = False
        activated_skill_id = None
        correct_skill_activated = False
        tool_calls = []
        
        for content_block in response.content:
            if hasattr(content_block, 'text'):
                response_text += content_block.text
            
            # Check for tool use (indicates skill activation)
            # Skills use 'server_tool_use' with name 'text_editor_code_execution'
            if content_block.type in ['bash_code_execution_tool_use', 'tool_use', 'server_tool_use']:
                tool_name = getattr(content_block, 'name', 'unknown')
                tool_input = str(getattr(content_block, 'input', ''))
                
                # Skill activated if using text_editor or accessing /skills/ path
                if tool_name == 'text_editor_code_execution' or '/skills/' in tool_input:
                    skill_activated = True
                    
                    # Detect WHICH skill activated by parsing the path
                    for skill_short_id, skill_api_id in SKILL_ID_MAP.items():
                        if f'/skills/{skill_short_id}/' in tool_input:
                            activated_skill_id = skill_short_id
                            if skill_short_id == expected_skill_id:
                                correct_skill_activated = True
                            break
                
                tool_calls.append({
                    'type': content_block.type,
                    'name': tool_name
                })
        
            return {
                'success': True,
                'response_text': response_text,
                'skill_activated': skill_activated,
                'activated_skill_id': activated_skill_id,
                'correct_skill_activated': correct_skill_activated,
                'tool_calls': json.dumps(tool_calls),
                'token_count': response.usage.output_tokens if hasattr(response, 'usage') else 0,
                'response_length': len(response_text),
                'model': MODEL,
                'container_id': response.container.id if hasattr(response, 'container') else '',
                'error': None
            }
            
        except Exception as e:
            error_msg = str(e)
            
            # Check for rate limit
            if "rate_limit" in error_msg.lower() or "429" in error_msg:
                wait_time = (2 ** attempt) * 5  # Exponential backoff: 5s, 10s, 20s
                print(f"    ⚠ Rate limit hit, waiting {wait_time}s before retry {attempt+1}/{max_retries}...")
                time.sleep(wait_time)
                continue
            
            # Check for connection/timeout errors
            if any(x in error_msg.lower() for x in ['connection', 'timeout', 'timed out']):
                wait_time = (2 ** attempt) * 3  # Exponential backoff: 3s, 6s, 12s
                if attempt < max_retries - 1:
                    print(f"    ⚠ Connection error, retrying in {wait_time}s ({attempt+1}/{max_retries})...")
                    time.sleep(wait_time)
                    continue
            
            # If custom type fails, it might be an anthropic skill
            if "skill" in error_msg.lower() and "not found" in error_msg.lower():
            return {
                'success': False,
                'response_text': '',
                'skill_activated': False,
                'activated_skill_id': None,
                'correct_skill_activated': False,
                'tool_calls': '[]',
                'token_count': 0,
                'response_length': 0,
                'model': MODEL,
                'container_id': '',
                    'error': f"Skill not found (may need to be uploaded): {error_msg}"
                }
            
            # Last attempt failed, return error
            if attempt == max_retries - 1:
                return {
            'success': False,
            'response_text': '',
            'skill_activated': False,
            'activated_skill_id': None,
            'correct_skill_activated': False,
            'tool_calls': '[]',
            'token_count': 0,
            'response_length': 0,
            'model': MODEL,
                'container_id': '',
                'error': error_msg
            }
    
    # Should never reach here
    return {
        'success': False,
        'response_text': '',
        'skill_activated': False,
        'activated_skill_id': None,
        'correct_skill_activated': False,
        'tool_calls': '[]',
        'token_count': 0,
        'response_length': 0,
        'model': MODEL,
        'container_id': '',
        'error': 'Max retries exceeded'
    }


def write_response_to_sheet(worksheet, response_data):
    """Write a single response to the API Responses tab."""
    
    # Prepare row data
    row = [
        response_data['response_id'],
        response_data['prompt_id'],
        response_data['skill_id'],
        response_data['run_number'],
        response_data['timestamp'],
        response_data['model'],
        response_data['skill_activated'],
        response_data.get('activated_skill_id', ''),
        response_data.get('correct_skill_activated', False),
        response_data['response_text'],
        response_data.get('response_length', 0),
        response_data['tool_calls'],
        response_data['token_count'],
        '',  # File IDs (placeholder)
        response_data.get('container_id', ''),
        response_data['error'] or '',
        ''   # Notes (empty)
    ]
    
    # Get next empty row
    existing_data = worksheet.get_all_values()
    next_row = len(existing_data) + 1
    
    # Write row starting at column A
    worksheet.update(values=[row], range_name=f'A{next_row}', value_input_option='USER_ENTERED')


def run_tests(spreadsheet, anthropic_client, limit=None, runs_per_prompt=3):
    """Run all tests and write responses to sheet."""
    
    print("\n" + "=" * 80)
    print("STARTING API TESTS WITH SKILLS")
    print("=" * 80)
    
    # Read prompts
    prompts = read_test_prompts(spreadsheet, limit=limit)
    
    # Get API Responses worksheet
    responses_worksheet = spreadsheet.worksheet(API_RESPONSES_TAB)
    
    # Check if header exists
    existing_data = responses_worksheet.get_all_values()
    if not existing_data or len(existing_data) == 0 or (len(existing_data) > 0 and len(existing_data[0]) > 0 and existing_data[0][0] != 'Response ID'):
        # Write header
        header = [
            'Response ID',
            'Prompt ID',
            'Expected Skill ID',
            'Run Number',
            'Timestamp',
            'Model',
            'Skill Activated',
            'Activated Skill ID',
            'Correct Skill',
            'Response Text',
            'Response Length',
            'Tool Calls',
            'Token Count',
            'File IDs',
            'Container ID',
            'Error',
            'Notes'
        ]
        responses_worksheet.clear()
        responses_worksheet.update(values=[header], range_name='A1', value_input_option='USER_ENTERED')
        print("✓ Created header row in API Responses tab")
    
    # Run tests
    total_tests = len(prompts) * runs_per_prompt
    completed = 0
    errors = 0
    skills_activated = 0
    
    print(f"\nRunning {total_tests} tests ({len(prompts)} prompts × {runs_per_prompt} runs)...")
    print()
    
    for prompt in prompts:
        prompt_id = prompt['Prompt ID']
        skill_id = prompt['Skill ID']
        prompt_text = prompt['Prompt Text']
        
        print(f"[{completed + 1}-{completed + runs_per_prompt}/{total_tests}] Testing: {prompt_id}")
        print(f"  Skill: {skill_id}")
        print(f"  Prompt: {prompt_text[:80]}...")
        
        for run_num in range(1, runs_per_prompt + 1):
            # Run through API with skill
            result = run_prompt_with_skill(anthropic_client, prompt_text, skill_id)
            
            # Prepare response data
            response_id = f"resp-{prompt_id}-{run_num}"
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            response_data = {
                'response_id': response_id,
                'prompt_id': prompt_id,
                'skill_id': skill_id,
                'run_number': run_num,
                'timestamp': timestamp,
                'model': result['model'],
                'skill_activated': result['skill_activated'],
                'activated_skill_id': result.get('activated_skill_id', ''),
                'correct_skill_activated': result.get('correct_skill_activated', False),
                'response_text': result['response_text'],
                'response_length': result.get('response_length', 0),
                'tool_calls': result['tool_calls'],
                'token_count': result['token_count'],
                'container_id': result.get('container_id', ''),
                'error': result['error']
            }
            
            # Write to sheet
            try:
                write_response_to_sheet(responses_worksheet, response_data)
                completed += 1
                
                if result['success']:
                    if result['correct_skill_activated']:
                        print(f"  ✓ Run {run_num}: {result['token_count']} tokens - CORRECT SKILL ({result['activated_skill_id']})")
                        skills_activated += 1
                    elif result['skill_activated']:
                        print(f"  ⚠ Run {run_num}: {result['token_count']} tokens - WRONG SKILL ({result['activated_skill_id']} instead of {skill_id})")
                    else:
                        print(f"  ✗ Run {run_num}: {result['token_count']} tokens - NO SKILL ACTIVATION")
                else:
                    print(f"  ✗ Run {run_num}: ERROR - {result['error'][:100]}")
                    errors += 1
                    
            except Exception as e:
                print(f"  ✗ Run {run_num}: Failed to write to sheet - {e}")
                errors += 1
                completed += 1
            
            # Rate limiting
            time.sleep(RATE_LIMIT_DELAY)
        
        print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total tests: {total_tests}")
    print(f"Completed: {completed}")
    print(f"Errors: {errors}")
    print(f"Skills activated: {skills_activated}/{total_tests} ({skills_activated/total_tests*100:.1f}%)")
    print(f"Success rate: {((completed - errors) / total_tests * 100):.1f}%")
    print("=" * 80)


def main():
    """Main entry point."""
    
    # Check API key
    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        return
    
    # Connect to services
    spreadsheet = connect_to_sheets()
    anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Run tests
    # Run ALL 180 prompts
    run_tests(spreadsheet, anthropic_client, limit=None, runs_per_prompt=3)


if __name__ == '__main__':
    main()
