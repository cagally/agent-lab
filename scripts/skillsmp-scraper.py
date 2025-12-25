#!/usr/bin/env python3
"""
SkillsMP Scraper - Extract top skills from skillsmp.com

Usage:
    python3 skillsmp-scraper.py --pages 8 --output ../skills-data/skillsmp-skills-top100.json

Author: Agent Lab Team
Date: 2025-12-25
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


class SkillsMPScraper:
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
            
            # Find all skill cards (links with skill info)
            skill_links = soup.find_all('a', href=re.compile(r'/skills/'))
            
            for link in skill_links:
                try:
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
        if not skill_url or not skill_url.startswith('/skills/'):
            return None
        
        full_url = f"{self.BASE_URL}{skill_url}"
        
        # Get text content
        text = link_element.get_text(strip=True)
        
        # Parse skill name (first part before stars)
        # Format: "skill-name.md 95.4k 1 2 3 4 export skill-name from..."
        parts = text.split()
        if not parts:
            return None
        
        skill_name = parts[0].replace('.md', '')
        
        # Parse stars (look for pattern like "95.4k" or "1.2k")
        stars_raw = None
        stars_int = 0
        for part in parts[1:4]:  # Stars usually in first few parts
            if 'k' in part.lower() or part.isdigit():
                stars_raw = part
                stars_int = self._parse_star_count(part)
                break
        
        # Parse repository from export statement
        # Format: "export skill-name from "author/repo""
        repo_match = re.search(r'from\s+"([^"]+)"', text)
        repository = repo_match.group(1) if repo_match else "unknown"
        
        # Parse description (everything after "export...")
        desc_match = re.search(r'export\s+\S+\s+from\s+"[^"]+"\s+(.+)', text)
        description = desc_match.group(1) if desc_match else ""
        
        return {
            'name': skill_name,
            'stars': stars_int,
            'stars_display': stars_raw or '0',
            'repository': repository,
            'skillsmp_url': full_url,
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
                return int(stars_str)
        except:
            return 0
    
    def scrape_skill_detail(self, skill_url: str) -> Optional[Dict]:
        """
        Scrape detailed information from a skill's detail page
        
        Args:
            skill_url: Full URL to skill detail page
            
        Returns:
            Dictionary with detailed skill information
        """
        print(f"  📄 Fetching details: {skill_url}")
        
        try:
            response = self.session.get(skill_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract SKILL.md content
            skill_md_content = ""
            skill_section = soup.find('div', {'id': 'SKILL.md'}) or soup.find('pre') or soup.find('code')
            if skill_section:
                skill_md_content = skill_section.get_text()
            
            # Extract metadata
            metadata = {
                'github_url': self._extract_github_url(soup),
                'last_updated': self._extract_last_updated(soup),
                'forks': self._extract_forks(soup),
                'skill_md_content': skill_md_content[:5000] if skill_md_content else None,  # First 5000 chars
                'has_marketplace_json': 'marketplace.json' in response.text
            }
            
            return metadata
            
        except Exception as e:
            print(f"  ⚠️  Error fetching details: {e}")
            return None
    
    def _extract_github_url(self, soup) -> Optional[str]:
        """Extract GitHub repository URL from page"""
        gh_link = soup.find('a', href=re.compile(r'github\.com'))
        return gh_link.get('href') if gh_link else None
    
    def _extract_last_updated(self, soup) -> Optional[str]:
        """Extract last updated date"""
        # Look for text like "updated: November 26, 2025"
        text = soup.get_text()
        match = re.search(r'updated:\s*([A-Za-z]+\s+\d+,\s+\d{4})', text)
        return match.group(1) if match else None
    
    def _extract_forks(self, soup) -> Optional[int]:
        """Extract fork count"""
        text = soup.get_text()
        match = re.search(r'forks:\s*([\d,]+)', text)
        if match:
            return int(match.group(1).replace(',', ''))
        return None
    
    def scrape_top_skills(self, num_pages: int = 8, include_details: bool = False) -> List[Dict]:
        """
        Scrape top skills from multiple pages
        
        Args:
            num_pages: Number of pages to scrape (12 skills per page)
            include_details: Whether to fetch detailed info for each skill
            
        Returns:
            List of skill dictionaries
        """
        all_skills = []
        
        for page in range(1, num_pages + 1):
            skills = self.scrape_homepage(page)
            
            if include_details:
                # Fetch detailed info for each skill
                for skill in skills:
                    details = self.scrape_skill_detail(skill['skillsmp_url'])
                    if details:
                        skill.update(details)
                    time.sleep(self.delay)  # Polite delay
            
            all_skills.extend(skills)
            
            # Polite delay between pages
            if page < num_pages:
                time.sleep(self.delay)
        
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
        print(f"📊 Top 5 skills by stars:")
        for skill in skills[:5]:
            print(f"  {skill['rank']}. {skill['name']} - {skill['stars_display']} stars ({skill['repository']})")


def main():
    parser = argparse.ArgumentParser(description='Scrape top skills from SkillsMP')
    parser.add_argument('--pages', type=int, default=8, help='Number of pages to scrape (default: 8)')
    parser.add_argument('--output', type=str, default='../skills-data/skillsmp-skills-top100.json',
                       help='Output JSON file path')
    parser.add_argument('--details', action='store_true', help='Fetch detailed info for each skill (slower)')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between requests in seconds')
    
    args = parser.parse_args()
    
    print("🚀 SkillsMP Scraper Starting...")
    print(f"📄 Pages to scrape: {args.pages}")
    print(f"💾 Output file: {args.output}")
    print(f"⏱️  Delay: {args.delay}s between requests\n")
    
    scraper = SkillsMPScraper(delay=args.delay)
    skills = scraper.scrape_top_skills(num_pages=args.pages, include_details=args.details)
    scraper.save_results(skills, args.output)
    
    print(f"\n✅ Scraping complete! Found {len(skills)} skills.")
    print(f"📁 Data saved to: {args.output}")


if __name__ == '__main__':
    main()
