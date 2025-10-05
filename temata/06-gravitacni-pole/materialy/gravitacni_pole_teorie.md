---
title: "Gravitační pole - Teoretický přehled"
subtitle: "Základní teorie, rovnice a jednotky"
author: "Fyzika - opakování a prohloubení"
date: "2025"
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
---

# 1. Newtonův gravitační zákon

## Zákon univerzální gravitace

**Rovnice:**
$$F_g = \kappa \frac{m_1 m_2}{r^2}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $F_g$ | Gravitační síla | N (newton) |
| $\kappa$ | Gravitační konstanta | N·m²·kg⁻² |
| $m_1, m_2$ | Hmotnosti těles | kg (kilogram) |
| $r$ | Vzdálenost středů těles | m (metr) |

**Hodnota gravitační konstanty:**
$$\kappa = 6,674 \times 10^{-11} \text{ N·m}^2\text{·kg}^{-2}$$

**Důležité vlastnosti:**

- Gravitační síla je vždy **přitažlivá**
- Síla klesá s **druhou mocninou** vzdálenosti
- Síla působí podél spojnice středů těles
- Gravitace je **univerzální** - působí mezi všemi tělesy s hmotností

\newpage

# 2. Gravitační pole

## Intenzita gravitačního pole

**Rovnice:**
$$K = \frac{F_g}{m} = \kappa \frac{M}{r^2}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $K$ | Intenzita gravitačního pole | N/kg nebo m/s² |
| $F_g$ | Gravitační síla | N |
| $m$ | Hmotnost zkušebního tělesa | kg |
| $M$ | Hmotnost tělesa vytvářejícího pole | kg |
| $r$ | Vzdálenost od středu pole | m |

**Fyzikální význam:**

- Intenzita pole udává **sílu na jednotku hmotnosti**
- Číselně rovna **gravitačnímu zrychlení** v daném místě
- Nezávisí na hmotnosti zkušebního tělesa

## Gravitační zrychlení

**Rovnice:**
$$a_g = K = \kappa \frac{M}{r^2}$$

**Na povrchu Země:**
$$g = \kappa \frac{M_Z}{R_Z^2} \approx 9,81 \text{ m/s}^2$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $a_g$ | Gravitační zrychlení | m/s² |
| $g$ | Tíhové zrychlení na Zemi | m/s² |
| $M_Z$ | Hmotnost Země | kg |
| $R_Z$ | Poloměr Země | m |

\newpage

# 3. Gravitační potenciál

**Rovnice:**
$$\varphi = -\kappa \frac{M}{r}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $\varphi$ | Gravitační potenciál | J/kg |
| $M$ | Hmotnost tělesa | kg |
| $r$ | Vzdálenost od středu | m |

**Fyzikální význam:**

- Potenciál je **záporný** (gravitace je přitažlivá síla)
- Udává **práci na jednotku hmotnosti** potřebnou k přenesení tělesa z daného místa do nekonečna
- Souvisí s potenciální energií: $E_p = m\varphi$

\newpage

# 4. Kosmické rychlosti

## Kruhová rychlost (1. kosmická rychlost)

**Rovnice:**
$$v_k = \sqrt{\kappa \frac{M}{r}}$$

**Pro nízké oběžné dráhy kolem Země:**
$$v_k \approx 7,9 \text{ km/s}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $v_k$ | Kruhová rychlost | m/s |
| $M$ | Hmotnost centrálního tělesa | kg |
| $r$ | Poloměr oběžné dráhy | m |

**Fyzikální význam:**

- Rychlost potřebná pro **kruhovou oběžnou dráhu**
- Dostředivá síla se rovná gravitační síle
- Pro nízké dráhy kolem Země: $v_k \approx 7,9$ km/s

## Úniková rychlost (2. kosmická rychlost)

**Rovnice:**
$$v_u = \sqrt{2\kappa \frac{M}{r}} = v_k\sqrt{2}$$

**Z povrchu Země:**
$$v_u \approx 11,2 \text{ km/s}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $v_u$ | Úniková rychlost | m/s |
| $M$ | Hmotnost tělesa | kg |
| $r$ | Vzdálenost od středu tělesa | m |

**Fyzikální význam:**

- Minimální rychlost k **opuštění gravitačního pole**
- Kinetická energie se rovná potenciální energii
- Úniková rychlost je $\sqrt{2}$-krát větší než kruhová rychlost

## Další kosmické rychlosti

**3. kosmická rychlost** (únik ze Sluneční soustavy):
$$v_3 \approx 16,7 \text{ km/s}$$

**4. kosmická rychlost** (únik z Galaxie):
$$v_4 \approx 525 \text{ km/s}$$

\newpage

# 5. Keplerovy zákony

## 1. Keplerův zákon (zákon elips)

**Formulace:**

> Planety se pohybují po **elipsách**, v jejichž jednom **ohnisku** je Slunce.

**Matematický popis:**

- Dráha planety je elipsa s hlavní poloosou $a$ a vedlejší poloosou $b$
- Slunce je v jednom z ohnisek elipsy
- Vzdálenost mezi ohnisky: $2c$, kde $c = \sqrt{a^2 - b^2}$

## 2. Keplerův zákon (zákon ploch)

**Formulace:**

> Plocha opsaná **průvodičem** planety je za stejný čas **stejná**.

**Fyzikální důsledek:**

- Planeta se pohybuje **rychleji**, když je blíže Slunci (v **perihelu**)
- Planeta se pohybuje **pomaleji**, když je dále od Slunce (v **afelu**)
- Zachování **momentu hybnosti**

## 3. Keplerův zákon (harmonický zákon)

**Rovnice:**
$$\frac{T_1^2}{T_2^2} = \frac{a_1^3}{a_2^3}$$

nebo pro jednu planetu:
$$T^2 = \frac{4\pi^2}{GM} a^3$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $T$ | Oběžná doba planety | s (sekunda) |
| $a$ | Hlavní poloosa dráhy | m |
| $G$ | Gravitační konstanta ($\kappa$) | N·m²·kg⁻² |
| $M$ | Hmotnost centrálního tělesa | kg |

**Fyzikální význam:**

- Druhá mocnina oběžné doby je úměrná třetí mocnině hlavní poloosy
- Platí pro všechna tělesa obíhající kolem stejného centrálního tělesa

\newpage

# 6. Fyzikální konstanty

| Konstanta | Symbol | Hodnota | Jednotka |
|-----------|--------|---------|----------|
| Gravitační konstanta | $\kappa$ nebo $G$ | $6,674 \times 10^{-11}$ | N·m²·kg⁻² |
| Hmotnost Země | $M_Z$ | $5,972 \times 10^{24}$ | kg |
| Poloměr Země | $R_Z$ | $6,371 \times 10^{6}$ | m |
| Hmotnost Slunce | $M_S$ | $1,989 \times 10^{30}$ | kg |
| Hmotnost Měsíce | $M_M$ | $7,342 \times 10^{22}$ | kg |
| Vzdálenost Země-Měsíc | $r_{ZM}$ | $3,844 \times 10^{8}$ | m |
| Tíhové zrychlení na Zemi | $g$ | $9,81$ | m/s² |

\newpage

# 7. Užitečné vztahy a vzorce

## Energie v gravitačním poli

**Potenciální energie:**
$$E_p = -\kappa \frac{Mm}{r}$$

**Kinetická energie kruhové oběžné dráhy:**
$$E_k = \frac{1}{2}mv_k^2 = \kappa \frac{Mm}{2r}$$

**Celková mechanická energie:**
$$E = E_k + E_p = -\kappa \frac{Mm}{2r}$$

## Vztah mezi zrychlením a výškou

**Gravitační zrychlení ve výšce $h$ nad povrchem:**
$$g_h = g \frac{R^2}{(R+h)^2}$$

kde:
- $g$ je tíhové zrychlení na povrchu
- $R$ je poloměr tělesa
- $h$ je výška nad povrchem

## Podmínky pro oběžné dráhy

**Kruhová dráha:**
$$F_g = F_{ds} \quad \Rightarrow \quad \kappa \frac{Mm}{r^2} = m\frac{v^2}{r}$$

**Eliptická dráha:**
$$v_k < v < v_u$$

**Únik z gravitačního pole:**
$$v \geq v_u$$

\newpage

# 8. Souhrn jednotek v SI

| Veličina | Jednotka SI | Další jednotky |
|----------|-------------|----------------|
| Síla | N (newton) | kg·m/s² |
| Hmotnost | kg (kilogram) | - |
| Vzdálenost | m (metr) | km = 10³ m |
| Rychlost | m/s | km/s, km/h |
| Zrychlení | m/s² | - |
| Energie | J (joule) | N·m, kg·m²/s² |
| Potenciál | J/kg | m²/s² |
| Intenzita pole | N/kg | m/s² |
| Čas | s (sekunda) | h (hodina), den, rok |

\newpage

# Poznámky

- Všechny vzorce předpokládají **bodové hmotnosti** nebo **kulově symetrická tělesa**
- Vzdálenost $r$ se měří od **středu těles**
- V reálných situacích může být třeba zohlednit **atmosféru** a **odpor vzduchu**
- Pro velmi přesné výpočty je nutné použít **relativistickou mechaniku**
