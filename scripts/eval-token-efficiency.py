#!/usr/bin/env python3
"""
Token Efficiency Evaluator
Analyzes skill files to measure static and dynamic token costs.
"""

import os
import sys
import yaml
import json
from pathlib import Path

def extract_frontmatter(skill_md_path):
    """Extract YAML frontmatter from SKILL.md file."""
    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None, content
    
    # Find the closing ---
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    frontmatter_text = parts[1]
    body = parts[2]
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, body
    except yaml.YAMLError as e:
        print(f"Error parsing frontmatter: {e}")
        return None, body

def calculate_token_efficiency(skill_path):
    """Calculate token efficiency metrics for a skill."""
    skill_md = Path(skill_path) / "SKILL.md"
    
    if not skill_md.exists():
        return {"error": "SKILL.md not found"}
    
    frontmatter, body = extract_frontmatter(skill_md)
    
    if frontmatter is None:
        return {"error": "No valid frontmatter found"}
    
    # Extract key fields
    name = frontmatter.get('name', 'Unknown')
    description = frontmatter.get('description', '')
    
    # Calculate costs
    description_chars = len(description)
    body_chars = len(body.strip())
    total_chars = description_chars + body_chars
    
    # Estimate tokens (rough approximation: 1 token ≈ 4 chars)
    description_tokens = description_chars // 4
    body_tokens = body_chars // 4
    total_tokens = total_chars // 4
    
    # Score based on efficiency curve
    # Shorter descriptions are better (max 1024 chars)
    if description_chars <= 256:
        description_score = 10
    elif description_chars <= 512:
        description_score = 8
    elif description_chars <= 768:
        description_score = 6
    elif description_chars <= 1024:
        description_score = 4
    else:
        description_score = 2
    
    # Body size matters less but still scored
    if body_chars <= 2000:
        body_score = 10
    elif body_chars <= 5000:
        body_score = 8
    elif body_chars <= 10000:
        body_score = 6
    elif body_chars <= 20000:
        body_score = 4
    else:
        body_score = 2
    
    # Weighted average (description matters more)
    overall_score = (description_score * 0.7) + (body_score * 0.3)
    
    return {
        "name": name,
        "description_chars": description_chars,
        "description_tokens": description_tokens,
        "body_chars": body_chars,
        "body_tokens": body_tokens,
        "total_chars": total_chars,
        "total_tokens": total_tokens,
        "description_score": description_score,
        "body_score": body_score,
        "overall_score": round(overall_score, 1),
        "rating": get_rating(overall_score)
    }

def get_rating(score):
    """Convert numeric score to rating."""
    if score >= 9:
        return "Excellent"
    elif score >= 7:
        return "Good"
    elif score >= 5:
        return "Fair"
    else:
        return "Poor"

def main():
    if len(sys.argv) < 2:
        print("Usage: python eval-token-efficiency.py <path-to-skill-directory>")
        print("Example: python eval-token-efficiency.py ../skills-data/raw-skills/pytorch-skill-writer")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    
    if not os.path.isdir(skill_path):
        print(f"Error: {skill_path} is not a directory")
        sys.exit(1)
    
    result = calculate_token_efficiency(skill_path)
    
    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)
    
    # Print results
    print(f"\n{'='*60}")
    print(f"Token Efficiency Analysis: {result['name']}")
    print(f"{'='*60}\n")
    
    print(f"Description:")
    print(f"  Characters: {result['description_chars']}")
    print(f"  Est. Tokens: {result['description_tokens']}")
    print(f"  Score: {result['description_score']}/10\n")
    
    print(f"Body:")
    print(f"  Characters: {result['body_chars']}")
    print(f"  Est. Tokens: {result['body_tokens']}")
    print(f"  Score: {result['body_score']}/10\n")
    
    print(f"Overall:")
    print(f"  Total Characters: {result['total_chars']}")
    print(f"  Total Est. Tokens: {result['total_tokens']}")
    print(f"  **Final Score: {result['overall_score']}/10**")
    print(f"  Rating: {result['rating']}\n")
    
    # Save to JSON
    output_file = Path(skill_path) / "token-efficiency-result.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
