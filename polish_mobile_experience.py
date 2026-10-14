with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Polimento Mobile Completo de Alta Conversão
mobile_polish = """
/* ==========================================================================
   POLIMENTO MOBILE PREMIUM (UX / UI AUDIT)
   ========================================================================== */
@media (max-width: 768px) {
    /* Header Mobile */
    .header-content {
        padding: 0.6rem 1rem;
    }
    .brand-avatar-circle {
        width: 42px !important;
        height: 42px !important;
    }
    .brand-main {
        font-size: 1.1rem !important;
    }
    .brand-kanji {
        font-size: 0.55rem !important;
    }
    .store-comic-badge {
        font-size: 0.8rem !important;
        padding: 0.2rem 0.7rem !important;
        letter-spacing: 1.5px !important;
        border-width: 2px !important;
        box-shadow: 2px 2px 0px var(--kuro-orange) !important;
    }

    /* Hero Section Mobile */
    .hero-section {
        padding: 3rem 0 2rem !important;
    }
    .hero-split-grid {
        display: flex !important;
        flex-direction: column !important;
        gap: 2rem !important;
        text-align: center !important;
    }
    .hero-left-content {
        align-items: center !important;
        order: 1;
    }
    .hero-right-visual {
        order: 2;
        width: 100%;
    }
    .cat-poster-frame {
        max-width: 280px !important;
        border-radius: 20px !important;
    }
    .cat-poster-badge {
        font-size: 0.72rem !important;
        padding: 0.4rem 0.9rem !important;
        bottom: 0.8rem !important;
    }
    .hero-headline {
        font-size: 1.85rem !important;
        line-height: 1.25 !important;
        margin-bottom: 1rem !important;
    }
    .hero-desc {
        font-size: 0.95rem !important;
        margin-bottom: 1.8rem !important;
    }
    .hero-cta-group {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }
    .btn-primary-glow, .btn-secondary-neon {
        width: 100%;
        justify-content: center;
        padding: 0.85rem 1.4rem !important;
        font-size: 0.95rem !important;
    }
    .hero-badges-row {
        grid-template-columns: 1fr !important;
        gap: 0.8rem !important;
        padding-top: 1.5rem !important;
    }
    .trust-badge {
        padding: 0.7rem 1rem !important;
    }

    /* Vitrine de Drops Mobile */
    .section-drops {
        padding: 3.5rem 0 2.5rem !important;
    }
    .section-title {
        font-size: 1.7rem !important;
    }
    .drops-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
    }

    /* Universos Mobile */
    .section-universes {
        padding: 2.5rem 0 3rem !important;
    }
    .universes-grid {
        grid-template-columns: 1fr !important;
        gap: 1.2rem !important;
    }
    .universe-card {
        min-height: 180px !important;
        padding: 1.5rem !important;
    }

    /* Localização Mobile */
    .section-locations {
        padding: 2rem 0 4rem !important;
    }
    .loc-card-wrapper {
        padding: 1.8rem 1.2rem !important;
        gap: 2rem !important;
    }
    .loc-left h2 {
        font-size: 1.6rem !important;
    }
    .social-radar-box {
        padding: 1.6rem 1.2rem !important;
    }

    /* Barra Fixa Flutuante Mobile (Orkes Ultra-Compact) */
    .sticky-footer-bar {
        padding: 8px 0 !important;
    }
    .sticky-container {
        padding: 0 1rem !important;
    }
    .sticky-avatar-wrap {
        width: 44px !important;
        height: 44px !important;
    }
    .st-title {
        font-size: 0.78rem !important;
        max-width: 130px;
        line-height: 1.2;
    }
    .st-sub {
        display: none !important; /* Esconde no mobile para não poluir */
    }
    .sticky-socials {
        display: none !important; /* Esconde os 3 ícones extras no mobile para priorizar o botão Zap */
    }
    .btn-sticky-neon {
        padding: 8px 14px !important;
        font-size: 0.82rem !important;
        gap: 5px !important;
    }
}
"""

css += mobile_polish

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Auditoria e polimento mobile aplicados com sucesso!")
