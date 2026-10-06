with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the instagram block to fix alignment
old_socials = '<div class="footer-socials" style="display: flex; align-items: center; gap: 1rem; margin-right: 0.2rem;">'
new_socials = '<div class="footer-socials" style="display: flex; align-items: center; margin-right: 12px; height: 100%;">'

html = html.replace(old_socials, new_socials)

old_insta_link = 'style="color: rgba(249, 243, 233, 0.6); transition: color 0.3s;"'
new_insta_link = 'style="color: rgba(249, 243, 233, 0.6); transition: color 0.3s; display: flex; align-items: center;"'

html = html.replace(old_insta_link, new_insta_link)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Instagram alignment fixed.")
