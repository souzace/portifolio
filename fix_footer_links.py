import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The current social links in the footer
# We need to extract them, remove the WhatsApp one, and restructure them.
social_links_match = re.search(r'<div class="social-links">.*?</div>', html, re.DOTALL)
if social_links_match:
    social_links_html = social_links_match.group(0)
    
    # Extract Insta
    insta = re.search(r'<a href="https://www.instagram.com/mvnilson/".*?</a>', social_links_html, re.DOTALL).group(0)
    # Extract YT
    yt = re.search(r'<a href="https://www.youtube.com/@NilsonVieira".*?</a>', social_links_html, re.DOTALL).group(0)
    # Extract FB
    fb = re.search(r'<a href="https://www.facebook.com/mvnilson".*?</a>', social_links_html, re.DOTALL).group(0)
    
    # SVG for WhatsApp
    wa_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
    
    # Construct the new HTML
    # We use the hollow green CTA button we made earlier.
    new_html = f"""<div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">
        <div class="social-links" style="margin: 0; display: flex; gap: 10px;">
            {insta}
            {yt}
            {fb}
        </div>
        <a href="https://wa.me/558597496713" target="_blank" class="cta-btn" style="margin: 0; padding: 0.6rem 1.2rem; font-size: 0.9rem;">
            {wa_svg} Falar no WhatsApp
        </a>
    </div>"""
    
    html = html.replace(social_links_html, new_html)

    with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Footer links updated successfully.")
else:
    print("Could not find social links.")

