// Kvíz funkce
function checkAnswer(event, questionId, selectedAnswer, isCorrect) {
    const resultElement = document.getElementById(questionId + '-result');
    const options = document.querySelectorAll(`#${questionId.replace('q', '')} .quiz-option`);

    // Reset všech možností
    options.forEach(option => {
        option.classList.remove('correct', 'incorrect');
    });

    // Označit vybranou odpověď
    event.target.classList.add(isCorrect ? 'correct' : 'incorrect');

    // Zobrazit výsledek
    resultElement.classList.remove('result-success', 'result-error');
    if (isCorrect) {
        resultElement.innerHTML = '<span style="color: #16a34a;"><i class="fas fa-check"></i> Správně!</span>';
        resultElement.classList.add('result-success');
    } else {
        resultElement.innerHTML = '<span style="color: #dc2626;"><i class="fas fa-times"></i> Zkus to znovu.</span>';
        resultElement.classList.add('result-error');
    }
}

// Etika accordion
function toggleEthics(id) {
    const content = document.getElementById(id);
    const header = content.previousElementSibling;
    const icon = header.querySelector('i');

    content.classList.toggle('active');
    icon.classList.toggle('fa-chevron-down');
    icon.classList.toggle('fa-chevron-up');
}

// Demo generování básně s analýzou promptu
function generatePoem() {
    const input = document.getElementById('prompt-input').value;
    const output = document.getElementById('poem-output');
    const analysisDiv = document.getElementById('prompt-analysis');
    const analysisContent = document.getElementById('analysis-content');

    if (!input.trim()) {
        output.innerHTML = '<em style="color: #dc2626;">Nejdřív zadejte prompt!</em>';
        analysisDiv.style.display = 'none';
        return;
    }

    // Analýza promptu
    const analysis = analyzePrompt(input);

    // Simulace AI odpovědi (v reálné aplikaci by se volalo API)
    const poems = [
        "Gravitace táhne dolů,<br>Icaro letěl moc vysoko.<br>Newton pod stromenem seděl,<br>Jablko mu na hlavu kleslo!",
        "F = ma, to je zákon,<br>Newton nám ho napsal v knihách.<br>Síla, hmota, zrychlení,<br>Fyzika je úžasná!",
        "Einstein řekl E=mc²,<br>Hmota je energie v kořeni.<br>Čas se kroutí, prostor taky,<br>Relativita - to jsou fajn zákony!"
    ];

    const randomPoem = poems[Math.floor(Math.random() * poems.length)];

    output.innerHTML = `
        <strong>Vygenerovaná báseň:</strong><br><br>
        <em>${randomPoem}</em>
        <br><br>
        <small><i class="fas fa-lightbulb"></i> V reálné aplikaci by tuto báseň vygenerovala AI na základě vašeho promptu.</small>
    `;

    // Zobrazení analýzy
    analysisContent.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div>
                <strong>📏 Délka:</strong><br>
                ${analysis.wordCount} slov, ${analysis.tokenEstimate} tokenů (odhad)
            </div>
            <div>
                <strong>🎯 Konkrétnost:</strong><br>
                <span style="color: ${analysis.specificity.color};">${analysis.specificity.level}</span>
            </div>
            <div>
                <strong>👤 Role definována:</strong><br>
                <span style="color: ${analysis.hasRole ? '#16a34a' : '#dc2626'};">${analysis.hasRole ? 'Ano' : 'Ne'}</span>
            </div>
            <div>
                <strong>📋 Formát zadán:</strong><br>
                <span style="color: ${analysis.hasFormat ? '#16a34a' : '#dc2626'};">${analysis.hasFormat ? 'Ano' : 'Ne'}</span>
            </div>
        </div>
        <div style="margin-top: 1rem;">
            <strong>💡 Doporučení:</strong> ${analysis.suggestions.join(', ')}
        </div>
    `;

    analysisDiv.style.display = 'block';
}

// Funkce pro analýzu promptu
function analyzePrompt(prompt) {
    const words = prompt.trim().split(/\s+/);
    const wordCount = words.length;
    const tokenEstimate = Math.ceil(wordCount * 1.3); // Hrubý odhad

    // Kontrola konkrétnosti
    const specificWords = ['konkrétní', 'detailní', 'přesný', 'specifický', 'pro', 'věk', 'úroveň', 'školu'];
    const hasSpecificWords = specificWords.some(word => prompt.toLowerCase().includes(word));

    let specificity = { level: 'Nízká', color: '#dc2626' };
    if (wordCount > 15 && hasSpecificWords) {
        specificity = { level: 'Vysoká', color: '#16a34a' };
    } else if (wordCount > 10 || hasSpecificWords) {
        specificity = { level: 'Střední', color: '#f59e0b' };
    }

    // Kontrola role
    const roleWords = ['jsi', 'jste', 'jako', 'expert', 'učitel', 'student', 'básník', 'spisovatel'];
    const hasRole = roleWords.some(word => prompt.toLowerCase().includes(word));

    // Kontrola formátu
    const formatWords = ['verš', 'řádek', 'bod', 'seznam', 'krátký', 'dlouhý', 'stránka', 'odstavec', 'rým'];
    const hasFormat = formatWords.some(word => prompt.toLowerCase().includes(word));

    // Doporučení
    const suggestions = [];
    if (!hasRole) suggestions.push('Definujte roli AI (např. "Jsi básník...")');
    if (!hasFormat) suggestions.push('Specifikujte formát výstupu');
    if (wordCount < 10) suggestions.push('Buďte konkrétnější v zadání');
    if (suggestions.length === 0) suggestions.push('Výborný prompt! 👏');

    return {
        wordCount,
        tokenEstimate,
        specificity,
        hasRole,
        hasFormat,
        suggestions
    };
}

// Prompt Builder funkce
function buildPrompt() {
    const role = document.getElementById('role-select').value;
    const topic = document.getElementById('topic-select').value;
    const format = document.getElementById('format-select').value;
    const audience = document.getElementById('audience-select').value;

    if (!role || !topic || !format || !audience) {
        alert('Prosím vyberte všechny možnosti.');
        return;
    }

    const prompt = `${role}. Vysvětli ${topic} ${audience} ${format}. Použij jednoduché příklady a zajímavé analogie.`;

    document.getElementById('prompt-result').textContent = prompt;
    document.getElementById('built-prompt').style.display = 'block';
}

function copyPrompt(event) {
    const promptText = document.getElementById('prompt-result').textContent;
    navigator.clipboard.writeText(promptText).then(function() {
        const button = event.target;
        const originalText = button.textContent;
        const originalBg = button.style.background || window.getComputedStyle(button).background;

        button.textContent = 'Zkopírováno! ✓';
        button.style.background = '#16a34a';

        setTimeout(() => {
            button.textContent = originalText;
            button.style.background = originalBg;
        }, 2000);
    }).catch(function(err) {
        console.error('Chyba při kopírování: ', err);
        alert('Kopírování se nezdařilo. Zkuste text vybrat a zkopírovat ručně.');
    });
}
