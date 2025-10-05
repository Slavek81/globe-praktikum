#!/usr/bin/env python3
"""Verification script for topic navigation buttons."""

import os
import re
from pathlib import Path

BASE_PATH = Path("/Users/slavekkilkovsky/Library/CloudStorage/SynologyDrive-Disk/work_lectures/vyuka_gymanzium/fyzika_chemie/web_page/temata")

# Define all topics
TOPICS = [
    "00-umela-inteligence",
    "01-matematicke-praktikum",
    "02-uvod-bilance",
    "03-kinematika",
    "04-dynamika",
    "05-mechanicka-prace-energie",
    "06-gravitacni-pole",
    "07-mechanika-tuheho-telesa",
    "08-mechanika-tekutin",
    "09-molekulova-fyzika-termika",
    "10-vnitrni-energie-prace-teplo",
    "11-struktura-vlastnosti-plynu",
    "12-struktura-vlastnosti-pevnych-latek",
    "13-struktura-vlastnosti-kapalin",
    "14-zmeny-skupenstvi-latek",
    "15-kmitani-mechanickeho-oscilatoru",
    "16-mechanicke-vlneni",
    "17-elektricky-naboj-elektricke-pole"
]

def check_navigation(topic_num, topic_folder):
    """Check navigation buttons for a topic."""
    index_file = BASE_PATH / topic_folder / "index.html"

    if not index_file.exists():
        return f"❌ Topic {topic_num}: index.html not found"

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract navigation section
    nav_pattern = r'<!-- Navigation -->.*?</section>'
    nav_match = re.search(nav_pattern, content, re.DOTALL)

    if not nav_match:
        return f"❌ Topic {topic_num}: No navigation section found"

    nav_section = nav_match.group(0)

    # Check for incorrect patterns (topic names)
    forbidden_patterns = [
        r'Předchozí téma:',
        r'Další téma:',
        r'Všechna témata'
    ]

    errors = []
    for pattern in forbidden_patterns:
        if re.search(pattern, nav_section):
            errors.append(f"Found forbidden text: {pattern}")

    # Check expected patterns based on topic position
    prev_btn = re.search(r'Předchozí téma\s*<', nav_section)
    next_btn = re.search(r'Další téma\s*<', nav_section)

    if topic_num == 0:
        # First topic: only "Další téma"
        if prev_btn:
            errors.append("Should NOT have 'Předchozí téma' button")
        if not next_btn:
            errors.append("Should have 'Další téma' button")
        if next_btn:
            if f'href="../{TOPICS[1]}/index.html"' not in nav_section:
                errors.append(f"'Další téma' should link to {TOPICS[1]}")

    elif topic_num == len(TOPICS) - 1:
        # Last topic: only "Předchozí téma"
        if not prev_btn:
            errors.append("Should have 'Předchozí téma' button")
        if next_btn:
            errors.append("Should NOT have 'Další téma' button")
        if prev_btn:
            if f'href="../{TOPICS[-2]}/index.html"' not in nav_section:
                errors.append(f"'Předchozí téma' should link to {TOPICS[-2]}")

    else:
        # Middle topics: both buttons
        if not prev_btn:
            errors.append("Should have 'Předchozí téma' button")
        if not next_btn:
            errors.append("Should have 'Další téma' button")
        if prev_btn:
            if f'href="../{TOPICS[topic_num-1]}/index.html"' not in nav_section:
                errors.append(f"'Předchozí téma' should link to {TOPICS[topic_num-1]}")
        if next_btn:
            if f'href="../{TOPICS[topic_num+1]}/index.html"' not in nav_section:
                errors.append(f"'Další téma' should link to {TOPICS[topic_num+1]}")

    if errors:
        return f"❌ Topic {topic_num:02d}: " + "; ".join(errors)
    else:
        return f"✅ Topic {topic_num:02d}: Navigation correct"

def main():
    print("=" * 80)
    print("NAVIGATION VERIFICATION REPORT")
    print("=" * 80)
    print()

    results = []
    errors = []

    for i, topic in enumerate(TOPICS):
        result = check_navigation(i, topic)
        results.append(result)
        if result.startswith("❌"):
            errors.append(result)
        print(result)

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total topics checked: {len(TOPICS)}")
    print(f"✅ Correct: {len(TOPICS) - len(errors)}")
    print(f"❌ Errors: {len(errors)}")

    if errors:
        print("\nERRORS FOUND:")
        for error in errors:
            print(f"  {error}")
        return 1
    else:
        print("\n🎉 ALL NAVIGATION BUTTONS ARE CORRECT!")
        return 0

if __name__ == "__main__":
    exit(main())
