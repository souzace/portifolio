/**
 * Picanha do Sávio - Script de Interatividade & Cardápio Modular
 * Adaptado ao Novo Layout Luminoso
 */

const MENU_ITEMS = [
  {
    category: 'carnes',
    badge: 'Carro-Chefe',
    title: 'Picanha Argentina na Chapa',
    serves: 'Serve 3 a 4 pessoas',
    desc: 'Corte nobre com capa de gordura perfeita, fatiada na hora e servida em chapa fumegante com sal grosso. Acompanha baião de dois com queijo coalho, macaxeira frita crocante, farofa na manteiga e vinagrete da casa.',
    price: 'R$ 139,90',
    image: 'img/hero_picanha.jpg'
  },
  {
    category: 'carnes',
    badge: 'Mais Pedido',
    title: 'Picanha Nacional Especial',
    serves: 'Serve 2 a 3 pessoas',
    desc: 'Carne macia e suculenta grelhada no braseiro no ponto de sua preferência. Acompanha baião de dois, feijão-verde cremoso, batata frita e farofa d’água.',
    price: 'R$ 119,90',
    image: 'img/prato_picanha_nacional.jpg'
  },
  {
    category: 'carnes',
    badge: 'Regional Farto',
    title: 'Carne de Sol do Sertão',
    serves: 'Serve 2 a 3 pessoas',
    desc: 'Maturada na casa, puxada na manteiga da terra, fatiada com cebola roxa dourada, acompanhada de macaxeira cozida ou frita e feijão tropeiro.',
    price: 'R$ 98,90',
    image: 'img/prato_carne_sol.jpg'
  },
  {
    category: 'carnes',
    badge: 'Corte Macio',
    title: 'Maminha na Brasa',
    serves: 'Serve 2 a 3 pessoas',
    desc: 'Extremamente macia e suculenta, selada no braseiro e fatiada fina. Acompanha arroz branco ou baião, purê de macaxeira e vinagrete.',
    price: 'R$ 108,90',
    image: 'img/prato_maminha.jpg'
  },
  {
    category: 'pizzas',
    badge: 'Exclusividade do Sávio',
    title: 'Pizza de Picanha Especial',
    serves: '8 fatias grandes',
    desc: 'A famosa receita da casa: massa artesanal fina e crocante, molho de tomate rústico, queijo mussarela derretido, tiras generosas de picanha grelhada na brasa, cebola roxa e orégano.',
    price: 'R$ 68,90',
    image: 'img/prato_pizza_picanha.jpg'
  },
  {
    category: 'pizzas',
    badge: 'Tradicional Cearense',
    title: 'Pizza Sertaneja com Coalho',
    serves: '8 fatias grandes',
    desc: 'Mussarela, carne de sol desfiada temperada, queijo coalho tostado em cubos, cebola caramelizada e toque de manteiga da terra.',
    price: 'R$ 62,90',
    image: 'img/prato_pizza_sertaneja.jpg'
  },
  {
    category: 'mar',
    badge: 'Clássico Cearense',
    title: 'Peixe à Delícia da Casa',
    serves: 'Serve 2 a 3 pessoas',
    desc: 'Filé de peixe nobre grelhado, coberto com banana frita em fatias, molho branco aveludado e gratinado ao forno com bastante queijo.',
    price: 'R$ 96,90',
    image: 'img/prato_peixe_delicia.jpg'
  },
  {
    category: 'mar',
    badge: 'Grelhado Fresco',
    title: 'Tilápia Inteira Desossada',
    serves: 'Serve 2 pessoas',
    desc: 'Grelhada na brasa, pele crocante e carne úmida temperada com ervas finas e limão taiti. Acompanha baião de dois e salada colorida.',
    price: 'R$ 79,90',
    image: 'img/prato_tilapia.jpg'
  },
  {
    category: 'mar',
    badge: 'Petisco Nobre',
    title: 'Camarão Alho & Óleo Crocante',
    serves: 'Porção para compartilhar',
    desc: 'Camarões selecionados dourados no azeite com lâminas de alho frito crocante e cheiro-verde fresco. Acompanha fatias de limão e molho rosé.',
    price: 'R$ 64,90',
    image: 'img/prato_camarao.jpg'
  },
  {
    category: 'boteco',
    badge: 'Petisco Campeão',
    title: 'Bolinhas Mistas do Sávio',
    serves: '12 unidades',
    desc: 'Seleção dos petiscos mais famosos: bolinhas de queijo coalho, carne de sol, camarão e bacalhau com casquinha crocante e recheio cremoso.',
    price: 'R$ 44,90',
    image: 'img/prato_petiscos.jpg'
  },
  {
    category: 'boteco',
    badge: 'Happy Hour',
    title: 'Torre de Batata com Cheddar & Bacon',
    serves: 'Serve 3 a 4 pessoas',
    desc: 'Batatas fritas sequinhas e crocantes cobertas com queijo cheddar cremoso derretido e pedaços crocantes de bacon artesanal.',
    price: 'R$ 42,90',
    image: 'img/prato_batata_cheddar.jpg'
  },
  {
    category: 'boteco',
    badge: 'Chopp Trincando',
    title: 'Chopp Artesanal & Cervejas Estupidamente Geladas',
    serves: 'Individual',
    desc: 'Ampla carta de cervejas e chopp servido na caneca ultracongelada a -2°C para acompanhar sua carne na brasa.',
    price: 'A partir de R$ 9,90',
    image: 'img/prato_chopp.jpg'
  }
];

document.addEventListener('DOMContentLoaded', () => {
  initMenuFilters();
  initCareersForm();
});

function initMenuFilters() {
  const filterBtns = document.querySelectorAll('.menu-filter-btn');
  const menuGrid = document.getElementById('menu-items-grid');

  if (!menuGrid) return;

  function renderMenu(category = 'todos') {
    const filtered = category === 'todos' 
      ? MENU_ITEMS 
      : MENU_ITEMS.filter(item => item.category === category);

    menuGrid.innerHTML = filtered.map(item => `
      <div class="menu-item-card-light" data-category="${item.category}">
        <div class="menu-item-header">
          <img src="${item.image}" alt="${item.title}" class="menu-item-img" loading="lazy">
          <span class="menu-item-badge">${item.badge}</span>
        </div>
        <div class="menu-item-body">
          <h3 class="menu-item-title">${item.title}</h3>
          <span class="menu-item-serves"><i class="fa-solid fa-users"></i> ${item.serves}</span>
          <p class="menu-item-desc">${item.desc}</p>
          <div class="menu-item-footer">
            <span class="menu-item-price">${item.price}</span>
            <a href="#unidades" class="btn btn-outline-red btn-sm">Pedir na Unidade</a>
          </div>
        </div>
      </div>
    `).join('');
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-filter') || 'todos';
      renderMenu(cat);
    });
  });

  renderMenu('todos');
}

function initCareersForm() {
  const form = document.getElementById('careers-talent-form');
  const feedback = document.getElementById('careers-feedback');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const nome = document.getElementById('cand-nome').value;
    const vaga = document.getElementById('cand-vaga').value;
    const unidade = document.getElementById('cand-unidade').value;

    if (feedback) {
      feedback.style.display = 'block';
      feedback.innerHTML = `
        <div style="background: #EFF6FF; border: 1.5px solid #1E3A8A; color: #1E3A8A; padding: 16px; border-radius: 8px; font-size: 0.95rem; font-weight: 600;">
          <i class="fa-solid fa-check-circle" style="color: #22C55E;"></i> Obrigado, <strong>${nome}</strong>! Sua candidatura para <strong>${vaga} (${unidade})</strong> foi registrada com sucesso no banco de talentos do Picanha do Sávio. Nossa gerência entrará em contato!
        </div>
      `;
      form.reset();
    }
  });
}
