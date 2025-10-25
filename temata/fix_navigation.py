#!/usr/bin/env python3
import os
import re

# Complete sequence of topics (00-16)
topics = [
    "00-umela-inteligence",
    "01-bilance-systemu",
    "02-kinematika",
    "03-dynamika",
    "04-mechanicka-prace-energie",
    "05-gravitacni-pole",
    "06-mechanika-tuheho-telesa",
    "07-mechanika-tekutin",
    "08-molekulova-fyzika-termika",
    "09-vnitrni-energie-prace-teplo",
    "10-struktura-vlastnosti-plynu",
    "11-struktura-vlastnosti-pevnych-latek",
    "12-struktura-vlastnosti-kapalin",
    "13-zmeny-skupenstvi-latek",
    "14-kmitani-mechanickeho-oscilatoru",
    "15-mechanicke-vlneni",
    "16-elektricky-naboj-elektricke-pole"
]

base_path = "/Users/slavekkilkovsky/Library/CloudStorage/SynologyDrive-Disk/work_lectures/vyuka_gymanzium/fyzika_chemie/web_page/temata"

for i, topic in enumerate(topics):
    index_path = os.path.join(base_path, topic, "index.html")

    if not os.path.exists(index_path):
        print(f"Soubor neexistuje: {index_path}")
        continue

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the navigation section
    nav_pattern = r'<section class="section">.*?<div class="lecture-navigation">(.*?)</div>.*?</section>'
    match = re.search(nav_pattern, content, re.DOTALL)

    if not match:
        print(f"Navigace nenalezena v: {topic}")
        continue

    # Build new navigation
    new_nav = ""

    # Previous button
    if i > 0:
        prev_topic = topics[i-1]
        new_nav += f'''                <a href="../{prev_topic}/index.html" class="nav-btn secondary">
                    <i class="fas fa-arrow-left"></i> Předchozí téma
                </a>'''

    # Next button
    if i < len(topics) - 1:
        if new_nav:  # Add newline if there was previous button
            new_nav += "\n"
        next_topic = topics[i+1]
        new_nav += f'''                <a href="../{next_topic}/index.html" class="nav-btn secondary">
                    Další téma <i class="fas fa-arrow-right"></i>
                </a>'''

    # Replace the navigation section
    new_section = f'''<section class="section">
        <div class="container">
            <div class="lecture-navigation">
{new_nav}
            </div>
        </div>
    </section>'''

    # Find and replace the entire navigation section
    content = re.sub(
        r'<!-- Navigation -->.*?<section class="section">.*?<div class="lecture-navigation">.*?</div>.*?</section>',
        f'<!-- Navigation -->\n    {new_section}',
        content,
        flags=re.DOTALL
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {topic}: navigace aktualizována")

print("\n✅ Všechny navigační odkazy aktualizovány!")
