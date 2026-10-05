import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix .social-icon (main body footer)
old_social_css = """        .social-icon {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 1px solid var(--brand-gold);
            color: var(--brand-gold);
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .social-icon:hover {
            background-color: var(--brand-gold);
            color: var(--brand-dark);
            transform: translateY(-3px);
        }"""

new_social_css = """        .social-icon {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            color: #aaa;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 5px;
        }
        .social-icon svg {
            width: 24px;
            height: 24px;
        }
        .social-icon:hover {
            color: var(--brand-gold);
            transform: translateY(-3px);
        }"""
html = html.replace(old_social_css, new_social_css)

# Fix .sticky-social-btn (desktop sticky footer)
old_sticky_css = """        .sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 5px; border: 1px solid var(--brand-gold);
            color: var(--brand-gold);
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .sticky-social-btn:hover {
            background-color: var(--brand-gold);
            color: var(--brand-dark);
        }"""

new_sticky_css = """        .sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #aaa;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 5px;
        }
        .sticky-social-btn svg {
            width: 24px;
            height: 24px;
        }
        .sticky-social-btn:hover {
            color: var(--brand-gold);
            transform: translateY(-2px);
        }"""
html = html.replace(old_sticky_css, new_sticky_css)

# Remove the mobile overrides that are no longer needed for sticky-social-btn since we made it global
mobile_override_to_remove = """            .sticky-social-btn {
                width: auto; /* Remove fixed width to match Orkes minimal style */
                height: auto;
                border: none !important; /* Remove borders */
                background: transparent !important;
                padding: 0;
            }
            .sticky-social-btn svg {
                width: 22px;
                height: 22px;
                color: #aaa;
            }"""

mobile_override_replacement = """            .sticky-social-btn {
                padding: 0;
            }
            .sticky-social-btn svg {
                width: 22px;
                height: 22px;
            }"""
html = html.replace(mobile_override_to_remove, mobile_override_replacement)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Icons updated.")
