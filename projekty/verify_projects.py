#!/usr/bin/env python3
"""
Kontrolní script pro ověření správnosti všech HTML stránek projektů
"""

import os
import re
from pathlib import Path

def check_html_file(filepath):
    """Zkontroluje jeden HTML soubor podle požadovaných kritérií"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {
        'file': filepath.name,
        'checks': {}
    }

    # 1. Kontrola že NEOBSAHUJE "středa 14:00-15:00"
    if 'středa 14:00' in content or 'středa 14:00-15:00' in content:
        results['checks']['no_consultation_hours'] = '❌ OBSAHUJE zakázané konzultační hodiny'
    else:
        results['checks']['no_consultation_hours'] = '✅ Neobsahuje konzultační hodiny'

    # 2. Kontrola že obsahuje správný email kilkovsky.s@seznam.cz
    email_count = content.count('kilkovsky.s@seznam.cz')
    if email_count >= 2:  # Měl by být alespoň 2x (konzultace + footer)
        results['checks']['correct_email'] = f'✅ Email správně ({email_count}x)'
    else:
        results['checks']['correct_email'] = f'❌ Email chybí nebo nedostatečný počet ({email_count}x)'

    # 3. Kontrola UTF-8 encoding (české znaky)
    czech_chars = ['á', 'č', 'ď', 'é', 'ě', 'í', 'ň', 'ó', 'ř', 'š', 'ť', 'ú', 'ů', 'ý', 'ž']
    has_czech = any(char in content for char in czech_chars)
    if has_czech:
        results['checks']['czech_encoding'] = '✅ České znaky správně'
    else:
        results['checks']['czech_encoding'] = '⚠️  Žádné české znaky (možná OK)'

    # 4. Kontrola CSS linku
    if 'href="../css/main.css"' in content:
        results['checks']['css_link'] = '✅ CSS link správně'
    else:
        results['checks']['css_link'] = '❌ CSS link chybí nebo špatný'

    # 5. Kontrola konzultační sekce
    if 'Online konzultace: MS Teams (po domluvě)' in content:
        results['checks']['consultation_section'] = '✅ Konzultační sekce OK'
    else:
        results['checks']['consultation_section'] = '❌ Konzultační sekce chybí'

    return results

def main():
    """Hlavní funkce - zkontroluje všechny HTML soubory projektů"""

    projekty_dir = Path(__file__).parent
    html_files = sorted(projekty_dir.glob('projekt*_zadani.html'))

    print("=" * 70)
    print("KONTROLA HTML STRÁNEK PROJEKTŮ")
    print("=" * 70)
    print()

    all_passed = True

    for html_file in html_files:
        results = check_html_file(html_file)

        print(f"📄 {results['file']}")
        print("-" * 70)

        for check_name, check_result in results['checks'].items():
            print(f"  {check_result}")
            if '❌' in check_result:
                all_passed = False

        print()

    # Kontrola projekty.html
    projekty_html = projekty_dir / 'projekty.html'
    if projekty_html.exists():
        with open(projekty_html, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"📄 projekty.html")
        print("-" * 70)

        # Kontrola CSS cesty
        if 'href="../css/main.css"' in content:
            print('  ✅ CSS link správně (../css/main.css)')
        else:
            print('  ❌ CSS link špatně')
            all_passed = False

        # Kontrola target="_blank" pro všechny odkazy
        html_links = content.count('target="_blank"')
        if html_links >= 8:  # 4 projekty × 2 odkazy
            print(f'  ✅ Target="_blank" na odkazech ({html_links}x)')
        else:
            print(f'  ❌ Target="_blank" chybí na některých odkazech ({html_links}x)')
            all_passed = False

        # Kontrola DOCX ikon
        if 'fa-file-word' in content:
            print('  ✅ DOCX ikony správně (fa-file-word)')
        else:
            print('  ❌ DOCX ikony chybí nebo špatné')
            all_passed = False

        print()

    print("=" * 70)
    if all_passed:
        print("✅ VŠECHNY KONTROLY PROŠLY")
    else:
        print("❌ NĚKTERÉ KONTROLY SELHALY")
    print("=" * 70)

    return 0 if all_passed else 1

if __name__ == '__main__':
    exit(main())
