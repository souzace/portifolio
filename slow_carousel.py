with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("animation: scroll-marquee 20s linear infinite;", "animation: scroll-marquee 45s linear infinite;")

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Carousel animation slowed down.")
