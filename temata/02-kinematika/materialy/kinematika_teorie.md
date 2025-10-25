---
title: "Kinematika - Teoretický přehled"
subtitle: "Základní teorie, rovnice a jednotky"
author: "Fyzika - opakování a prohloubení"
date: "2025"
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
---

# 1. Základní pojmy

## Pohyb

**Definice:**
> Pohyb je změna polohy tělesa vůči zvolenému vztažnému systému v čase.

**Druhy pohybu:**
- **Přímočarý** - trajektorie je přímka
- **Křivočarý** - trajektorie je křivka
- **Rovnoměrný** - rychlost je konstantní
- **Nerovnoměrný** - rychlost se mění

## Dráha a posunutí

**Dráha (s):**
- **Skalární** veličina
- Délka trajektorie, kterou těleso urazilo
- Jednotka: m (metr)

**Posunutí ($\vec{r}$):**
- **Vektorová** veličina
- Přímá vzdálenost mezi počáteční a koncovou polohou
- Jednotka: m (metr)

## Rychlost

**Průměrná rychlost:**
$$v_p = \frac{s}{t}$$

**Okamžitá rychlost:**
$$v = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t} = \frac{ds}{dt}$$

**Jednotka:** m/s (metr za sekundu)

## Zrychlení

**Definice:**
> Zrychlení je změna rychlosti v čase.

**Rovnice:**
$$a = \frac{\Delta v}{\Delta t} = \frac{v - v_0}{t}$$

**Jednotka:** m/s² (metr za sekundu na druhou)

\newpage

# 2. Rovnoměrný přímočarý pohyb

## Základní rovnice

**Dráha:**
$$s = v \cdot t$$

**Rychlost:**
$$v = \text{konstantní}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $s$ | Dráha | m |
| $v$ | Rychlost | m/s |
| $t$ | Čas | s |

**Grafické znázornění:**
- **Graf s(t):** Přímka procházející počátkem (při $s_0 = 0$)
- **Graf v(t):** Vodorovná přímka (konstantní rychlost)
- **Graf a(t):** Nulová hodnota (žádné zrychlení)

\newpage

# 3. Rovnoměrně zrychlený pohyb

## Kinematické rovnice

**Rychlost:**
$$v = v_0 + a \cdot t$$

**Dráha (se začáteční rychlostí):**
$$s = v_0 \cdot t + \frac{1}{2} a \cdot t^2$$

**Dráha (bez času):**
$$v^2 = v_0^2 + 2 a \cdot s$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $v$ | Koncová rychlost | m/s |
| $v_0$ | Počáteční rychlost | m/s |
| $a$ | Zrychlení | m/s² |
| $t$ | Čas | s |
| $s$ | Dráha | m |

**Grafické znázornění:**
- **Graf s(t):** Parabola
- **Graf v(t):** Přímka se sklonem $a$
- **Graf a(t):** Vodorovná přímka (konstantní zrychlení)

## Speciální případy

**Rozjezd z klidu ($v_0 = 0$):**
$$s = \frac{1}{2} a \cdot t^2$$
$$v = a \cdot t$$
$$v^2 = 2 a \cdot s$$

**Brzdění do zastavení ($v = 0$):**
$$0 = v_0 + a \cdot t \quad \Rightarrow \quad t = -\frac{v_0}{a}$$
$$s = v_0 \cdot t + \frac{1}{2} a \cdot t^2 = \frac{v_0^2}{2|a|}$$

\newpage

# 4. Volný pád

## Základní rovnice

**Výška:**
$$h = \frac{1}{2} g \cdot t^2$$

**Rychlost:**
$$v = g \cdot t$$

**Rychlost bez času:**
$$v^2 = 2 g \cdot h$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $h$ | Výška | m |
| $v$ | Rychlost | m/s |
| $g$ | Gravitační zrychlení | m/s² |
| $t$ | Čas | s |

**Fyzikální význam:**
- Volný pád je speciální případ rovnoměrně zrychleného pohybu
- Zrychlení $a = g = 9{,}81$ m/s² (na Zemi)
- Zanedbáváme odpor vzduchu

\newpage

# 5. Vrhy

## Svislý vrh vzhůru

**Výška:**
$$y = v_0 \cdot t - \frac{1}{2} g \cdot t^2$$

**Rychlost:**
$$v_y = v_0 - g \cdot t$$

**Maximální výška:**
$$h_{max} = \frac{v_0^2}{2g}$$

**Doba výstupu (do maximální výšky):**
$$t_{max} = \frac{v_0}{g}$$

**Doba letu (celková):**
$$t_{celk} = \frac{2v_0}{g}$$

## Vodorovný vrh

**Vodorovná složka:**
$$x = v_0 \cdot t$$
$$v_x = v_0 = \text{konstantní}$$

**Svislá složka:**
$$y = -\frac{1}{2} g \cdot t^2$$
$$v_y = -g \cdot t$$

**Trajektorie:**
$$y = -\frac{g}{2v_0^2} \cdot x^2$$ (parabola)

**Dopad na zem (z výšky $h$):**
$$t = \sqrt{\frac{2h}{g}}$$
$$x = v_0 \cdot \sqrt{\frac{2h}{g}}$$

## Vrh šikmo vzhůru

**Rozklad počáteční rychlosti:**
$$v_x = v_0 \cos \alpha$$
$$v_y = v_0 \sin \alpha$$

**Pohybové rovnice:**
$$x = v_0 \cos \alpha \cdot t$$
$$y = v_0 \sin \alpha \cdot t - \frac{1}{2} g \cdot t^2$$

**Trajektorie:**
$$y = x \tan \alpha - \frac{g x^2}{2 v_0^2 \cos^2 \alpha}$$

**Dosah (R):**
$$R = \frac{v_0^2 \sin 2\alpha}{g}$$

**Maximální výška:**
$$h_{max} = \frac{v_0^2 \sin^2 \alpha}{2g}$$

**Doba letu:**
$$t_{celk} = \frac{2v_0 \sin \alpha}{g}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $v_0$ | Počáteční rychlost | m/s |
| $\alpha$ | Úhel vrhu | ° nebo rad |
| $v_x, v_y$ | Složky rychlosti | m/s |
| $R$ | Dosah | m |
| $h_{max}$ | Maximální výška | m |

\newpage

# 6. Pohyb po kružnici

## Základní veličiny

**Úhlová rychlost:**
$$\omega = \frac{2\pi}{T} = 2\pi f = \frac{\varphi}{t}$$

**Obvodová rychlost:**
$$v = \omega \cdot r = \frac{2\pi r}{T}$$

**Perioda:**
$$T = \frac{2\pi}{\omega} = \frac{1}{f}$$

**Frekvence:**
$$f = \frac{1}{T} = \frac{\omega}{2\pi}$$

**Popis veličin:**

| Veličina | Popis | Jednotka |
|----------|-------|----------|
| $\omega$ | Úhlová rychlost | rad/s |
| $v$ | Obvodová rychlost | m/s |
| $r$ | Poloměr | m |
| $T$ | Perioda | s |
| $f$ | Frekvence | Hz |
| $\varphi$ | Úhel | rad |

## Dostředivé zrychlení a síla

**Dostředivé zrychlení:**
$$a_d = \frac{v^2}{r} = \omega^2 \cdot r$$

**Dostředivá síla:**
$$F_d = m \cdot a_d = \frac{m v^2}{r} = m \omega^2 \cdot r$$

**Fyzikální význam:**
- Dostředivé zrychlení směřuje k středu kružnice
- Dostředivá síla je výslednice všech sil, které udržují těleso na kruhové dráze
- Tato síla neprovádí práci (je kolmá na rychlost)

\newpage

# 7. Převody jednotek rychlosti

## Základní převody

**km/h ↔ m/s:**
$$1 \text{ km/h} = \frac{1000 \text{ m}}{3600 \text{ s}} = \frac{1}{3{,}6} \text{ m/s} \approx 0{,}278 \text{ m/s}$$

$$1 \text{ m/s} = 3{,}6 \text{ km/h}$$

**Praktický vzorec:**
$$v[\text{m/s}] = \frac{v[\text{km/h}]}{3{,}6}$$
$$v[\text{km/h}] = v[\text{m/s}] \times 3{,}6$$

## Příklady převodů

| km/h | m/s | Poznámka |
|------|-----|----------|
| 36 | 10 | Běžná rychlost ve městě |
| 50 | 13,9 | Rychlost ve městě |
| 90 | 25 | Rychlost mimo obec |
| 130 | 36,1 | Maximální rychlost na dálnici |
| 360 | 100 | Vysoká rychlost |

\newpage

# 8. Fyzikální konstanty

| Konstanta | Symbol | Hodnota | Jednotka |
|-----------|--------|---------|----------|
| Gravitační zrychlení (Země) | $g$ | 9,81 | m/s² |
| Gravitační zrychlení (Měsíc) | $g_M$ | 1,62 | m/s² |
| Rychlost světla ve vakuu | $c$ | 299 792 458 | m/s |
| Rychlost zvuku ve vzduchu (20°C) | $v_{zvuk}$ | 343 | m/s |

\newpage

# 9. Souhrn jednotek v SI

| Veličina | Jednotka SI | Další jednotky | Převody |
|----------|-------------|----------------|---------|
| Dráha, posunutí | m (metr) | km, cm, mm | 1 km = 1000 m |
| Rychlost | m/s | km/h | 1 m/s = 3,6 km/h |
| Zrychlení | m/s² | - | - |
| Čas | s (sekunda) | min, h | 1 h = 3600 s |
| Úhel | rad (radián) | °  (stupeň) | 1 rad = 57,3° |
| Úhlová rychlost | rad/s | °/s, ot/min | 1 ot/min = 0,105 rad/s |
| Frekvence | Hz (Hertz) | ot/min | 1 Hz = 1/s |
| Perioda | s (sekunda) | min | T = 1/f |

\newpage

# Poznámky

- **Trajektorie:** Křivka, po které se těleso pohybuje
- **Vztažný systém:** Soustava souřadnic, vůči které měříme pohyb
- **Vektor vs. skalár:** Vektor má velikost i směr (posunutí, rychlost, zrychlení), skalár má jen velikost (dráha, rychlost v absolutní hodnotě, čas)
- **Pohyb je relativní:** Závisí na volbě vztažného systému (v jednom může být těleso v klidu, v jiném se pohybuje)
- **Grafická analýza:** Z grafu s(t) lze určit rychlost (směrnice tečny), z grafu v(t) lze určit zrychlení (směrnice) a dráhu (obsah pod křivkou)
- **Optimální úhel vrhu:** Pro maximální dosah je optimální úhel 45° (při vrhu ze stejné výšky na stejnou výšku)
- **Kruhový pohyb:** I při konstantní velikosti rychlosti se mění směr → existuje zrychlení (dostředivé)
