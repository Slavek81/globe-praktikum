---
title: "Mechanická práce a energie - Teoretický přehled"
subtitle: "Základní teorie, rovnice a jednotky"
author: "Fyzika - opakování a prohloubení"
date: "2025"
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
---

# 1. Mechanická práce

## Definice

**Obecná definice:**
> Mechanická práce je energie přenesená silou, která působí na těleso po určité dráze.

**Rovnice:**
$$W = F \cdot s \cdot \cos\alpha$$

**Speciální případy:**
- $\alpha = 0°$ (síla ve směru pohybu): $W = F \cdot s$
- $\alpha = 90°$ (síla kolmá k pohybu): $W = 0$
- $\alpha = 180°$ (síla proti pohybu): $W = -F \cdot s$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $W$ | Mechanická práce | J (Joule) |
| $F$ | Síla | N |
| $s$ | Dráha | m |
| $\alpha$ | Úhel mezi silou a dráhou | ° nebo rad |

**Fyzikální význam:**
- Práce je skalární veličina (může být kladná, záporná i nulová)
- Kladná práce: síla koná práci (přidává energii)
- Záporná práce: síla brzdí (odebírá energii)
- Nulová práce: síla nekoná práci (kolmá k pohybu)

\newpage

# 2. Výkon

## Průměrný výkon

**Definice:**
> Průměrný výkon je práce vykonaná za jednotku času.

**Rovnice:**
$$P_p = \frac{W}{t}$$

## Okamžitý výkon

**Rovnice:**
$$P = F \cdot v$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $P$ | Výkon | W (Watt) |
| $W$ | Práce | J |
| $t$ | Čas | s |
| $F$ | Síla | N |
| $v$ | Rychlost | m/s |

**Jednotka:**
- 1 W (Watt) = 1 J/s
- 1 kW = 1000 W
- 1 MW = 1 000 000 W

## Účinnost

**Definice:**
> Účinnost vyjadřuje poměr užitečné energie (výkonu) k celkové dodané energii (výkonu).

**Rovnice:**
$$\eta = \frac{P_{výst}}{P_{vst}} = \frac{W_{výst}}{W_{vst}}$$

**Vyjádření:**
- V desetinném tvaru: $0 < \eta < 1$
- V procentech: $0\% < \eta < 100\%$

**Fyzikální význam:**
- Vždy $\eta < 1$ (nebo $\eta < 100\%$)
- Část energie se vždy ztratí (nejčastěji jako teplo třením)
- Ideální stroj by měl $\eta = 1$ (neexistuje)

\newpage

# 3. Mechanická energie

## Kinetická energie

**Definice:**
> Kinetická energie je energie pohybujícího se tělesa.

**Rovnice:**
$$E_k = \frac{1}{2}mv^2$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $E_k$ | Kinetická energie | J |
| $m$ | Hmotnost | kg |
| $v$ | Rychlost | m/s |

**Fyzikální význam:**
- Závisí na druhé mocnině rychlosti
- Zdvojnásobení rychlosti → zčtyřnásobení energie
- Vždy kladná hodnota (rychlost je na druhou)

## Potenciální energie

**Definice:**
> Potenciální energie je energie polohy tělesa v gravitačním poli.

**Rovnice:**
$$E_p = mgh$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $E_p$ | Potenciální energie | J |
| $m$ | Hmotnost | kg |
| $g$ | Tíhové zrychlení | m/s² |
| $h$ | Výška nad referenční hladinou | m |

**Fyzikální význam:**
- Závisí na výběru nulové hladiny (referenční úrovně)
- Čím výše, tím větší potenciální energie
- Při pádu se mění na kinetickou energii

## Celková mechanická energie

**Rovnice:**
$$E = E_k + E_p = \frac{1}{2}mv^2 + mgh$$

\newpage

# 4. Zákony zachování

## Zákon zachování mechanické energie

**Formulace:**
> V konzervativním systému (bez třecích sil) zůstává celková mechanická energie konstantní.

**Rovnice:**
$$E_k + E_p = \text{konst.}$$

$$\frac{1}{2}mv^2 + mgh = \text{konst.}$$

**Aplikace na volný pád:**

V nejvyšším bodě (h = $h_{max}$, v = 0):
$$E = E_p = mgh_{max}$$

Při dopadu (h = 0, v = $v_{max}$):
$$E = E_k = \frac{1}{2}mv_{max}^2$$

**Rovnost:**
$$mgh_{max} = \frac{1}{2}mv_{max}^2$$

**Rychlost při volném pádu:**
$$v = \sqrt{2gh}$$

## Zákon zachování hybnosti

**Formulace:**
> V izolované soustavě je celková hybnost konstantní.

**Rovnice:**
$$\vec{p}_{před} = \vec{p}_{po}$$

Pro dvě tělesa:
$$m_1\vec{v}_1 + m_2\vec{v}_2 = m_1\vec{v}'_1 + m_2\vec{v}'_2$$

**Aplikace:**
- Srážky těles
- Výbuch
- Raketový pohon

**Důležité:**
- Platí vždy (i při nepružných srážkách)
- Zachovává se i v případech, kdy se nezachovává mechanická energie

\newpage

# 5. Druhy srážek

## Pružná srážka

**Charakteristika:**
- Zachovává se hybnost
- Zachovává se kinetická energie
- Dokonale pružné tělesa (idealizace)

**Zákony:**
$$m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2$$
$$\frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2 = \frac{1}{2}m_1v'^2_1 + \frac{1}{2}m_2v'^2_2$$

## Nepružná srážka

**Charakteristika:**
- Zachovává se hybnost
- Nezachovává se kinetická energie (část se mění na teplo, deformaci)
- Reálné srážky

**Zákon:**
$$m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2$$

**Dokonale nepružná srážka:**
- Tělesa se po srážce spojí
- Pohybují se společnou rychlostí

$$m_1v_1 + m_2v_2 = (m_1 + m_2)v'$$

\newpage

# 6. Praktické vztahy

## Vztah mezi prací a energií

**Práce jako změna kinetické energie:**
$$W = \Delta E_k = \frac{1}{2}mv^2 - \frac{1}{2}mv_0^2$$

**Práce tíhové síly:**
$$W_g = -\Delta E_p = -(mgh_2 - mgh_1) = mg(h_1 - h_2)$$

## Brzdná dráha

**Z kinetické energie:**
$$E_k = W_{tření}$$
$$\frac{1}{2}mv^2 = F_t \cdot s$$
$$s = \frac{mv^2}{2F_t} = \frac{v^2}{2a}$$

Kde $a = F_t/m$ je brzdné zrychlení.

**Závislost na rychlosti:**
- Zdvojnásobení rychlosti → zčtyřnásobení brzdné dráhy
- Proto je rychlost kritická pro bezpečnost

\newpage

# 7. Fyzikální konstanty

| Konstanta | Symbol | Hodnota | Jednotka |
|-----------|--------|---------|----------|
| Tíhové zrychlení (Země) | $g$ | 9,81 | m/s² |
| Tíhové zrychlení (Měsíc) | $g_M$ | 1,62 | m/s² |

\newpage

# 8. Souhrn jednotek v SI

| Veličina | Jednotka SI | Odvození | Poznámka |
|----------|-------------|----------|----------|
| Práce | J (Joule) | N·m = kg·m²/s² | 1 J = práce síly 1 N po dráze 1 m |
| Energie | J (Joule) | N·m = kg·m²/s² | Stejná jako práce |
| Výkon | W (Watt) | J/s = kg·m²/s³ | 1 W = 1 J/s |
| Účinnost | - | - | Bezrozměrná veličina (0-1 nebo 0-100%) |

**Běžné násobky:**
- 1 kJ = 1000 J
- 1 MJ = 1 000 000 J
- 1 kW = 1000 W
- 1 MW = 1 000 000 W
- 1 kWh = 3 600 000 J = 3,6 MJ

\newpage

# Poznámky

- **Konzervativní síla:** Síla, u které práce nezávisí na dráze, ale jen na počáteční a koncové poloze (gravitační síla, elektrická síla)
- **Nekonzervativní síla:** Síla, u které práce závisí na dráze (třecí síla)
- **Energetická bilance:** Součet všech energií zůstává konstantní (ale může se měnit forma energie)
- **Práce a teplo:** Jsou to formy přenosu energie, ne druhy energie
- **Perpetuum mobile:** Stroj s účinností 100% nebo větší - neexistuje (porušoval by termodynamické zákony)
- **Vztah práce a výkonu:** Stejná práce může být vykonána s různým výkonem (záleží na čase)
- **Elastická potenciální energie:** $E_{pel} = \frac{1}{2}kx^2$ (pružina, kde k je tuhost a x je prodloužení)
