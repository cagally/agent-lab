#!/usr/bin/env python3
"""
Run test prompts through Anthropic API and write responses to Google Sheets.

This script:
1. Reads prompts from "Test Prompts" tab
2. Runs each prompt through Anthropic API (3 times per prompt)
3. Writes responses to "API Responses" tab
4. Tracks progress and handles errors
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
RATE_LIMIT_DELAY = 1.5  # seconds between API calls


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


def run_prompt_through_api(client, prompt_text, skill_id):
    """Run a single prompt through Anthropic API."""
    
    try:
        # Call API
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": prompt_text
            }]
        )
        
        # Extract response data
        response_text = response.content[0].text if response.content else ""
        
        # Check if skill activated (simple heuristic - look for skill-related keywords)
        skill_activated = False
        # This is a placeholder - in reality, we'd need to check the actual API response
        # for skill activation signals
        
        # Extract tool calls if any
        tool_calls = []
        # Anthropic API doesn't expose tool calls in the same way
        # We'll leave this empty for now
        
        return {
            'success': True,
            'response_text': response_text,
            'skill_activated': skill_activated,
            'tool_calls': json.dumps(tool_calls),
            'token_count': response.usage.output_tokens if hasattr(response, 'usage') else 0,
            'model': MODEL,
            'error': None
        }
        
    except Exception as e:
        return {
            'success': False,
            'response_text': '',
            'skill_activated': False,
            'tool_calls': '[]',
            'token_count': 0,
            'model': MODEL,
            'error': str(e)
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
        response_data['response_text'],
        response_data['tool_calls'],
        response_data['token_count'],
        '',  # File IDs (placeholder)
        '',  # Container ID (placeholder)
        response_data['error'] or '',
        ''   # Notes (empty)
    ]
    
    # Append row
    worksheet.append_row(row, value_input_option='USER_ENTERED')


def run_tests(spreadsheet, anthropic_client, limit=None, runs_per_prompt=3):
    """Run all tests and write responses to sheet."""
    
    print("\n" + "=" * 80)
    print("STARTING API TESTS")
    print("=" * 80)
    
    # Read prompts
    prompts = read_test_prompts(spreadsheet, limit=limit)
    
    # Get API Responses worksheet
    responses_worksheet = spreadsheet.worksheet(API_RESPONSES_TAB)
    
    # Check if header exists
    existing_data = responses_worksheet.get_all_values()
    if not existing_data or existing_data[0][0] != 'Response ID':
        # Write header
        header = [
            'Response ID',
            'Prompt ID',
            'Skill ID',
            'Run Number',
            'Timestamp',
            'Model',
            'Skill Activated',
            'Response Text',
            'Tool Calls',
            'Token Count',
            'File IDs',
            'Container ID',
            'Error',
            'Notes'
        ]
        responses_worksheet.clear()
        responses_worksheet.append_row(header, value_input_option='USER_ENTERED')
        print("✓ Created header row in API Responses tab")
    
    # Run tests
    total_tests = len(prompts) * runs_per_prompt
    completed = 0
    errors = 0
    
    print(f"\nRunning {total_tests} tests ({len(prompts)} prompts × {runs_per_prompt} runs)...")
    print()
    
    for prompt in prompts:
        prompt_id = prompt['Prompt ID']
        skill_id = prompt['Skill ID']
        prompt_text = prompt['Prompt Text']
        
        print(f"[{completed + 1}-{completed + runs_per_prompt}/{total_tests}] Testing: {prompt_id}")
        print(f"  Prompt: {prompt_text[:80]}...")
        
        for run_num in range(1, runs_per_prompt + 1):
            # Run through API
            result = run_prompt_through_api(anthropic_client, prompt_text, skill_id)
            
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
                'response_text': result['response_text'],
                'tool_calls': result['tool_calls'],
                'token_count': result['token_count'],
                'error': result['error']
            }
            
            # Write to sheet
            try:
                write_response_to_sheet(responses_worksheet, response_data)
                completed += 1
                
                if result['success']:
                    print(f"  ✓ Run {run_num}: {result['token_count']} tokens")
                else:
                    print(f"  ✗ Run {run_num}: ERROR - {result['error']}")
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
    # For testing, limit to 5 prompts
    run_tests(spreadsheet, anthropic_client, limit=5, runs_per_prompt=3)


if __name__ == '__main__':
    main()
