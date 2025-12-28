#!/usr/bin/env python3.11
"""
Check evaluation progress by reading Google Sheets
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_ID = '12FTvurGOZ7Pi3Okcdch40QO1woyAdVzRJe--Aj-B9pY'

def main():
    # Connect to Google Sheets
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/home/ubuntu/agent-lab/credentials.json',
        scope
    )
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    
    # Read API Responses
    responses_worksheet = spreadsheet.worksheet('API Responses')
    responses = responses_worksheet.get_all_values()
    
    # Read Test Prompts
    prompts_worksheet = spreadsheet.worksheet('Test Prompts')
    prompts = prompts_worksheet.get_all_values()
    
    # Calculate stats
    total_prompts = len(prompts) - 1  # Exclude header
    total_responses = len(responses) - 1  # Exclude header
    
    # Calculate expected total tests (activation 3x, others 1x)
    expected_tests = 0
    for row in prompts[1:]:
        prompt_type = row[3].lower() if len(row) > 3 else ''
        if 'activation' in prompt_type:
            expected_tests += 3
        else:
            expected_tests += 1
    
    # Get unique prompts tested
    tested_prompts = set()
    for row in responses[1:]:
        if len(row) > 1:
            prompt_id = row[1]  # Column B: Prompt ID
            tested_prompts.add(prompt_id)
    
    # Calculate progress
    progress_pct = (total_responses / expected_tests * 100) if expected_tests > 0 else 0
    
    print("=" * 60)
    print("EVALUATION PROGRESS")
    print("=" * 60)
    print(f"Total prompts: {total_prompts}")
    print(f"Unique prompts tested: {len(tested_prompts)}")
    print(f"Total test runs completed: {total_responses}/{expected_tests} ({progress_pct:.1f}%)")
    print()
    
    if total_responses > 0:
        print("Last 5 tests:")
        for row in responses[-5:]:
            if len(row) > 5:
                response_id = row[0]
                prompt_id = row[1]
                skill_activated = row[4]
                correct_skill = row[5]
                print(f"  {response_id}: {prompt_id} | Activated: {skill_activated} | Correct: {correct_skill}")
    
    print("=" * 60)

if __name__ == '__main__':
    main()
