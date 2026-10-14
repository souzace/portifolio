with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Bloco antigo da sticky-right
old_sticky_right = """            <div class="sticky-right">
                <a href="https://wa.me/558592828087?text=Ol%C3%A1%20Kuro%20Neko!%20Estou%20no%20site%20e%20procurando%20um%20colecion%C3%A1vel%20espec%C3%ADfico." target="_blank" class="btn-sticky-neon">
                    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
                    <span>Falar no Zap</span>
                </a>
            </div>"""

# Novo bloco com os ícones das redes sociais oficiais do Carrd (Instagram, Facebook, LinkedIn) ao lado do botão de WhatsApp
new_sticky_right = """            <div class="sticky-right">
                <div class="sticky-socials">
                    <!-- Instagram -->
                    <a href="https://www.instagram.com/kuronekotoys/" target="_blank" rel="noopener noreferrer" class="sticky-social-link ig-link" title="Instagram @kuronekotoys">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                    </a>
                    <!-- Facebook -->
                    <a href="https://www.facebook.com/profile.php?id=61563701499130" target="_blank" rel="noopener noreferrer" class="sticky-social-link fb-link" title="Facebook Kuro Neko Toys">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                    </a>
                    <!-- LinkedIn -->
                    <a href="https://www.linkedin.com/company/storekuronekotoys/" target="_blank" rel="noopener noreferrer" class="sticky-social-link in-link" title="LinkedIn Store Kuro Neko Toys">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </a>
                </div>

                <a href="https://wa.me/558592828087?text=Ol%C3%A1%20Kuro%20Neko!%20Estou%20no%20site%20e%20procurando%20um%20colecion%C3%A1vel%20espec%C3%ADfico." target="_blank" class="btn-sticky-neon">
                    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
                    <span>Falar no Zap</span>
                </a>
            </div>"""

html = html.replace(old_sticky_right, new_sticky_right)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
/* Ícones das Redes Sociais na Barra Fixa Flutuante (Padrão Orkes) */
.sticky-right {
    display: flex;
    align-items: center;
    gap: 1.2rem;
}

.sticky-socials {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.sticky-social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-color);
    color: var(--text-muted);
    text-decoration: none;
    transition: transform 0.2s, color 0.2s, border-color 0.2s, background 0.2s, box-shadow 0.2s;
}

.sticky-social-link:hover {
    transform: translateY(-3px) scale(1.08);
}

.ig-link:hover {
    color: #fff;
    background: linear-gradient(135deg, #E1306C 0%, #C13584 100%);
    border-color: #E1306C;
    box-shadow: 0 0 15px rgba(225, 48, 108, 0.4);
}

.fb-link:hover {
    color: #fff;
    background: #1877F2;
    border-color: #1877F2;
    box-shadow: 0 0 15px rgba(24, 119, 242, 0.4);
}

.in-link:hover {
    color: #fff;
    background: #0A66C2;
    border-color: #0A66C2;
    box-shadow: 0 0 15px rgba(10, 102, 194, 0.4);
}

@media (max-width: 768px) {
    .sticky-right {
        gap: 0.6rem;
    }
    .sticky-socials {
        gap: 0.4rem;
    }
    .sticky-social-link {
        width: 32px;
        height: 32px;
    }
    .sticky-social-link svg {
        width: 16px;
        height: 16px;
    }
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Redes sociais oficiais adicionadas na barra fixa com sucesso!")
