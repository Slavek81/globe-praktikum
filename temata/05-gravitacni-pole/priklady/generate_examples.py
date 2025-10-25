#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatické generování HTML souborů example_04.html až example_14.html
ze zdrojového souboru gravitacni_pole_zadani_reseni.html
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

# Cesta k souborům
base_dir = Path(__file__).parent
source_file = base_dir / "gravitacni_pole_zadani_reseni.html"

# Přečteme zdrojový HTML soubor
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# HTML template
html_template = '''<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- MathJax konfigurace pro správné zobrazování matematických vzorců -->
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true,
                processEnvironments: true
            }},
            options: {{
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }}
        }};
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <link rel="stylesheet" href="unified-style.css">
</head>
<body>
    <main>
        <header>
            <h1>{number}. {title}</h1>
            <p>Gravitační pole - řešený příklad</p>
        </header>

        <!-- Motivační úvod pro studenty -->
        <div class="intro-context">
            <strong>💡 Praktická aplikace:</strong> {motivation}
        </div>

        <section id="zadani">
            <h2>Zadání úlohy</h2>
            <div class="zadani-text">
