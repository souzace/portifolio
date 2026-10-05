import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the subtitle text
html = html.replace('<span class="ff-sub">Fale com nosso mestre padeiro.</span>', '<span class="ff-sub">Venha nos conhecer!</span>')

# Inject the instagram icon into the right side
insta_icon = """<div class="footer-socials" style="display: flex; align-items: center; gap: 1rem; margin-right: 1.5rem;">
                    <a href="https://www.instagram.com/emporio_linneo/" target="_blank" aria-label="Instagram" style="color: rgba(249, 243, 233, 0.6); transition: color 0.3s;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" onmouseover="this.style.color='#D4AF37'" onmouseout="this.style.color='currentColor'"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                </div>"""

# Replace the start of footer-fixed-right
old_right = '<div class="footer-fixed-right">'
new_right = '<div class="footer-fixed-right" style="display: flex; align-items: center;">\n                ' + insta_icon

html = html.replace(old_right, new_right)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Footer text and Instagram icon updated.")
