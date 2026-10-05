import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add a media query for the header and logo
mobile_css = """
@media (max-width: 768px) {
    .header-content {
        flex-direction: column;
        gap: 12px;
        padding: 1rem;
        text-align: center;
    }
    .logo {
        font-size: 1.6rem;
    }
    .logo-sax {
        width: 26px;
        height: 26px;
    }
    .logo-sub {
        font-size: 0.65rem;
        letter-spacing: 2px;
    }
    .floating-notes {
        right: 15px; /* Adjust slightly for scaled sax */
        top: -8px;
    }
}
"""
css += mobile_css

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile CSS fixed.")
