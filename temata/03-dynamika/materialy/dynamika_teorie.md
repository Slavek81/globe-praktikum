---
title: "Dynamika - Teoretický přehled"
subtitle: "Základní teorie, rovnice a jednotky"
author: "Fyzika - opakování a prohloubení"
date: "2025"
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
---

# 1. Newtonovy zákony pohybu

## 1. Newtonův zákon (Zákon setrvačnosti)

**Formulace:**
> Těleso setrvává v klidu nebo v rovnoměrném přímočarém pohybu, pokud není nuceno vnějšími silami tento stav změnit.

**Fyzikální význam:**
- Každé těleso má vlastnost setrvačnosti
- Setrvačnost závisí na hmotnosti
- Platí v inerciálních vztažných soustavách

## 2. Newtonův zákon (Zákon síly)

**Rovnice:**
$$\vec{F} = m \cdot \vec{a}$$

nebo

$$\vec{a} = \frac{\vec{F}}{m}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $\vec{F}$ | Síla (vektor) | N (Newton) |
| $m$ | Hmotnost | kg |
| $\vec{a}$ | Zrychlení (vektor) | m/s² |

**Fyzikální význam:**
- Síla způsobuje zrychlení
- Zrychlení je přímo úměrné síle a nepřímo úměrné hmotnosti
- Směr zrychlení je stejný jako směr výsledné síly

## 3. Newtonův zákon (Zákon akce a reakce)

**Formulace:**
> Každé působení (akce) vyvolává stejně velké opačné působení (reakci).

**Rovnice:**
$$\vec{F}_{12} = -\vec{F}_{21}$$

**Fyzikální význam:**
- Síly vznikají vždy ve dvojicích
- Akce a reakce působí na různá tělesa
- Akce a reakce mají stejnou velikost a opačný směr

\newpage

# 2. Druhy sil

## Tíhová síla

**Rovnice:**
$$F_g = m \cdot g$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $F_g$ | Tíhová síla | N |
| $m$ | Hmotnost | kg |
| $g$ | Tíhové zrychlení | m/s² |

**Fyzikální význam:**
- Gravitační síla působící na těleso v blízkosti Země
- Na Zemi: $g \approx 9{,}81$ m/s²
- Směřuje svisle dolů k středu Země

## Třecí síla

**Rovnice:**
$$F_t = f \cdot F_n$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $F_t$ | Třecí síla | N |
| $f$ | Součinitel tření | - |
| $F_n$ | Normálová síla | N |

**Druhy tření:**
- **Statické tření** ($f_s$) - těleso v klidu
- **Kinetické tření** ($f_k$) - těleso v pohybu
- Platí: $f_s > f_k$

## Dostředivá síla

**Rovnice:**
$$F_d = m \cdot \frac{v^2}{r} = m \cdot \omega^2 \cdot r$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $F_d$ | Dostředivá síla | N |
| $m$ | Hmotnost | kg |
| $v$ | Obvodová rychlost | m/s |
| $r$ | Poloměr | m |
| $\omega$ | Úhlová rychlost | rad/s |

**Fyzikální význam:**
- Výslednice sil při pohybu po kružnici
- Směřuje k středu kružnice
- Nutná pro udržení kruhové trajektorie

\newpage

# 3. Síla na nakloněné rovině

## Rozklad tíhové síly

**Rovnoběžná složka (po nakloněné rovině):**
$$F_{||} = m \cdot g \cdot \sin \alpha$$

**Kolmá složka (na nakloněnou rovinu):**
$$F_{\perp} = m \cdot g \cdot \cos \alpha$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $F_{||}$ | Síla rovnoběžná s rovinou | N |
| $F_{\perp}$ | Síla kolmá k rovině | N |
| $\alpha$ | Úhel sklonu roviny | ° nebo rad |

**Normálová síla:**
$$F_n = F_{\perp} = m \cdot g \cdot \cos \alpha$$

**Podmínka rovnováhy (bez tření):**
$$F_{tah} = F_{||} = m \cdot g \cdot \sin \alpha$$

**S třením:**
$$F_{tah} = m \cdot g \cdot \sin \alpha + f \cdot m \cdot g \cdot \cos \alpha$$

\newpage

# 4. Hybnost a zákony zachování

## Hybnost

**Definice:**
> Hybnost je vektorová veličina rovná součinu hmotnosti a rychlosti.

**Rovnice:**
$$\vec{p} = m \cdot \vec{v}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $\vec{p}$ | Hybnost | kg·m/s |
| $m$ | Hmotnost | kg |
| $\vec{v}$ | Rychlost | m/s |

## Zákon zachování hybnosti

**Formulace:**
> V izolované soustavě je celková hybnost konstantní.

**Rovnice:**
$$\sum \vec{p}_{\text{před}} = \sum \vec{p}_{\text{po}}$$

Pro dvě tělesa:
$$m_1 \vec{v}_1 + m_2 \vec{v}_2 = m_1 \vec{v}'_1 + m_2 \vec{v}'_2$$

**Aplikace:**
- Srážky těles (pružné i nepružné)
- Výstřel z děla (zpětný ráz)
- Raketový pohon

## Impuls síly

**Definice:**
> Impuls síly je změna hybnosti.

**Rovnice:**
$$\Delta \vec{p} = \vec{F} \cdot \Delta t$$

nebo
$$\vec{F} = \frac{\Delta \vec{p}}{\Delta t}$$

**Fyzikální význam:**
- Stejná změna hybnosti může být dosažena malou silou po dlouhý čas nebo velkou silou po krátký čas
- Airbag v autě prodlužuje dobu nárazu → menší síla

\newpage

# 5. Fyzikální konstanty

| Konstanta | Symbol | Hodnota | Jednotka |
|-----------|--------|---------|----------|
| Tíhové zrychlení (Země) | $g$ | 9,81 | m/s² |
| Tíhové zrychlení (Měsíc) | $g_M$ | 1,62 | m/s² |

## Typické hodnoty součinitelů tření

| Materiály | Statické $f_s$ | Kinetické $f_k$ |
|-----------|----------------|-----------------|
| Ocel - ocel | 0,74 | 0,57 |
| Dřevo - dřevo | 0,25-0,50 | 0,20 |
| Led - led | 0,10 | 0,03 |
| Guma - suchý asfalt | 1,0 | 0,8 |
| Guma - mokrý asfalt | 0,7 | 0,5 |

\newpage

# 6. Souhrn jednotek v SI

| Veličina | Jednotka SI | Odvození | Poznámka |
|----------|-------------|----------|----------|
| Síla | N (Newton) | kg·m/s² | 1 N = síla potřebná k udělení zrychlení 1 m/s² tělesu o hmotnosti 1 kg |
| Hmotnost | kg (kilogram) | - | Základní jednotka |
| Zrychlení | m/s² | - | - |
| Hybnost | kg·m/s | - | Alternativně N·s |
| Impuls síly | N·s | - | Alternativně kg·m/s |

\newpage

# Poznámky

- **Inerciální soustava:** Vztažná soustava, ve které platí Newtonovy zákony (soustava pohybující se rovnoměrně přímočaře nebo v klidu)
- **Setrvačná hmotnost vs. tíhová hmotnost:** V klasické mechanice jsou totožné, obecně mohou být různé
- **Výsledná síla:** Vektorový součet všech sil působících na těleso
- **Rovnováha sil:** $\sum \vec{F} = 0$ → těleso je v klidu nebo se pohybuje rovnoměrně přímočaře
- **Třecí síla:** Vždy působí proti směru pohybu (nebo možného pohybu)
- **Izolovaná soustava:** Soustava, na kterou nepůsobí vnější síly (uzavřená soustava)
- **Pružná srážka:** Zachovává se hybnost i kinetická energie
- **Nepružná srážka:** Zachovává se pouze hybnost, ne kinetická energie
