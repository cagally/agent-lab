#!/usr/bin/env python3
"""
Security Audit Script
Scans skill files for dangerous patterns and security risks.
"""

import os
import sys
import re
import json
from pathlib import Path

# Dangerous patterns to detect
DANGEROUS_PATTERNS = [
    # Destructive file operations
    (r'rm\s+-rf', 'Destructive file deletion (rm -rf)', 'CRITICAL'),
    (r'rm\s+.*\*', 'Wildcard file deletion', 'HIGH'),
    (r'dd\s+if=', 'Direct disk write (dd command)', 'CRITICAL'),
    
    # Code execution
    (r'eval\s*\(', 'Dynamic code execution (eval)', 'HIGH'),
    (r'exec\s*\(', 'Dynamic code execution (exec)', 'HIGH'),
    (r'__import__', 'Dynamic module import', 'MEDIUM'),
    
    # Network/External access
    (r'requests\.get\(.*http', 'External HTTP request', 'MEDIUM'),
    (r'urllib.*urlopen', 'URL opening', 'MEDIUM'),
    (r'socket\.', 'Raw socket usage', 'HIGH'),
    
    # Credentials/Secrets
    (r'password\s*=\s*["\']', 'Hardcoded password', 'CRITICAL'),
    (r'api[_-]?key\s*=\s*["\']', 'Hardcoded API key', 'CRITICAL'),
    (r'secret\s*=\s*["\']', 'Hardcoded secret', 'CRITICAL'),
    (r'token\s*=\s*["\'][a-zA-Z0-9]{20,}', 'Hardcoded token', 'CRITICAL'),
    
    # File system manipulation
    (r'chmod\s+777', 'Overly permissive file permissions', 'HIGH'),
    (r'chown\s+.*root', 'Ownership change to root', 'HIGH'),
    
    # Dangerous bash patterns
    (r';\s*rm\s+', 'Command chaining with rm', 'HIGH'),
    (r'\|\s*sh', 'Piping to shell', 'HIGH'),
    (r'>\s*/dev/null\s+2>&1', 'Output suppression (potential hiding)', 'LOW'),
    
    # SQL injection risks
    (r'execute\(.*%s', 'Potential SQL injection', 'HIGH'),
    (r'cursor\.execute\(.*\+', 'String concatenation in SQL', 'HIGH'),
]

def scan_file(file_path):
    """Scan a single file for dangerous patterns."""
    findings = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
            
            for pattern, description, severity in DANGEROUS_PATTERNS:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    # Find line number
                    line_num = content[:match.start()].count('\n') + 1
                    line_content = lines[line_num - 1].strip()
                    
                    findings.append({
                        'file': str(file_path),
                        'line': line_num,
                        'pattern': description,
                        'severity': severity,
                        'matched_text': match.group(),
                        'line_content': line_content
                    })
    except Exception as e:
        print(f"Error scanning {file_path}: {e}")
    
    return findings

def scan_skill_directory(skill_path):
    """Scan all files in a skill directory."""
    all_findings = []
    
    # Scan all files recursively
    for root, dirs, files in os.walk(skill_path):
        for file in files:
            file_path = Path(root) / file
            # Skip binary files and common non-code files
            if file_path.suffix in ['.md', '.py', '.sh', '.bash', '.js', '.yml', '.yaml', '.txt']:
                findings = scan_file(file_path)
                all_findings.extend(findings)
    
    return all_findings

def calculate_security_score(findings):
    """Calculate security score based on findings."""
    if not findings:
        return 10, "Safe"
    
    # Count by severity
    critical_count = sum(1 for f in findings if f['severity'] == 'CRITICAL')
    high_count = sum(1 for f in findings if f['severity'] == 'HIGH')
    medium_count = sum(1 for f in findings if f['severity'] == 'MEDIUM')
    low_count = sum(1 for f in findings if f['severity'] == 'LOW')
    
    # Any critical finding = automatic 0
    if critical_count > 0:
        return 0, "Unsafe"
    
    # Calculate score based on severity weights
    penalty = (high_count * 3) + (medium_count * 1.5) + (low_count * 0.5)
    score = max(0, 10 - penalty)
    
    if score >= 8:
        rating = "Safe"
    elif score >= 5:
        rating = "Caution"
    else:
        rating = "Unsafe"
    
    return round(score, 1), rating

def main():
    if len(sys.argv) < 2:
        print("Usage: python eval-security-audit.py <path-to-skill-directory>")
        print("Example: python eval-security-audit.py ../skills-data/raw-skills/pytorch-skill-writer")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    
    if not skill_path.is_dir():
        print(f"Error: {skill_path} is not a directory")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"Security Audit: {skill_path.name}")
    print(f"{'='*60}\n")
    
    print("Scanning files...")
    findings = scan_skill_directory(skill_path)
    
    score, rating = calculate_security_score(findings)
    
    print(f"\n**Security Score: {score}/10**")
    print(f"Rating: {rating}\n")
    
    if findings:
        print(f"Found {len(findings)} potential security issues:\n")
        
        # Group by severity
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            severity_findings = [f for f in findings if f['severity'] == severity]
            if severity_findings:
                print(f"\n{severity} ({len(severity_findings)}):")
                for finding in severity_findings:
                    print(f"  - {finding['pattern']}")
                    print(f"    File: {finding['file']}, Line: {finding['line']}")
                    print(f"    Code: {finding['line_content'][:80]}")
                    print()
    else:
        print("✅ No security issues detected!\n")
    
    # Save results
    result = {
        'skill_name': skill_path.name,
        'score': score,
        'rating': rating,
        'findings_count': len(findings),
        'findings': findings
    }
    
    output_file = skill_path / "security-audit-result.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
