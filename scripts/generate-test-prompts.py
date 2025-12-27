#!/usr/bin/env python3
"""
Generate high-quality, skill-specific test prompts using Anthropic API.

This script reads each skill's SKILL.md file and uses Claude Sonnet 4.5 to generate
realistic, nuanced test prompts across 5 categories:
1. Activation-Explicit (4 prompts)
2. Activation-Implicit (4 prompts)
3. Edge Cases (2 prompts)
4. Adversarial-Confusion (3 prompts)
5. Adversarial-Impossible (2 prompts)

Total: 15 prompts per skill × 12 skills = 180 prompts
"""

import os
import json
import csv
import time
from pathlib import Path
from anthropic import Anthropic

# Configuration
SKILLS_JSON = "/home/ubuntu/agent-lab/skills-data/skillsmp-top12-skills.json"
RAW_SKILLS_DIR = "/home/ubuntu/agent-lab/skills-data/raw-skills"
OUTPUT_CSV = "/home/ubuntu/agent-lab/evaluations/test-prompts-generated.csv"
MODEL = "claude-sonnet-4-20250514"  # Sonnet 4.5

# Prompt templates (V3 - Improved after iteration testing)
TEMPLATES = {
    "activation-explicit": """Generate a test prompt for the "{skill_name}" skill.

Skill purpose: {skill_description}

Create ONE user message that would make Claude activate this skill.

The message should:
1. Explicitly ask for the skill's core function
2. Use natural language (like a real developer would)
3. Be specific enough to trigger THIS skill, not others
4. Be 1-2 sentences max

Return ONLY the user message.""",

    "activation-implicit": """Generate a test prompt where the user IMPLIES they need the "{skill_name}" skill without directly asking for it.

Skill purpose: {skill_description}

Create ONE user message that describes a problem or goal this skill solves, but DON'T mention:
- The skill name
- Technical jargon about skills or SKILL.md files
- Explicit references to what the skill does

The user should sound like they need help with something this skill does, but they don't know the skill exists.

Return ONLY the user message.""",

    "edge-case": """You are generating a test prompt to find edge cases where the "{skill_name}" skill might fail or behave unexpectedly.

Skill Description: {skill_description}

Output ONLY one prompt that tests an edge case.

The prompt must include ONE of these challenges:
- Ambiguous requirements that could match multiple skills
- Conflicting constraints that are difficult to satisfy
- Unusual input formats or edge cases
- Requirements at the boundary of the skill's capabilities

Do not explain. Return only the test prompt text.""",

    "adversarial-confusion": """Generate a FALSE POSITIVE test for the "{skill_name}" skill.

Skill purpose: {skill_description}

Create ONE user message that:
- Uses similar keywords to this skill's domain
- Sounds like it MIGHT need this skill
- But actually needs something else entirely
- Should NOT activate this skill

Example: If the skill is about "writing code", ask about "writing documentation" instead.

Return ONLY the user message.""",

    "adversarial-impossible": """You are generating an adversarial test prompt with an impossible or contradictory request related to "{skill_name}".

Skill Description: {skill_description}

Output ONLY one prompt that includes an impossible constraint or contradiction.

The prompt must:
- Request something this skill does
- Include a hidden conflict or impossible requirement
- Require the model to notice and gracefully decline or ask for clarification
- Be subtle (not obviously impossible)

Do not explain. Return only the test prompt text."""
}

# Prompt counts per type
PROMPT_COUNTS = {
    "activation-explicit": 4,
    "activation-implicit": 4,
    "edge-case": 2,
    "adversarial-confusion": 3,
    "adversarial-impossible": 2
}


def load_skills():
    """Load skills metadata from JSON."""
    with open(SKILLS_JSON, 'r') as f:
        data = json.load(f)
    return data['skills']


def read_skill_file(skill_dir):
    """Read SKILL.md file and extract description."""
    skill_path = Path(skill_dir) / "SKILL.md"
    
    if not skill_path.exists():
        return None
    
    with open(skill_path, 'r') as f:
        content = f.read()
    
    # Extract frontmatter description
    lines = content.split('\n')
    description = None
    
    for i, line in enumerate(lines):
        if line.startswith('description:'):
            description = line.replace('description:', '').strip()
            break
    
    # If no frontmatter, use first paragraph
    if not description:
        for line in lines:
            if line.strip() and not line.startswith('#') and not line.startswith('---'):
                description = line.strip()
                break
    
    return {
        'description': description or "No description available",
        'full_content': content
    }


def generate_prompt(client, template, skill_name, skill_description, max_retries=3):
    """Generate a single test prompt using Claude API with retry logic."""
    
    # Fill template
    prompt = template.format(
        skill_name=skill_name,
        skill_description=skill_description
    )
    
    # Retry loop
    for attempt in range(max_retries):
        try:
            # Call API
            response = client.messages.create(
                model=MODEL,
                max_tokens=500,
                temperature=1.0,  # Higher temperature for creativity
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract text
            generated_text = response.content[0].text.strip()
            return generated_text
            
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"  ⚠️  Retry {attempt + 1}/{max_retries - 1} after error: {e}")
                time.sleep(1.5)  # Wait before retry
            else:
                raise  # Re-raise on final attempt


def generate_prompts_for_skill(client, skill):
    """Generate all test prompts for a single skill."""
    
    print(f"\n{'='*80}")
    print(f"Processing: {skill['name']}")
    print(f"{'='*80}")
    
    # Read skill file
    skill_dir = os.path.join(RAW_SKILLS_DIR, skill['local_path'].replace('./', '').replace('raw-skills/', ''))
    skill_data = read_skill_file(skill_dir)
    
    if not skill_data:
        print(f"⚠️  Could not read SKILL.md for {skill['name']}")
        return []
    
    skill_description = skill_data['description']
    print(f"Description: {skill_description[:100]}...")
    
    prompts = []
    total_prompts = sum(PROMPT_COUNTS.values())
    current = 0
    
    # Generate prompts for each type
    for prompt_type, count in PROMPT_COUNTS.items():
        template = TEMPLATES[prompt_type]
        
        for i in range(count):
            current += 1
            print(f"\n[{current}/{total_prompts}] Generating {prompt_type} #{i+1}...")
            
            try:
                generated_prompt = generate_prompt(
                    client,
                    template,
                    skill['name'],
                    skill_description
                )
                
                # Store result
                prompts.append({
                    'skill_id': skill['name'],
                    'skill_name': skill['name'],
                    'prompt_type': prompt_type,
                    'prompt_number': i + 1,
                    'prompt_text': generated_prompt,
                    'expected_behavior': get_expected_behavior(prompt_type),
                    'category': get_category(prompt_type)
                })
                
                print(f"✓ Generated: {generated_prompt[:80]}...")
                
                # Rate limiting (1.5 seconds to avoid API limits)
                time.sleep(1.5)
                
            except Exception as e:
                print(f"✗ Error: {e}")
                continue
    
    return prompts


def get_expected_behavior(prompt_type):
    """Get expected behavior for each prompt type."""
    behaviors = {
        "activation-explicit": "Skill should activate",
        "activation-implicit": "Skill should recognize implicit request and activate",
        "edge-case": "Skill should handle edge case gracefully or ask for clarification",
        "adversarial-confusion": "Skill should NOT activate (wrong context)",
        "adversarial-impossible": "Skill should notice contradiction and decline/clarify"
    }
    return behaviors.get(prompt_type, "Unknown")


def get_category(prompt_type):
    """Get category for each prompt type."""
    if "activation" in prompt_type:
        return "Activation"
    elif "edge" in prompt_type:
        return "Edge Case"
    else:
        return "Adversarial"


def save_to_csv(prompts, output_path):
    """Save generated prompts to CSV."""
    
    fieldnames = [
        'skill_id',
        'skill_name',
        'prompt_type',
        'prompt_number',
        'prompt_text',
        'expected_behavior',
        'category'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(prompts)
    
    print(f"\n✓ Saved {len(prompts)} prompts to {output_path}")


def main():
    """Main execution."""
    
    print("="*80)
    print("AGENT SKILLS PLATFORM - TEST PROMPT GENERATOR")
    print("="*80)
    print(f"Model: {MODEL}")
    print(f"Output: {OUTPUT_CSV}")
    print("="*80)
    
    # Initialize Anthropic client
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    # Load skills
    skills = load_skills()
    print(f"\nLoaded {len(skills)} skills")
    
    # Generate prompts for all skills
    all_prompts = []
    
    for skill in skills:
        prompts = generate_prompts_for_skill(client, skill)
        all_prompts.extend(prompts)
    
    # Save results
    save_to_csv(all_prompts, OUTPUT_CSV)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total prompts generated: {len(all_prompts)}")
    print(f"Skills processed: {len(skills)}")
    print(f"Average prompts per skill: {len(all_prompts) / len(skills):.1f}")
    print("="*80)


if __name__ == "__main__":
    main()
