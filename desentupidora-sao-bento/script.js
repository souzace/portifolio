// Script de Interatividade e Otimização de Conversão para Desentupidora São Bento

// 1. Alternador de Modo no Hero (Residencial B2C vs Condomínios B2B)
function switchHeroMode(mode) {
    const b2cBox = document.getElementById('b2c-content');
    const b2bBox = document.getElementById('b2b-content');
    const tabBtns = document.querySelectorAll('.tab-btn');

    tabBtns.forEach(btn => btn.classList.remove('active'));

    if (mode === 'b2c') {
        b2cBox.style.display = 'block';
        b2bBox.style.display = 'none';
        tabBtns[0].classList.add('active');
    } else {
        b2cBox.style.display = 'none';
        b2bBox.style.display = 'block';
        tabBtns[1].classList.add('active');
    }
}

// 2. Calculadora de Tempo Estimado por Região de Fortaleza
function calcularTempo() {
    const select = document.getElementById('bairro-select');
    const box = document.getElementById('tempo-resposta');
    const valor = select.value;

    if (!valor) {
        box.innerHTML = '🚗 Selecione seu bairro para ver o tempo estimado de chegada.';
        box.style.color = 'var(--text-muted)';
        return;
    }

    const tempos = {
        'Aldeota / Meireles': '⚡ Equipe na região! Tempo estimado: <strong>20 a 30 minutos</strong>.',
        'São Bento / Messejana': '⚡ Base operacional próxima! Tempo estimado: <strong>15 a 25 minutos</strong>.',
        'Cocó / Papicu': '⚡ Equipe na região! Tempo estimado: <strong>25 a 35 minutos</strong>.',
        'Fátima / Benfica': '⚡ Equipe na região! Tempo estimado: <strong>20 a 30 minutos</strong>.',
        'Parquelândia / Monte Castelo': '⚡ Equipe em trânsito! Tempo estimado: <strong>25 a 35 minutos</strong>.',
        'Maraponga / Mondubim': '⚡ Equipe na região! Tempo estimado: <strong>25 a 40 minutos</strong>.',
        'Eusébio / Aquiraz': '⚡ Viatura volante RMF! Tempo estimado: <strong>30 a 45 minutos</strong>.',
        'Caucaia / Outras Regiões': '⚡ Viatura volante RMF! Tempo estimado: <strong>35 a 50 minutos</strong>.'
    };

    const resposta = tempos[valor] || '⚡ Tempo médio de atendimento estimado: <strong>30 minutos</strong>.';
    box.innerHTML = `${resposta} <br><a href="https://wa.me/5585986042721?text=Ol%C3%A1,%20estou%20no%20bairro%20${encodeURIComponent(valor)}%20e%20preciso%20de%20um%20t%C3%A9cnico%20urgente!" target="_blank" style="color: var(--primary-yellow); font-weight: 700; text-decoration: underline; margin-top: 6px; display: inline-block;">Confirmar Chamada Imediata →</a>`;
    box.style.color = '#fff';
}

// 3. Smooth Scroll para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
