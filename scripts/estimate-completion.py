#!/usr/bin/env python3.11
"""
Estimate evaluation completion time
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

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
    
    # Calculate expected total tests
    expected_tests = 0
    for row in prompts[1:]:
        prompt_type = row[3].lower() if len(row) > 3 else ''
        if 'activation' in prompt_type:
            expected_tests += 3
        else:
            expected_tests += 1
    
    total_responses = len(responses) - 1
    
    # Get timestamps from last 10 responses to calculate rate
    recent_responses = responses[-11:-1] if len(responses) > 11 else responses[1:]
    
    if len(recent_responses) >= 2:
        try:
            # Parse timestamps (column index 4: Timestamp)
            first_time = datetime.strptime(recent_responses[0][4], '%Y-%m-%d %H:%M:%S')
            last_time = datetime.strptime(recent_responses[-1][4], '%Y-%m-%d %H:%M:%S')
            
            time_diff = (last_time - first_time).total_seconds()
            tests_completed = len(recent_responses)
            
            # Calculate rate (seconds per test)
            rate = time_diff / tests_completed if tests_completed > 0 else 30
            
            # Estimate remaining time
            remaining_tests = expected_tests - total_responses
            remaining_seconds = remaining_tests * rate
            remaining_time = timedelta(seconds=remaining_seconds)
            
            completion_time = datetime.now() + remaining_time
            
            print(f"Current progress: {total_responses}/{expected_tests} ({total_responses/expected_tests*100:.1f}%)")
            print(f"Average rate: {rate:.1f} seconds per test")
            print(f"Remaining tests: {remaining_tests}")
            print(f"Estimated remaining time: {remaining_time}")
            print(f"Estimated completion: {completion_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"Could not parse timestamps: {e}")
            print(f"Progress: {total_responses}/{expected_tests}")
    else:
        print(f"Not enough data yet. Progress: {total_responses}/{expected_tests}")

if __name__ == '__main__':
    main()
