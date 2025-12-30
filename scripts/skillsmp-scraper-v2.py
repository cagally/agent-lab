#!/usr/bin/env python3
"""
SkillsMP Scraper V2 - Extract top skills from skillsmp.com (Updated for 2025)

Usage:
    python3 skillsmp-scraper-v2.py --pages 10 --output ../skills-data/skillsmp-top-skills.json

Author: Agent Lab Team
Date: 2025-12-30
"""

import argparse
import json
import time
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup


class SkillsMPScraperV2:
    """Scraper for skillsmp.com to extract top skills"""
    
    BASE_URL = "https://skillsmp.com"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    def __init__(self, delay: float = 2.0):
        """
        Initialize scraper
        
        Args:
            delay: Delay between requests in seconds (default 2.0 for polite scraping)
        """
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
    
    def scrape_homepage(self, page: int = 1) -> List[Dict]:
        """
        Scrape a single page from the homepage
        
        Args:
            page: Page number to scrape (1-indexed)
            
        Returns:
            List of skill dictionaries
        """
        url = f"{self.BASE_URL}/?page={page}" if page > 1 else self.BASE_URL
        
        print(f"📥 Scraping page {page}: {url}")
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            skills = []
            
            # Find all skill links - they end with .md and contain export statements
            # Format: "at-dispatch-v2.md 95.4k 1 2 3 4 export at-dispatch-v2 from "pytorch/pytorch" ..."
            skill_links = soup.find_all('a', href=True)
            
            for link in skill_links:
                try:
                    # Check if this is a skill link (contains .md in text)
                    text = link.get_text(strip=True)
                    if '.md' in text and 'export' in text:
                        skill_data = self._parse_skill_card(link)
                        if skill_data:
                            skills.append(skill_data)
                except Exception as e:
                    print(f"⚠️  Error parsing skill card: {e}")
                    continue
            
            print(f"✅ Found {len(skills)} skills on page {page}")
            return skills
            
        except Exception as e:
            print(f"❌ Error scraping page {page}: {e}")
            return []
    
    def _parse_skill_card(self, link_element) -> Optional[Dict]:
        """Parse a single skill card element"""
        
        # Get URL
        skill_url = link_element.get('href', '')
        if not skill_url:
            return None
        
        # Make sure it's a full URL
        if not skill_url.startswith('http'):
            skill_url = f"{self.BASE_URL}{skill_url}"
        
        # Get text content
        # Format: "at-dispatch-v2.md 95.4k 1 2 3 4 export at-dispatch-v2 from "pytorch/pytorch" Convert PyTorch AT_DISPATCH..."
        text = link_element.get_text(strip=True)
        
        # Parse skill name (first part before .md)
        name_match = re.match(r'^([a-zA-Z0-9_-]+)\.md', text)
        if not name_match:
            return None
        
        skill_name = name_match.group(1)
        
        # Parse stars (look for pattern like "95.4k" or "1.2k")
        stars_raw = None
        stars_int = 0
        # Stars appear after .md and before "export"
        stars_match = re.search(r'\.md\s+([\d.]+k?)\s+', text)
        if stars_match:
            stars_raw = stars_match.group(1)
            stars_int = self._parse_star_count(stars_raw)
        
        # Parse repository from export statement
        # Format: 'export skill-name from "author/repo"'
        repo_match = re.search(r'export\s+[a-zA-Z0-9_-]+\s+from\s+"([^"]+)"', text)
        repository = repo_match.group(1) if repo_match else "unknown"
        
        # Parse description (everything after the repository)
        desc_match = re.search(r'from\s+"[^"]+"\s+(.+)$', text)
        description = desc_match.group(1) if desc_match else ""
        
        return {
            'name': skill_name,
            'stars': stars_int,
            'stars_display': stars_raw or '0',
            'repository': repository,
            'skillsmp_url': skill_url,
            'description': description[:200] + '...' if len(description) > 200 else description,
            'scraped_at': datetime.utcnow().isoformat()
        }
    
    def _parse_star_count(self, stars_str: str) -> int:
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
    
    def scrape_top_skills(self, num_pages: int = 10) -> List[Dict]:
        """
        Scrape top skills from multiple pages
        
        Args:
            num_pages: Number of pages to scrape (12 skills per page)
            
        Returns:
            List of skill dictionaries sorted by stars
        """
        all_skills = []
        seen_names = set()
        
        for page in range(1, num_pages + 1):
            skills = self.scrape_homepage(page)
            
            # Deduplicate by name
            for skill in skills:
                if skill['name'] not in seen_names:
                    all_skills.append(skill)
                    seen_names.add(skill['name'])
            
            # Polite delay between pages
            if page < num_pages:
                time.sleep(self.delay)
        
        # Sort by stars (descending)
        all_skills.sort(key=lambda x: x['stars'], reverse=True)
        
        # Add rank
        for i, skill in enumerate(all_skills, 1):
            skill['rank'] = i
        
        return all_skills
    
    def save_results(self, skills: List[Dict], output_path: str):
        """Save scraped skills to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'scraped_at': datetime.utcnow().isoformat(),
            'total_skills': len(skills),
            'skills': skills
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Saved {len(skills)} skills to {output_file}")
        print(f"\n📊 Top 10 skills by stars:")
        for skill in skills[:10]:
            print(f"  {skill['rank']:2d}. {skill['name']:30s} - {skill['stars_display']:>6s} stars ({skill['repository']})")


def main():
    parser = argparse.ArgumentParser(description='Scrape top skills from SkillsMP')
    parser.add_argument('--pages', type=int, default=10, help='Number of pages to scrape (default: 10)')
    parser.add_argument('--output', type=str, default='../skills-data/skillsmp-top-skills.json',
                       help='Output JSON file path')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between requests in seconds')
    
    args = parser.parse_args()
    
    print("🚀 SkillsMP Scraper V2 Starting...")
    print(f"📄 Pages to scrape: {args.pages}")
    print(f"💾 Output file: {args.output}")
    print(f"⏱️  Delay: {args.delay}s between requests\n")
    
    scraper = SkillsMPScraperV2(delay=args.delay)
    skills = scraper.scrape_top_skills(num_pages=args.pages)
    scraper.save_results(skills, args.output)
    
    print(f"\n✅ Scraping complete! Found {len(skills)} unique skills.")
    print(f"📁 Data saved to: {args.output}")


if __name__ == '__main__':
    main()
