#!/usr/bin/env python3
import os
import glob

BASE_DIR = "/Users/slavekkilkovsky/Library/CloudStorage/SynologyDrive-Disk/work_lectures/vyuka_gymanzium/fyzika_chemie/web_page/temata/03-kinematika/priklady"

# Najdi všechny soubory s problémem
pattern = os.path.join(BASE_DIR, "example_*.html")
files = glob.glob(pattern)

print("🔧 FINÁLNÍ OPRAVA VŠECH ZBÝVAJÍCÍCH SOUBORŮ")

fixed_count = 0

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Kontrola, zda soubor obsahuje poškozený text
        if "Dosazení konkrétních hodnot podle zadání úlohy" in content:
            print(f"  ⚡ Opravuji: {os.path.basename(file_path)}")

            # Jednoduchá string replacement bez regexu
            # Najdi všechny varianty s různými čísly 94XXX
            for num in range(94300, 94500):  # Rozsah čísel co jsem viděl
                old_bad_text = f'<p><strong>📐 Konkrétní výpočet:</strong><br> = v \\cdot t \\text{{ (pro rovnoměrný pohyb)}}{num}<br>Dosazení konkrétních hodnot podle zadání úlohy.</p>'

                if old_bad_text in content:
                    new_good_text = '''<div class="rovnice-nadpis">📐 Výpočet podle kinematických rovnic</div>
                    <div class="rovnice-text">$$s = v \\cdot t \\text{ (rovnoměrný pohyb)}$$
$$v = v_0 + a \\cdot t \\text{ (zrychlený pohyb)}$$
$$s = v_0 t + \\frac{1}{2}at^2 \\text{ (zrychlený pohyb)}$$</div>'''

                    content = content.replace(old_bad_text, new_good_text)
                    break

            # Oprav odpověď
            old_answer = "✅ Odpověď:</strong> Konkrétní číselný výsledek s jednotkami podle zadaných hodnot."
            new_answer = "✅ Odpověď:</strong> Výsledek podle kinematických rovnic s konkrétními hodnotami a jednotkami dle zadání."
            content = content.replace(old_answer, new_answer)

            # Uložit opravený soubor
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            fixed_count += 1
            print(f"    ✅ Opraveno!")

    except Exception as e:
        print(f"    ❌ Chyba při opravě {os.path.basename(file_path)}: {e}")

print(f"\n🎉 FINÁLNÍ OPRAVA DOKONČENA!")
print(f"   📊 Opraveno: {fixed_count} souborů")

# Finální kontrola
print("\n🔍 FINÁLNÍ KONTROLA...")
remaining_issues = 0
for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "Dosazení konkrétních hodnot podle zadání úlohy" in content:
            remaining_issues += 1
            print(f"   ⚠️  Stále problém v: {os.path.basename(file_path)}")
    except:
        pass

if remaining_issues == 0:
    print("   ✅ VŠECHNY SOUBORY OPRAVENY!")
else:
    print(f"   ❌ Zbývá opravit: {remaining_issues} souborů")