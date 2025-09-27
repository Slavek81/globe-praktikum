# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## KRITICKÝ POŽADAVEK NA PŘESNOST - ABSOLUTNĚ STEJNÝ STYL

### POVINNÉ NÁSTROJE PRO KAŽDÝ ÚKOL
- **sage-mcp**: Konzultace s o3 a gemini-2.5-pro modely pro složitější úkoly
- **browsermcp-enhanced**: Kontrola a testování HTML souborů, screenshoty
- **sequential-thinking**: Přemýšlení o zadaném úkolu před implementací
- **TodoWrite**: Před každým úkolem vytvořit todo list s konkrétními úkoly

### PEDAGOGICKÉ HTML SOUBORY - NEPORUŠITELNÁ PRAVIDLA

#### ABSOLUTNĚ STEJNÝ STYL
Jednotlivé sekce MUSÍ mít **100% identický CSS styl** 
- ❌ **ŽÁDNÉ odchylky** v barvách, rozestupech, fontech nebo struktuře
- ✅ **PŘESNÉ kopírování** všech CSS tříd a jejich vlastností
- ✅ **IDENTICKÁ struktura** HTML elementů

#### MATEMATICKÝ ZÁPIS - POVINNÝ
- ❌ **NIKDY prostý text** pro matematické vzorce
- ✅ **VŽDY KaTeX nebo MathJax** pro všechny rovnice a vzorce
- ✅ **Správné matematické značení** (m·s⁻¹, km·h⁻¹, atd.)

#### KONTROLNÍ PROCES - POVINNÝ PŘED DOKONČENÍM
Před označením jakéhokoli HTML souboru za dokončený MUSÍM:

1. **🧠 Sequential-thinking**: Analyzovat úkol před začátkem práce
2. **📋 TodoWrite**: Vytvořit konkrétní todo list s kroky
3. **💬 Sage-mcp**: Konzultovat složitější části s AI modely
4. **📱 Screenshot test**: Browsermcp-enhanced screenshot vzoru vs. mého souboru
5. **🔍 Vizuální porovnání**: Pixel-perfect shoda v rozložení a barvách
6. **⚙️ Funkční test**: Všechny toggle a interaktivní prvky fungují
7. **📐 Matematika test**: Všechny vzorce renderovány matematicky
8. **✅ Označit dokončené**: Teprve po 100% shodě označit za hotové

#### FAILSAFE - "NEFUNGUJE DOKUD NEVIDÍM ŽE FUNGUJE"
- **Žádné dohady** - pouze to co vidím na screenshotu
- **Screenshot POVINNÝ** při každé změně HTML souboru
- **TODO tracking** - každý příklad označit až po kompletní kontrole

**PRAVIDLO**: HTML soubor označit za dokončený pouze po splnění všech 8 kontrolních kritérií!

## Project Overview

This is a static educational website for "Praktické aplikace fyziky a chemie" (Practical Applications of Physics and Chemistry) course at Gymnázium Globe. The site provides lectures, semester projects, and educational materials for students.

## Architecture

### Content Structure
- **Root**: Main landing page (`index.html`) with course overview
- **`temata/`**: Individual lecture topics, each in numbered directories (e.g., `00-umela-inteligence/`, `01-matematicke-praktikum/`)
- **`projekty/`**: Semester projects with both HTML pages and markdown documentation
- **`css/`**: Stylesheets (`main.css` for main styles, `apps.css` for applications)
- **`js/`**: JavaScript functionality (`main.js` for interactions)

### Navigation Architecture
- Each topic directory contains an `index.html` with relative paths back to root (`../../css/main.css`)
- Project pages use relative paths (`../css/main.css`)
- Consistent header structure across all pages with breadcrumb navigation

### Design System
The site uses a modern design system built with CSS custom properties:
- **Colors**: Primary (`#2563eb`), secondary (`#10b981`), accent (`#f59e0b`)
- **Typography**: Inter font family from Google Fonts
- **Layout**: CSS Grid and Flexbox with consistent spacing variables
- **Icons**: Font Awesome 6.4.0 for visual elements

## Development Guidelines

### File Organization
- Topic numbering: `00-`, `01-`, `02-`, etc. for proper ordering
- Consistent naming: kebab-case for directories and files
- Each topic must have an `index.html` file
- Projects use both `.html` and `.md` formats

### CSS Architecture
- CSS custom properties defined in `:root` for theming
- Mobile-first responsive design
- Consistent component classes (`.lecture-card`, `.project-card`, etc.)
- Smooth animations and hover effects throughout

### JavaScript Functionality
- Smooth scrolling navigation
- Mobile menu toggle
- Scroll-based active navigation highlighting
- Animated statistics counters
- Card hover animations

### Content Management
- Course topics are managed through numbered directories in `temata/`
- Project descriptions in markdown format with corresponding HTML presentations
- All paths are relative to maintain portability

### Browser Testing
When making changes to the UI:
1. Test navigation between pages
2. Verify responsive design on mobile devices
3. Check that all relative paths work correctly
4. Ensure smooth scrolling and animations function properly

### Adding New Topics
1. Create numbered directory in `temata/` (e.g., `05-new-topic/`)
2. Add corresponding lecture card in main `index.html`
3. Update README.md with new topic count and description
4. Ensure consistent styling and navigation

### Adding New Projects
1. Create markdown file in `projekty/` directory
2. Add project card to `projekty.html` or main page
3. Follow existing project structure with stats and technical tags
4. Include ROI calculations and practical applications where applicable

This is a pure frontend project with no build process, package management, or testing framework - all development is done directly with HTML, CSS, and vanilla JavaScript.