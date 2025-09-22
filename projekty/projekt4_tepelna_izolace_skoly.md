# Semestrální projekt 4: Optimalizace tepelné izolace školy - teoretická studie

## Základní informace
- **Předmět:** Praktické použití fyziky a chemie
- **Typ projektu:** Energetický audit a optimalizační studie
- **Časová dotace:** 16 týdnů (2 hodiny týdně + domácí příprava)
- **Práce v týmu:** 2-3 studenti

## Charakteristika projektu
Studenti zpracují zjednodušený energetický audit školní budovy se zaměřením na tepelné ztráty a navrhnou optimalizaci tepelné izolace. Projekt kombinuje teoretické znalosti stavební fyziky s praktickou aplikací na reálnou budovu, ekonomickým hodnocením a environmentálními aspekty.

## Cíle projektu

### Hlavní cíl
Analyzovat tepelně-technické vlastnosti školní budovy, identifikovat kritická místa tepelných ztrát a navrhnout ekonomicky optimální řešení zateplení.

### Dílčí cíle
1. Osvojit si principy přenosu tepla ve stavebních konstrukcích
2. Naučit se pracovat s normami ČSN v oblasti stavební fyziky
3. Pochopit metodiku energetického auditu
4. Rozvíjet schopnost systémového přístupu k řešení problémů
5. Získat praktické zkušenosti s hodnocením investic

## Zadání projektu

### 1. Mapování současného stavu (25% hodnocení)

#### 1.1 Dokumentace budovy

**Získání podkladů**
- Půdorysy všech podlaží (1:100)
- Řezy budovou (1:100)
- Situační plán
- Rok výstavby a rekonstrukcí
- Technická dokumentace (pokud existuje)

**Vlastní měření a dokumentace**
- Ověření rozměrů
- Fotodokumentace fasád
- Identifikace konstrukčního systému
- Orientace ke světovým stranám

#### 1.2 Stavební konstrukce

**Obvodové stěny**
- Materiál a tloušťka
- Součinitel prostupu tepla U [W/m²·K]
- Plocha stěn podle orientace [m²]
- Tepelné mosty

**Střecha/strop pod půdou**
- Typ konstrukce
- Skladba vrstev
- Současné zateplení
- Součinitel U [W/m²·K]

**Výplně otvorů**
- Typy oken (jednoduché, dvojité, trojité)
- Materiál rámů
- Součinitel Uw [W/m²·K]
- Celková plocha oken [m²]

**Podlaha/strop nad suterénem**
- Konstrukce
- Zateplení (pokud existuje)
- Součinitel U [W/m²·K]

#### 1.3 Vytápěcí systém
- Zdroj tepla (typ, výkon, účinnost)
- Roční spotřeba energie [GJ/rok]
- Náklady na vytápění [Kč/rok]
- Otopná soustava (radiátory, podlahové)

### 2. Výpočet tepelných ztrát (35% hodnocení)

#### 2.1 Tepelné ztráty prostupem

**Metodika výpočtu dle ČSN 73 0540**

Pro každou konstrukci vypočítejte:
```
HT,i = Ai × Ui × bi [W/K]
```
kde:
- Ai = plocha konstrukce [m²]
- Ui = součinitel prostupu tepla [W/m²·K]
- bi = teplotní redukční činitel [-]

**Výpočty pro:**
- Obvodové stěny (S, J, V, Z)
- Střecha/strop pod půdou
- Podlaha/strop nad suterénem
- Okna a dveře

**Celková měrná ztráta prostupem:**
```
HT = ΣHT,i + ΔHT,tb [W/K]
```
kde ΔHT,tb jsou tepelné mosty (10-15% z HT)

#### 2.2 Tepelné ztráty větráním

**Přirozené větrání**
```
HV = 0,34 × n × V [W/K]
```
kde:
- n = intenzita výměny vzduchu [h⁻¹]
- V = objem vytápěného prostoru [m³]

**Nucené větrání (pokud existuje)**
- Průtok vzduchu [m³/h]
- Účinnost rekuperace [%]

#### 2.3 Celková tepelná ztráta

```
Q = (HT + HV) × (ti - te) [W]
```
kde:
- ti = vnitřní teplota (20°C)
- te = venkovní výpočtová teplota (-15°C)

#### 2.4 Roční potřeba tepla

**Denostupňová metoda**
```
E = 24 × ε × (HT + HV) × D / 1000 [GJ/rok]
```
kde:
- ε = opravný součinitel (0,8-0,9)
- D = počet denostupňů [K·den]

### 3. Návrh úsporných opatření (30% hodnocení)

#### 3.1 Katalog opatření

Pro každé opatření určete:
- Technické řešení
- Zlepšení součinitele U
- Investiční náklady [Kč]
- Úspora energie [GJ/rok]
- Prostá návratnost [roky]

**Opatření 1: Zateplení fasády**
- ETICS 160 mm EPS/MW
- U před: 1,2 W/m²·K → U po: 0,20 W/m²·K
- Cena: 1 800 Kč/m² včetně montáže

**Opatření 2: Zateplení střechy/stropu**
- 300 mm minerální vaty
- U před: 0,8 W/m²·K → U po: 0,12 W/m²·K
- Cena: 800 Kč/m²

**Opatření 3: Výměna oken**
- Trojsklo s teplým rámem
- Uw před: 2,8 W/m²·K → Uw po: 0,8 W/m²·K
- Cena: 12 000 Kč/m²

**Opatření 4: Zateplení soklu**
- XPS 120 mm
- U před: 1,5 W/m²·K → U po: 0,25 W/m²·K
- Cena: 2 200 Kč/m²

**Opatření 5: Instalace rekuperace**
- Účinnost 85%
- Investice: 500 000 Kč
- Úspora větrání: 70%

#### 3.2 Výpočet úspor

Pro každé opatření:
```
ΔE = 24 × ε × ΔH × D / 1000 [GJ/rok]
```
kde ΔH = snížení tepelné ztráty [W/K]

Finanční úspora:
```
ΔN = ΔE × cena_tepla [Kč/rok]
```

#### 3.3 Kombinace opatření

**Varianta A: Minimální**
- Pouze nejnutnější opravy
- Investice do 1 mil. Kč

**Varianta B: Optimální**
- Nejlepší poměr cena/výkon
- Návratnost do 10 let

**Varianta C: Komplexní**
- Pasivní standard
- Maximální úspory

### 4. Ekonomické vyhodnocení (10% hodnocení)

#### 4.1 Investiční náklady

| Opatření | Množství | Jednotková cena | Celkem |
|----------|----------|-----------------|--------|
| Zateplení fasády | m² | Kč/m² | Kč |
| Zateplení střechy | m² | Kč/m² | Kč |
| Výměna oken | m² | Kč/m² | Kč |
| **CELKEM** | | | **Kč** |

#### 4.2 Hodnocení variant

Pro každou variantu vypočítejte:
- Celkové investiční náklady [Kč]
- Roční úspora energie [GJ]
- Roční úspora nákladů [Kč]
- Prostá návratnost [roky]
- NPV (20 let, i = 4%)
- IRR [%]

#### 4.3 Prioritizace opatření

Seřaďte opatření podle:
1. Návratnosti (nejkratší první)
2. Absolutní úspory (největší první)
3. Technické naléhavosti

#### 4.4 Dotační možnosti
- Nová zelená úsporám
- OPŽP
- Vlastní zdroje

## Výstupy projektu

### 1. Energetický audit (15-20 stran)

**Struktura dokumentu:**

1. **Identifikační údaje**
   - Název budovy
   - Adresa
   - Vlastník/provozovatel
   - Zpracovatel auditu

2. **Executive summary** (1 strana)
   - Hlavní zjištění
   - Doporučení
   - Ekonomické ukazatele

3. **Popis budovy**
   - Stavebně-technické řešení
   - Vytápěcí systém
   - Současná spotřeba

4. **Výpočet tepelných ztrát**
   - Metodika
   - Detailní výpočty
   - Souhrnné tabulky

5. **Návrh opatření**
   - Technická řešení
   - Výpočet úspor
   - Investiční náklady

6. **Ekonomické vyhodnocení**
   - Varianty řešení
   - Finanční analýza
   - Doporučení

7. **Environmentální přínosy**
   - Snížení emisí CO₂
   - Úspora primární energie

8. **Závěr a doporučení**

9. **Přílohy**
   - Výpočtové tabulky
   - Půdorysy s vyznačením opatření
   - Fotodokumentace
   - Cenové nabídky

### 2. Prezentace pro vedení školy

**PowerPoint (15 minut)**
- Současný stav (fotky, termovize)
- Tepelné ztráty (graf rozdělení)
- Navrhovaná opatření (vizualizace)
- Investice vs. úspory (graf návratnosti)
- Varianty řešení (srovnávací tabulka)
- Dotační možnosti
- Doporučený postup

### 3. Informační leták

**A4 oboustranně**
- Pro studenty a rodiče
- Jednoduché vysvětlení problému
- Navrhovaná řešení
- Přínosy (úspory, komfort, ekologie)

### 4. 3D vizualizace (bonus)
- Model budovy před/po zateplení
- Tepelné toky
- Kritická místa

## Hodnotící kritéria

### Bodové hodnocení (100 bodů)

| Část | Body | Kritéria |
|------|------|----------|
| **Analýza stavu** | 25 | Úplnost dat, správnost U-hodnot |
| **Výpočty** | 35 | Metodika, správnost, interpretace |
| **Návrh opatření** | 30 | Realističnost, komplexnost, inovace |
| **Ekonomika** | 10 | Správnost analýzy, závěry |

### Bonusové body (max. 10)
- Termovizní snímky: +3 body
- Konzultace s energetickým auditorem: +2 body
- 3D model/vizualizace: +3 body
- Měření infiltrace (blower door): +2 body

## Časový harmonogram

| Týden | Fáze | Úkoly | Výstup |
|-------|------|-------|--------|
| 1-2 | Start | Týmy, studium zadání | Plán projektu |
| 3-4 | Mapování | Dokumentace budovy | Technické podklady |
| 5-6 | Analýza | Součinitele U, plochy | Tabulka konstrukcí |
| 7-8 | Výpočty I | Tepelné ztráty | Výpočtový protokol |
| 9-10 | Výpočty II | Roční spotřeba | Energetická bilance |
| 11-12 | Návrhy | Opatření, úspory | Katalog opatření |
| 13 | Ekonomika | Hodnocení variant | Finanční analýza |
| 14-15 | Dokumentace | Audit, prezentace | Finální dokumenty |
| 16 | Prezentace | Obhajoby | Prezentace |

## Doporučené zdroje

### Normy a předpisy
1. ČSN 73 0540 - Tepelná ochrana budov
2. ČSN EN ISO 13790 - Energetická náročnost budov
3. Vyhláška 78/2013 Sb. - Energetická náročnost budov
4. TNI 73 0329 - Zjednodušené výpočtové hodnocení

### Literatura
1. VAVERKA, J. a kol.: Stavební tepelná technika a energetika budov. Brno: VUTIUM, 2006
2. ŘEHÁNEK, J.: Tepelná akumulace budov. Praha: ČKAIT, 2002
3. HÁJEK, P.: Pozemní stavitelství III. Praha: ČVUT, 2004

### Online nástroje
- www.tzb-info.cz/tabulky-a-vypocty/58-prostup-tepla-vicevrstvou-konstrukci
- www.isover.cz/aplikace/tep-technika
- www.knaufinsulation.cz/kalkulacka-uspor
- www.nkn.cz - Národní kalkulační nástroj

### Software (volitelné)
- Teplo (Svoboda Software)
- Area (Svoboda Software)
- Energy+ (pokročilí)

### Katalogy materiálů
- ISOVER, ROCKWOOL - tepelné izolace
- BAUMIT, STO - ETICS systémy
- VEKRA, INTERNORM - okna a dveře

## Praktické pokyny

### Získávání dat
1. **Kontaktujte správce budovy** - technická dokumentace
2. **Změřte si sami** - laser, pásmo
3. **Využijte katastr** - půdorys budovy
4. **Fotodokumentace** - všechny fasády
5. **Ptejte se** - rok rekonstrukcí, problémy

### Určení součinitelů U

**Pokud neznáte skladbu:**
- Použijte tabulkové hodnoty dle roku výstavby
- Orientační hodnoty:
  - Nezateplená zeď 45 cm: U = 1,2 W/m²·K
  - Okna dvojitá stará: U = 2,8 W/m²·K
  - Střecha nezateplená: U = 0,8-1,0 W/m²·K

### Časté chyby
- Zapomenutí na tepelné mosty (+10-15%)
- Špatné jednotky (W vs. kW, GJ vs. kWh)
- Nereálné ceny (ověřte u firem)
- Zanedbání údržby a životnosti
- Podcenění přípravných prací

### Tipy pro úspěch
1. **Začněte včas** - získání dat trvá
2. **Rozdělte si práci** - každý člen něco
3. **Kontrolujte výpočty** - řády veličin
4. **Používejte Excel** - snadné přepočty
5. **Konzultujte** - využijte všech možností

## Rozšíření projektu

### Pokročilé analýzy
- Dynamická simulace (hodinový krok)
- Tepelné zisky (sluneční, vnitřní)
- Letní přehřívání
- Denní světlo

### Další opatření
- Fotovoltaika
- Tepelné čerpadlo
- Zelená střecha
- Stínění

## Konzultace

### Pravidelné
- **Středa:** 14:00-15:00 (kabinet fyziky)
- **Online:** MS Teams (rezervace)

### Speciální (po domluvě)
- Energetický auditor
- Projektant pozemních staveb
- Zástupce dodavatele izolací

### Kontrolní body
- **Týden 4:** Dokumentace budovy
- **Týden 8:** Kontrola výpočtů
- **Týden 12:** Návrh opatření

## Poznámky

### Bezpečnost
- Při dokumentaci dodržujte bezpečnost
- Nevstupujte na střechu bez povolení
- Při měření používejte OOPP

### Etika
- Respektujte soukromí
- Nefotografujte osoby
- Data používejte pouze pro projekt

## Kontakt
**Vyučující:** [Jméno učitele]  
**Email:** [email]  
**Kabinet:** [číslo místnosti]  
**MS Teams:** [odkaz na tým]