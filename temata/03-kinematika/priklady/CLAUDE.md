# PRAVIDLA PRO EDUKAČNÍ VYLEPŠENÍ KINEMATICKÝCH PŘÍKLADŮ

## HLAVNÍ CÍL
Transformovat všech 49 kinematických příkladů (example_01.html až example_49.html) na plně edukační materiály pro studenty středních škol s důrazem na POCHOPENÍ, ne jen výpočet.

## POVINNÁ STRUKTURA KAŽDÉHO PŘÍKLADU

### 1. MOTIVAČNÍ ÚVOD (před zadáním)
```html
<div class="intro-context">
    <strong>💡 Praktická aplikace:</strong> [Konkrétní příklad z reálného života - řidiči, záchranáři, inženýři, sport, atd.]
</div>
```

### 2. ZADÁNÍ (vylepšené)
- Zvýraznit klíčové hodnoty pomocí `<strong>` tagů
- Udržet původní text, jen přidat zvýraznění

### 3. KROK 1: ANALÝZA SITUACE
Povinné elementy:
```html
<div class="equation-logic-box">
    <strong>Logika výběru:</strong> [Vysvětlení PROČ jde o daný typ pohybu]
</div>

<div class="warning-box">
    <strong>Pozor na jednotky!</strong> [Specifické upozornění na jednotky pro daný příklad]
</div>

<div class="note-box">
    <strong>Dané hodnoty:</strong>
    <ul>
        <li>[Seznam všech daných hodnot]</li>
        <li>Hledáme: [co počítáme]</li>
    </ul>
</div>
```

### 4. KROK 2: VÝBĚR ROVNICE
Povinné elementy:
```html
<div class="equation-logic-box">
    <strong>Proč tuto rovnici?</strong> [Zdůvodnění výběru konkrétní rovnice]
</div>

<div class="formula-box">
    [Původní vzorec]
</div>

<div class="analogy-box">
    <strong>Praktická analogie:</strong> [Srovnání s běžnou situací]
</div>
```

### 5. KROK 3: VÝPOČET
- Rozdělit na dílčí kroky s vlastními result-box
- Přidat tip-box s užitečnými radami
- Použít details/summary pro pokročilé informace

### 6. KROK 4: KONTROLA A ODPOVĚĎ
Povinné elementy:
```html
<div class="summary-box">
    <strong>Odpověď:</strong> [Struktuovaná odpověď]
</div>

<div class="info-box">
    <strong>Kontrola rozumnosti:</strong> [Ověření, že výsledek dává smysl]
</div>

<div class="alternative-method-box">
    <strong>Alternativní způsob:</strong> [Jiný postup řešení]
</div>

<details>
    <summary>🤔 Metakognitivní otázky</summary>
    <div>
        <ul>
            <li>[Otázky k zamyšlení]</li>
        </ul>
    </div>
</details>
```

## REFERENČNÍ ZDROJ
Vždy používat kinematika_zadani_reseni.html jako referenci pro:
- Správné výpočty a postupy
- Inspiraci pro praktické analogie
- Metakognitivní otázky
- Alternativní metody

## KONTROLNÍ SEZNAM PRO KAŽDÝ PŘÍKLAD

### PŘED ÚPRAVOU:
- [ ] Přečíst původní example_XX.html
- [ ] Najít odpovídající řešení v kinematika_zadani_reseni.html
- [ ] Identifikovat typ kinematické úlohy
- [ ] Naplánovat praktické analogie

### PŘI ÚPRAVĚ:
- [ ] Přidat motivační úvod s praktickou aplikací
- [ ] Vysvětlit logiku výběru rovnice
- [ ] Přidat upozornění na časté chyby
- [ ] Vložit praktické analogie
- [ ] Rozdělit výpočet na logické kroky
- [ ] Přidat alternativní metody
- [ ] Vytvořit metakognitivní otázky

### PO ÚPRAVĚ:
- [ ] Zkontrolovat správnost všech výpočtů
- [ ] Ověřit, že všechny edukační boxy jsou použity
- [ ] Otestovat v prohlížeči (otevřít soubor)
- [ ] Označit jako dokončený v todo listu

## POUŽÍVANÉ CSS TŘÍDY

### Edukační boxy:
- `.intro-context` - motivační úvod
- `.equation-logic-box` - logika výběru rovnic
- `.warning-box` - upozornění na chyby
- `.tip-box` - užitečné tipy
- `.analogy-box` - praktické analogie
- `.interpretation-box` - fyzikální význam
- `.summary-box` - shrnutí odpovědi
- `.alternative-method-box` - alternativní postupy
- `.info-box` - obecné informace
- `.note-box` - poznámky a seznamy

### Strukturální:
- `.calculation-step` - jednotlivé kroky
- `.formula-box` - matematické vzorce
- `.result-box` - výsledky výpočtů
- `<details>/<summary>` - rozbalovací sekce

## TYPY KINEMATICKÝCH ÚLOH A JEJICH SPECIFIKA

### ROVNOMĚRNÝ POHYB:
- Analogie: vlak, dopravník, eskalátor
- Pozor na: jednotky času a rychlosti
- Tipы: plocha pod grafem v-t

### ROVNOMĚRNĚ ZRYCHLENÝ POHYB:
- Analogie: rozjezd auta, volný pád
- Pozor na: počáteční rychlost (v₀ = 0?)
- Tipy: výběr správné kinematické rovnice

### ROTAČNÍ POHYB:
- Analogie: ventilátory, motory, kola
- Pozor na: RPM vs rad/s převody
- Tipy: vztah mezi lineární a úhlovou rychlostí

## WORKFLOW PRO HROMADNÉ ZPRACOVÁNÍ

1. **PŘÍPRAVA**: Vytvořit todo list se všemi 49 příklady
2. **BATCH 1**: Příklady 1-10 (základní rovnoměrný pohyb)
3. **BATCH 2**: Příklady 11-25 (zrychlený pohyb)
4. **BATCH 3**: Příklady 26-35 (složitější kinematika)
5. **BATCH 4**: Příklady 36-49 (rotační pohyb a kombinace)

## KVALITNÍ STANDARDY

### MUSÍ MÍT:
- Všech 8 typů edukačních boxů alespoň jednou
- Praktickou analogii relevantní k příkladu
- Metakognitivní otázky (3-5 otázek)
- Alternativní metodu řešení
- Kontrolu rozumnosti výsledku

### NESMÍ MÍT:
- Obecné fráze bez konkrétního obsahu
- Chyby ve výpočtech
- Nekonzistentní CSS třídy
- Chybějící MathJax formátování

## POSTUP IMPLEMENTACE

Každý příklad zpracovat v tomto pořadí:
1. Read original example_XX.html
2. Grep corresponding solution from kinematika_zadani_reseni.html
3. MultiEdit with all educational enhancements
4. Bash open to test in browser
5. Mark completed in TodoWrite
6. Continue to next example

**CÍЛЬ**: Vytvořit nejlepší edukační materiály pro kinematiku v češtině na internetu!