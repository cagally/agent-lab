#!/usr/bin/env python3
"""
Upload all 12 skills to Anthropic via Skills API.
"""

import anthropic
from anthropic.lib import files_from_dir
import os
import json

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
SKILLS_DIR = '/home/ubuntu/agent-lab/skills-data/raw-skills'

# Skill directories (renamed to match SKILL.md names)
SKILLS = [
    'at-dispatch-v2',
    'add-uint-support',
    'skill-writer',
    'docstring',
    'skill-creator',
    'skill-installer',
    'frontend-design',
    'hook-development',
    'command-development',
    'agent-identifier',
    'rule-identifier',
    'mcp-integration'
]

def upload_skill(client, skill_dir_name):
    """Upload a single skill to Anthropic."""
    
    skill_dir = f"{SKILLS_DIR}/{skill_dir_name}"
    skill_path = f"{skill_dir}/SKILL.md"
    
    print(f"\nUploading: {skill_dir_name}")
    print(f"  Path: {skill_path}")
    
    try:
        # Upload skill directory via API
        response = client.beta.skills.create(
            display_title=skill_dir_name,
            files=files_from_dir(skill_dir),
            betas=["skills-2025-10-02"]
        )
        
        skill_id = response.id
        print(f"  ✓ Uploaded: {skill_id}")
        
        return {
            'name': skill_dir_name,
            'skill_id': skill_id,
            'success': True
        }
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {
            'name': skill_dir_name,
            'skill_id': None,
            'success': False,
            'error': str(e)
        }


def main():
    """Upload all skills."""
    
    print("=" * 80)
    print("UPLOADING SKILLS TO ANTHROPIC")
    print("=" * 80)
    
    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    results = []
    
    for skill_dir in SKILLS:
        result = upload_skill(client, skill_dir)
        results.append(result)
    
    # Save skill IDs to file
    output_file = '/home/ubuntu/agent-lab/skills-data/skill-ids.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    successful = sum(1 for r in results if r['success'])
    print(f"Uploaded: {successful}/{len(SKILLS)}")
    print(f"Skill IDs saved to: {output_file}")
    print("=" * 80)


if __name__ == '__main__':
    main()
