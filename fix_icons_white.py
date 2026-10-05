import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make .social-links a (main footer) white and borderless
old_social = re.search(r'\.social-links a \{.*?\}', html, re.DOTALL).group(0)
new_social = """.social-links a {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 5px;
        }"""
html = html.replace(old_social, new_social)

old_social_hover = re.search(r'\.social-links a:hover \{.*?\}', html, re.DOTALL).group(0)
new_social_hover = """.social-links a:hover {
            color: var(--brand-gold);
            transform: translateY(-3px);
        }"""
html = html.replace(old_social_hover, new_social_hover)


# Make .sticky-social-btn (sticky footer) white and borderless
old_sticky = re.search(r'\.sticky-social-btn \{.*?\}', html, re.DOTALL).group(0)
new_sticky = """.sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 5px;
        }"""
html = html.replace(old_sticky, new_sticky)

old_sticky_hover = re.search(r'\.sticky-social-btn:hover \{.*?\}', html, re.DOTALL).group(0)
new_sticky_hover = """.sticky-social-btn:hover {
            color: var(--brand-gold);
            transform: translateY(-2px);
        }"""
html = html.replace(old_sticky_hover, new_sticky_hover)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Icons changed to white and borderless.")
