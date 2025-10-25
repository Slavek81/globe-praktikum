---
title: "Úvod a bilance - Teoretický přehled"
subtitle: "Základní teorie, rovnice a jednotky"
author: "Fyzika - opakování a prohloubení"
date: "2025"
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
---

# 1. Základní pojmy

## Teplota (Temperature)

**Definice:**
> Teplota je stavová veličina vyjadřující průměrnou kinetickou energii molekul látky. Je nezávislá na množství látky.

**Jednotky:**
- **°C** (stupeň Celsia) - nejběžnější v Evropě
- **K** (Kelvin) - základní jednotka SI, absolutní teplota
- **°F** (stupeň Fahrenheita) - používá se v USA

**Převody:**
$$T[K] = T[°C] + 273{,}15$$
$$T[°F] = T[°C] \times \frac{9}{5} + 32$$

## Teplo (Heat)

**Definice:**
> Teplo je dějová veličina - forma energie, která se přenáší mezi tělesy s různou teplotou. Závisí na množství látky, teplotním rozdílu a druhu látky.

**Jednotka:** J (Joule)

## Tepelný tok (Heat Flow)

**Definice:**
> Tepelný tok udává množství tepla přenášeného za jednotku času.

**Rovnice:**
$$\dot{Q} = \frac{Q}{t}$$

**Jednotka:** W (Watt) = J/s

## Entalpie (Enthalpy)

**Definice:**
> Entalpie je fyzikální veličina rozměru energie, která vyjadřuje celkovou energii systému včetně vnitřní energie a energie spojené s tlakem a objemem.

**Symbol:** H
**Jednotka:** J (Joule)

\newpage

# 2. Základní rovnice

## Diskontinuální provoz (bez průtoku v čase)

**Ohřev nebo ochlazení látky:**
$$Q = m \cdot c_p \cdot (T_2 - T_1)$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $Q$ | Teplo | J (Joule) |
| $m$ | Hmotnost | kg |
| $c_p$ | Měrná tepelná kapacita | J/(kg·K) |
| $T_1$ | Počáteční teplota | °C nebo K |
| $T_2$ | Konečná teplota | °C nebo K |

## Kontinuální provoz (s průtokem v čase)

**Ohřev nebo ochlazení tekutiny:**
$$\dot{Q} = \dot{m} \cdot c_p \cdot (T_2 - T_1)$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $\dot{Q}$ | Tepelný tok | W (Watt) |
| $\dot{m}$ | Hmotnostní tok | kg/s |
| $c_p$ | Měrná tepelná kapacita | J/(kg·K) |
| $T_1$ | Teplota na vstupu | °C nebo K |
| $T_2$ | Teplota na výstupu | °C nebo K |

## S fázovou změnou (var/kondenzace)

**Kompletní rovnice s odpařováním:**
$$\dot{Q} = \dot{m} \cdot c_{p,kapaliny} \cdot (T_{var} - T_1) + \dot{m} \cdot l_v + \dot{m} \cdot c_{p,páry} \cdot (T_2 - T_{var})$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $c_{p,kapaliny}$ | Měrná tepelná kapacita kapaliny | J/(kg·K) |
| $c_{p,páry}$ | Měrná tepelná kapacita páry | J/(kg·K) |
| $l_v$ | Měrné skupenské teplo varu | J/kg |
| $T_{var}$ | Teplota varu | °C nebo K |

**Fyzikální význam:**
- **První člen:** Ohřev kapaliny na teplotu varu
- **Druhý člen:** Energie potřebná ke změně skupenství (odpařování)
- **Třetí člen:** Ohřev páry nad teplotu varu

\newpage

# 3. Zákony zachování

## Zákon zachování hmoty

**Obecná bilance:**
$$\text{Vstup} = \text{Výstup} + \text{Akumulace}$$

**Pro ustálený stav (akumulace = 0):**
$$\dot{m}_{vstup} = \dot{m}_{výstup}$$

**Fyzikální význam:**
- Hmota nemůže vzniknout ani zaniknout
- V uzavřeném systému je celková hmotnost konstantní
- Hmotnostní toky do systému se rovnají hmotnostním tokům ze systému

## Zákon zachování energie

**První termodynamický zákon:**
$$\text{Energie vstupující} - \text{Energie vystupující} = \text{Akumulace energie}$$

**Pro ustálený stav:**
$$\dot{Q}_{vstup} + \dot{W}_{vstup} = \dot{Q}_{výstup} + \dot{W}_{výstup}$$

**Fyzikální význam:**
- Energie nemůže vzniknout ani zaniknout, pouze se přeměňuje
- Celková energie izolovaného systému je konstantní
- Energetická bilance zahrnuje teplo i práci

## Obecná bilance

**Univerzální rovnice bilance:**
$$\text{Vstup} + \text{Výroba} = \text{Výstup} + \text{Spotřeba} + \text{Akumulace}$$

**Aplikace:**
- **Hmotnostní bilance:** Výroba = 0, Spotřeba = 0
- **Energetická bilance:** Energie se nemění na hmotu
- **Látkové bilance:** Pro jednotlivé složky směsi

\newpage

# 4. Měrné tepelné kapacity běžných látek

| Látka | $c_p$ [J/(kg·K)] | Poznámka |
|-------|------------------|----------|
| Voda (kapalná) | 4 186 | Nejvyšší ze společných látek |
| Vzduch | 1 005 | Při konstantním tlaku |
| Led | 2 050 | Při 0°C |
| Vodní pára | 2 010 | Při 100°C |
| Hliník | 897 | Kovy obecně nízká hodnota |
| Měď | 385 | |
| Železo | 449 | |
| Olovo | 129 | |
| Ethanol | 2 440 | |
| Rtuť | 140 | |

**Důležité poznatky:**
- Voda má jednu z nejvyšších měrných tepelných kapacit
- Kovy mají obecně nízké hodnoty $c_p$
- Vyšší $c_p$ znamená větší schopnost akumulovat teplo

\newpage

# 5. Měrná skupenská tepla

## Voda

| Děj | Symbol | Hodnota | Jednotka |
|-----|--------|---------|----------|
| Tání ledu | $l_t$ | 334 000 | J/kg |
| Tuhnutí vody | $l_t$ | 334 000 | J/kg |
| Var vody | $l_v$ | 2 260 000 | J/kg |
| Kondenzace páry | $l_v$ | 2 260 000 | J/kg |

**Fyzikální význam:**
- Skupenské teplo je energie potřebná ke změně skupenství bez změny teploty
- Při varu a kondenzaci se přenáší velké množství energie
- Proto je vodní pára efektivní pro přenos tepla (parní topení)

## Další látky

| Látka | Tání $l_t$ [J/kg] | Var $l_v$ [J/kg] |
|-------|-------------------|------------------|
| Ethanol | 108 000 | 838 000 |
| Hliník | 397 000 | 10 900 000 |
| Olovo | 23 000 | 858 000 |
| Rtuť | 11 800 | 272 000 |

\newpage

# 6. Praktické aplikace

## Výpočet tepla pro ohřev vody

**Bez fázové změny:**
$$Q = m \cdot c_p \cdot \Delta T$$

**Příklad:** Ohřát 2 kg vody z 20°C na 80°C
$$Q = 2 \cdot 4186 \cdot (80-20) = 502{,}320 \text{ J} = 502{,}3 \text{ kJ}$$

## Výpočet výkonu pro var vody

**S fázovou změnou:**
$$\dot{Q} = \dot{m} \cdot (c_p \cdot \Delta T + l_v)$$

**Příklad:** Odpařit 0,1 kg/s vody při 100°C (již horká voda)
$$\dot{Q} = 0{,}1 \cdot 2{,}26 \times 10^6 = 226{,}000 \text{ W} = 226 \text{ kW}$$

## Směšování látek

**Zákon zachování energie při směšování:**
$$m_1 \cdot c_{p1} \cdot (T_1 - T_{výsl}) = m_2 \cdot c_{p2} \cdot (T_{výsl} - T_2)$$

Kde:
- $T_1$ > $T_{výsl}$ > $T_2$
- Teplejší látka odevzdává teplo, chladnější přijímá
- Výsledná teplota $T_{výsl}$ leží mezi $T_1$ a $T_2$

\newpage

# 7. Souhrn jednotek v SI

| Veličina | Jednotka SI | Další jednotky | Převody |
|----------|-------------|----------------|---------|
| Teplota | K (Kelvin) | °C, °F | K = °C + 273,15 |
| Teplo | J (Joule) | kJ, MJ, cal | 1 cal = 4,186 J |
| Tepelný tok | W (Watt) | kW, MW | 1 W = 1 J/s |
| Entalpie | J (Joule) | kJ, MJ | - |
| Hmotnost | kg (kilogram) | g, t | 1 t = 1000 kg |
| Hmotnostní tok | kg/s | kg/h, t/h | 1 kg/h = 0,000278 kg/s |
| Měrná tepelná kapacita | J/(kg·K) | kJ/(kg·K) | - |
| Měrné skupenské teplo | J/kg | kJ/kg, MJ/kg | - |
| Čas | s (sekunda) | min, h | 1 h = 3600 s |

\newpage

# Poznámky

- **Teplota vs. Teplo:** Teplota je stavová veličina (nezávisí na množství), teplo je dějová (závisí na množství)
- **Uzavřený systém:** Systém, který nevyměňuje hmotu s okolím (ale může vyměňovat energii)
- **Izolovaný systém:** Systém, který nevyměňuje ani hmotu, ani energii s okolím
- **Ustálený stav:** Stav, kdy se veličiny v systému nemění v čase (akumulace = 0)
- **Fázová změna:** Změna skupenství probíhá při konstantní teplotě (bod varu, bod tání)
- **Měrná vs. celková veličina:** Měrná veličina je vztažena na jednotku hmotnosti (J/kg), celková na celkové množství (J)
