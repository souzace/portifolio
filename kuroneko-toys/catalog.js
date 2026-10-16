/**
 * Kuro Neko Toys - Dynamic Catalog & API Integration Layer
 * 
 * Arquitetura Preparada para Hostinger / Headless API:
 * 1. MODO LOCAL / MOCK (Ativo por padrão para demonstração instantânea)
 * 2. MODO API EXTERNA (WooCommerce / Nuvemshop / Endpoint próprio na Hostinger)
 *    Basta alternar USE_EXTERNAL_API para true e configurar API_ENDPOINT.
 */

const CATALOG_CONFIG = {
    // Alterne para true quando o cliente fornecer a URL do WooCommerce/API na Hostinger
    USE_EXTERNAL_API: false,
    API_ENDPOINT: 'https://kuronekotoys.com.br/wp-json/wc/v3/products',
    WHATSAPP_NUMBER: '558592828087',
};

// Base de Produtos (Estrutura idêntica ao payload retornado por APIs de e-commerce)
const MOCK_PRODUCTS = [
    {
        id: 1,
        name: 'Monkey D. Luffy — Gear 5 Sun God',
        universe: 'shonen',
        category: 'One Piece',
        scale: '22cm',
        tag: 'Original Banpresto',
        price: 289.90,
        installments: '3x de R$ 96,63 sem juros',
        badge: 'anime-shonen',
        status: 'available', // available | low_stock | preorder
        statusLabel: 'Pronta Entrega',
        image: '🏴‍☠️',
        description: 'PVC de alta fidelidade • Linha Grandista • Efeitos translúcidos de nuvens celestiais'
    },
    {
        id: 2,
        name: 'Kamado Tanjiro — Hinokami Kagura',
        universe: 'shonen',
        category: 'Demon Slayer',
        scale: '18cm',
        tag: 'Edição Especial',
        price: 249.90,
        installments: '3x de R$ 83,30 sem juros',
        badge: 'anime-kimetsu',
        status: 'available',
        statusLabel: 'Pronta Entrega',
        image: '⚔️',
        description: 'Rica em detalhes • Chamas de fogo esculpidas em resina • Base de suporte reforçada'
    },
    {
        id: 3,
        name: 'Son Goku Super Saiyan 3 — Masterlise',
        universe: 'shonen',
        category: 'Dragon Ball Z',
        scale: '25cm',
        tag: 'Linha Masterlise',
        price: 349.90,
        installments: '3x de R$ 116,63 sem juros',
        badge: 'anime-dbz',
        status: 'low_stock',
        statusLabel: 'Últimas 2 Unidades',
        image: '💥',
        description: 'Pintura fosca premium • Textura anatômica dos músculos e cabelo clássico'
    },
    {
        id: 4,
        name: 'Gundam Aerial — HG 1/144 The Witch from Mercury',
        universe: 'gamer',
        category: 'Gunpla Mecha',
        scale: '1/144',
        tag: 'Bandai Spirits',
        price: 199.90,
        installments: '3x de R$ 66,63 sem juros',
        badge: 'anime-shonen',
        status: 'available',
        statusLabel: 'Pronta Entrega',
        image: '🤖',
        description: 'Kit de montagem oficial Bandai • Articulações completas • Não necessita cola'
    },
    {
        id: 5,
        name: 'Link & Hylian Shield — Tears of the Kingdom',
        universe: 'gamer',
        category: 'Zelda',
        scale: '20cm',
        tag: 'First 4 Figures',
        price: 329.90,
        installments: '3x de R$ 109,96 sem juros',
        badge: 'anime-kimetsu',
        status: 'available',
        statusLabel: 'Pronta Entrega',
        image: '🛡️',
        description: 'Braço Rauru translúcido com luz LED integrada • Escultura oficial Nintendo'
    },
    {
        id: 6,
        name: 'Kuro Neko Jiji — Relógio de Mesa Vintage',
        universe: 'ghibli',
        category: 'Studio Ghibli',
        scale: '15cm',
        tag: 'Kiki Delivery',
        price: 169.90,
        installments: '2x de R$ 84,95 sem juros',
        badge: 'anime-dbz',
        status: 'available',
        statusLabel: 'Exclusivo Kuro Neko',
        image: '🐾',
        description: 'O gato preto clássico em resina moldada com mini relógio funcional analógico'
    }
];

class KuroNekoCatalog {
    constructor() {
        this.products = [];
        this.currentFilter = 'all';
        this.searchQuery = '';
        this.gridElement = document.getElementById('catalog-grid');
        this.filterButtons = document.querySelectorAll('.catalog-filter-btn');
        this.searchInput = document.getElementById('catalog-search-input');
        
        this.init();
    }

    async init() {
        await this.loadProducts();
        this.bindEvents();
        this.render();
    }

    async loadProducts() {
        if (CATALOG_CONFIG.USE_EXTERNAL_API) {
            try {
                // Chamada à API segura na Hostinger
                const response = await fetch(CATALOG_CONFIG.API_ENDPOINT);
                if (!response.ok) throw new Error('Falha ao carregar API');
                const data = await response.json();
                
                // Normaliza formato caso venha de WooCommerce
                this.products = data.map(item => ({
                    id: item.id,
                    name: item.name,
                    category: item.categories?.[0]?.name || 'Colecionável',
                    universe: this.mapCategoryToUniverse(item.categories?.[0]?.name),
                    scale: item.attributes?.find(a => a.name === 'Escala')?.options?.[0] || 'Original',
                    tag: item.tags?.[0]?.name || 'Importado',
                    price: parseFloat(item.price || item.regular_price || 0),
                    installments: 'em até 3x sem juros',
                    badge: 'anime-shonen',
                    status: item.stock_quantity > 0 ? 'available' : 'out_of_stock',
                    statusLabel: item.stock_quantity > 0 ? 'Em Estoque' : 'Esgotado',
                    image: item.images?.[0]?.src || '🎮',
                    description: item.short_description?.replace(/<[^>]+>/g, '') || item.description?.replace(/<[^>]+>/g, '') || ''
                }));
            } catch (err) {
                console.warn('Fallback para produtos mock locais devido ao erro da API:', err);
                this.products = MOCK_PRODUCTS;
            }
        } else {
            // Modo Local Mock
            this.products = MOCK_PRODUCTS;
        }
    }

    mapCategoryToUniverse(catName = '') {
        const lower = catName.toLowerCase();
        if (lower.includes('ghibli') || lower.includes('kuro neko')) return 'ghibli';
        if (lower.includes('zelda') || lower.includes('game') || lower.includes('pokemon')) return 'gamer';
        return 'shonen';
    }

    bindEvents() {
        // Filtros por botões
        this.filterButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.currentFilter = btn.dataset.filter || 'all';
                this.render();
            });
        });

        // Campo de busca em tempo real
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => {
                this.searchQuery = e.target.value.toLowerCase().trim();
                this.render();
            });
        }
    }

    getFilteredProducts() {
        return this.products.filter(item => {
            const matchesFilter = this.currentFilter === 'all' || item.universe === this.currentFilter;
            const matchesSearch = !this.searchQuery || 
                item.name.toLowerCase().includes(this.searchQuery) ||
                item.category.toLowerCase().includes(this.searchQuery) ||
                item.description.toLowerCase().includes(this.searchQuery);
            return matchesFilter && matchesSearch;
        });
    }

    formatPrice(price) {
        return price.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    }

    render() {
        if (!this.gridElement) return;

        const filtered = this.getFilteredProducts();

        if (filtered.length === 0) {
            this.gridElement.innerHTML = `
                <div class="catalog-empty-state">
                    <span class="empty-icon">🔍</span>
                    <h4>Nenhum item encontrado</h4>
                    <p>Não encontramos nenhum colecionável para essa busca no momento.</p>
                    <a href="https://wa.me/${CATALOG_CONFIG.WHATSAPP_NUMBER}?text=Ol%C3%A1!%20Procuro%20um%20colecion%C3%A1vel%20espec%C3%ADfico%20que%20n%C3%A3o%20vi%20no%20site." target="_blank" class="btn-primary-glow btn-sm">
                        Consultar Encomenda no WhatsApp
                    </a>
                </div>
            `;
            return;
        }

        this.gridElement.innerHTML = filtered.map(product => {
            const encodedText = encodeURIComponent(`Olá Kuro Neko! Vi o produto "${product.name}" (${this.formatPrice(product.price)}) no site e gostaria de garantir.`);
            const waLink = `https://wa.me/${CATALOG_CONFIG.WHATSAPP_NUMBER}?text=${encodedText}`;
            
            const isImage = typeof product.image === 'string' && (product.image.startsWith('http') || product.image.endsWith('.jpg') || product.image.endsWith('.png'));

            return `
                <div class="product-card" data-universe="${product.universe}" data-id="${product.id}">
                    <div class="card-badge ${product.badge}">${product.category}</div>
                    
                    <div class="card-image-box">
                        ${isImage ? `<img src="${product.image}" alt="${product.name}" class="card-real-img" loading="lazy">` : `<span class="placeholder-emoji">${product.image}</span>`}
                        
                        <div class="card-tags-overlay">
                            <span class="mini-tag">${product.scale}</span>
                            <span class="mini-tag">${product.tag}</span>
                        </div>

                        ${product.status === 'low_stock' ? `<span class="card-stock-alert">Poucas Unidades</span>` : ''}
                    </div>

                    <div class="card-info">
                        <h3 class="product-name">${product.name}</h3>
                        <p class="product-specs">${product.description}</p>
                        
                        <div class="card-price-row">
                            <div class="price-box">
                                <span class="price-val">${this.formatPrice(product.price)}</span>
                                <span class="price-installments">${product.installments}</span>
                            </div>
                            <span class="status-pill status-${product.status}">${product.statusLabel}</span>
                        </div>

                        <div class="card-actions">
                            <a href="${waLink}" target="_blank" rel="noopener noreferrer" class="btn-buy-card" title="Garantir ${product.name}">
                                <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
                                <span>Garantir no WhatsApp</span>
                            </a>
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }
}

// Inicializa quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    window.kuroNekoCatalog = new KuroNekoCatalog();
});
