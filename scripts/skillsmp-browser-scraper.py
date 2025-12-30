#!/usr/bin/env python3
"""
SkillsMP Browser Scraper - Extract top skills using browser automation

This scraper uses the browser to handle JavaScript-rendered content.

Usage:
    python3 skillsmp-browser-scraper.py --pages 10 --output ../skills-data/skillsmp-top-skills.json

Requirements:
    - Browser tools (uses Manus browser automation)

Author: Agent Lab Team
Date: 2025-12-30
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict

# Note: This script is designed to be run within the Manus environment
# which has browser automation capabilities built-in

def parse_star_count(stars_str: str) -> int:
    """Convert star string like '95.4k' to integer"""
    try:
        stars_str = stars_str.lower().replace(',', '')
        if 'k' in stars_str:
            return int(float(stars_str.replace('k', '')) * 1000)
        elif 'm' in stars_str:
            return int(float(stars_str.replace('m', '')) * 1000000)
        else:
            return int(float(stars_str))
    except:
        return 0


def extract_skills_from_page(page_text: str) -> List[Dict]:
    """
    Extract skills from page text
    
    Expected format:
    "at-dispatch-v2.md 95.4k 1 2 3 4 export at-dispatch-v2 from "pytorch/pytorch" Convert PyTorch..."
    """
    skills = []
    
    # Pattern to match skill entries
    # Format: skill-name.md STARS export skill-name from "repo" description
    pattern = r'([a-zA-Z0-9_-]+)\.md\s+([\d.]+k?)\s+.*?export\s+[a-zA-Z0-9_-]+\s+from\s+"([^"]+)"\s+([^\.]+)'
    
    matches = re.finditer(pattern, page_text)
    
    for match in matches:
        skill_name = match.group(1)
        stars_display = match.group(2)
        repository = match.group(3)
        description = match.group(4).strip()
        
        skills.append({
            'name': skill_name,
            'stars': parse_star_count(stars_display),
            'stars_display': stars_display,
            'repository': repository,
            'description': description[:200] + '...' if len(description) > 200 else description,
            'skillsmp_url': f"https://skillsmp.com/skills/{skill_name}",
            'scraped_at': datetime.utcnow().isoformat()
        })
    
    return skills


def main():
    """
    Main function - provides instructions for manual scraping
    
    Since SkillsMP is JavaScript-rendered, this script provides instructions
    for using browser automation within the Manus environment.
    """
    parser = argparse.ArgumentParser(description='Scrape top skills from SkillsMP using browser')
    parser.add_argument('--pages', type=int, default=10, help='Number of pages to scrape')
    parser.add_argument('--output', type=str, default='../skills-data/skillsmp-top-skills.json',
                       help='Output JSON file path')
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("SkillsMP Browser Scraper")
    print("=" * 80)
    print()
    print("⚠️  SkillsMP is a JavaScript-rendered site that requires browser automation.")
    print()
    print("MANUAL SCRAPING INSTRUCTIONS:")
    print()
    print("1. Use browser_navigate to visit: https://skillsmp.com")
    print("2. Use browser_scroll to load more skills (they load dynamically)")
    print("3. Extract skill data from the visible elements")
    print("4. Navigate to next pages using pagination buttons")
    print()
    print("ALTERNATIVE: Use the existing scraper script:")
    print("  scripts/scrape-skillsmp-browser.py")
    print()
    print("=" * 80)
    print()
    print("For now, here are the top skills visible on the first page:")
    print()
    
    # Top skills from manual observation
    top_skills = [
        {"rank": 1, "name": "at-dispatch-v2", "stars": 95400, "stars_display": "95.4k", "repository": "pytorch/pytorch", 
         "description": "Convert PyTorch AT_DISPATCH macros to AT_DISPATCH_V2 in ATen C++ code"},
        {"rank": 2, "name": "add-uint-support", "stars": 95400, "stars_display": "95.4k", "repository": "pytorch/pytorch",
         "description": "Add unsigned integer (uint) type support to PyTorch operators"},
        {"rank": 3, "name": "skill-writer", "stars": 95400, "stars_display": "95.4k", "repository": "pytorch/pytorch",
         "description": "Guide users through creating Agent Skills for Claude Code"},
        {"rank": 4, "name": "docstring", "stars": 95400, "stars_display": "95.4k", "repository": "pytorch/pytorch",
         "description": "Write docstrings for PyTorch functions and methods"},
        {"rank": 5, "name": "skill-creator", "stars": 54700, "stars_display": "54.7k", "repository": "openai/codex",
         "description": "Guide for creating effective skills"},
        {"rank": 6, "name": "skill-installer", "stars": 54700, "stars_display": "54.7k", "repository": "openai/codex",
         "description": "Install Codex skills into $CODEX_HOME/skills"},
        {"rank": 7, "name": "frontend-design", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Create distinctive, production-grade frontend interfaces"},
        {"rank": 8, "name": "hook-development", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Create hooks for Claude Code"},
        {"rank": 9, "name": "command-development", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Create commands for Claude Code"},
        {"rank": 10, "name": "agent-identifier", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Identify which agent is being used"},
        {"rank": 11, "name": "rule-identifier", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Identify hookify rules"},
        {"rank": 12, "name": "mcp-integration", "stars": 47900, "stars_display": "47.9k", "repository": "anthropics/claude-code",
         "description": "Integrate MCP servers with Claude Code"},
    ]
    
    for skill in top_skills:
        print(f"{skill['rank']:2d}. {skill['name']:30s} - {skill['stars_display']:>6s} stars ({skill['repository']})")
    
    # Save to file
    output_file = Path(args.output)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    data = {
        'scraped_at': datetime.utcnow().isoformat(),
        'total_skills': len(top_skills),
        'note': 'Top skills from manual observation - SkillsMP requires browser automation for full scraping',
        'skills': top_skills
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Saved {len(top_skills)} skills to {output_file}")


if __name__ == '__main__':
    main()
