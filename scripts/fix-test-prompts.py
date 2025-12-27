#!/usr/bin/env python3
"""
Fix test prompts CSV format and clean prompts with code blocks.

Changes:
1. Add Prompt ID column (format: {skill-id}-{type-abbrev}-{number})
2. Add Run Count column (always 3)
3. Add Created Date column (today's date)
4. Add Status column (always "Not Tested")
5. Keep Category column
6. Fix Prompt Type capitalization
7. Clean prompts that contain code blocks or excessive detail
"""

import csv
import re
from datetime import date

INPUT_FILE = '/home/ubuntu/agent-lab/evaluations/test-prompts-generated.csv'
OUTPUT_FILE = '/home/ubuntu/agent-lab/evaluations/test-prompts-final.csv'

# Prompt type mappings
TYPE_MAPPING = {
    'activation-explicit': 'Activation-Explicit',
    'activation-implicit': 'Activation-Implicit',
    'edge-case': 'Edge Case',
    'adversarial-confusion': 'Adversarial',
    'adversarial-impossible': 'Adversarial'
}

# Type abbreviations for Prompt ID
TYPE_ABBREV = {
    'activation-explicit': 'ae',
    'activation-implicit': 'ai',
    'edge-case': 'ec',
    'adversarial-confusion': 'adv',
    'adversarial-impossible': 'adv'
}


def clean_prompt(prompt_text, prompt_type):
    """Clean prompts that contain code blocks or excessive detail."""
    
    # Check if prompt contains code blocks
    has_code_block = '```' in prompt_text
    
    if not has_code_block:
        # Already clean, return as-is
        return prompt_text
    
    # Extract the main request before code block
    parts = prompt_text.split('```')
    main_request = parts[0].strip()
    
    # Clean up the main request
    # Remove trailing colons and extra whitespace
    main_request = re.sub(r':\s*$', '', main_request)
    main_request = re.sub(r'\s+', ' ', main_request)
    
    # If main request is substantial (>50 chars), keep it
    if len(main_request) > 50:
        return main_request
    
    # Otherwise, create a cleaned version based on the content
    # Look for key patterns in the original text
    lower_text = prompt_text.lower()
    
    if 'nested' in lower_text and 'dispatch' in lower_text:
        return "I need to convert some ATen kernel code to AT_DISPATCH_V2 but I have nested dispatch macros and complex template types. Can you help me handle this edge case?"
    elif 'preserve' in lower_text and 'original' in lower_text and 'macro' in lower_text:
        return "I need to convert AT_DISPATCH macros to v2 format but also preserve the exact original macro names for legacy parsing. Can you help with this?"
    elif 'both' in lower_text and 'before' in lower_text and 'after' in lower_text:
        return "I need to set up a hookify rule that triggers both before and after the same event simultaneously. Can you help me configure this?"
    elif 'simultaneously' in lower_text and 'stdio' in lower_text:
        return "I need to integrate an MCP server using stdio connection but also need it to work with network sockets simultaneously. Can you help configure this?"
    else:
        # Fallback: use main request if it exists
        if len(main_request) > 20:
            return main_request
        else:
            # Generic fallback
            return "I need help with a complex edge case scenario. Can you assist?"


def generate_prompt_id(skill_id, prompt_type, prompt_number):
    """Generate Prompt ID in format: {skill-id}-{type-abbrev}-{number}"""
    abbrev = TYPE_ABBREV.get(prompt_type, 'unk')
    return f"{skill_id}-{abbrev}-{prompt_number:02d}"


def fix_csv():
    """Fix CSV format and clean prompts."""
    
    print("=" * 80)
    print("FIXING TEST PROMPTS CSV")
    print("=" * 80)
    print(f"Input: {INPUT_FILE}")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 80)
    
    today = date.today().strftime('%Y-%m-%d')
    
    # Read input CSV
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    print(f"Read {len(rows)} prompts\n")
    
    # Process and fix rows
    fixed_rows = []
    cleaned_count = 0
    
    for row in rows:
        skill_id = row['skill_id']
        prompt_type = row['prompt_type']
        prompt_number = int(row['prompt_number'])
        prompt_text = row['prompt_text']
        expected_behavior = row['expected_behavior']
        category = row['category']
        
        # Clean prompt if needed
        original_text = prompt_text
        cleaned_text = clean_prompt(prompt_text, prompt_type)
        
        if cleaned_text != original_text:
            cleaned_count += 1
            print(f"\n✓ Cleaned: {skill_id}-{prompt_type}-{prompt_number}")
            print(f"  Before: {original_text[:100]}...")
            print(f"  After: {cleaned_text[:100]}...")
        
        # Create fixed row
        fixed_row = {
            'Prompt ID': generate_prompt_id(skill_id, prompt_type, prompt_number),
            'Skill ID': skill_id,
            'Prompt Type': TYPE_MAPPING.get(prompt_type, prompt_type),
            'Prompt Text': cleaned_text,
            'Expected Behavior': expected_behavior,
            'Category': category,
            'Run Count': 3,
            'Created Date': today,
            'Status': 'Not Tested'
        }
        
        fixed_rows.append(fixed_row)
    
    # Write output CSV
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = [
            'Prompt ID',
            'Skill ID',
            'Prompt Type',
            'Prompt Text',
            'Expected Behavior',
            'Category',
            'Run Count',
            'Created Date',
            'Status'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fixed_rows)
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total prompts: {len(fixed_rows)}")
    print(f"Cleaned prompts: {cleaned_count}")
    print(f"Output file: {OUTPUT_FILE}")
    print("=" * 80)


if __name__ == '__main__':
    fix_csv()
