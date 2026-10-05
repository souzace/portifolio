import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace product image styles
old_img = """.arch-img {
    height: 350px;
    border-radius: 0;
    background-size: cover;
    background-position: center;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(53, 28, 21, 0.1);
    box-shadow: 0 10px 20px rgba(53, 28, 21, 0.05);
    transition: transform 0.3s;
}"""

new_img = """.arch-img {
    height: 350px;
    border-radius: 2px;
    background-size: cover;
    background-position: center;
    margin-bottom: 1.5rem;
    border: 12px solid #FDFBF7; /* Polaroid frame */
    box-shadow: 0 15px 35px rgba(53, 28, 21, 0.15); /* Shadow for depth */
    transition: transform 0.3s;
}"""
css = css.replace(old_img, new_img)

# Also apply it to the historia image
old_hist = """.historia-image-arch {
    flex: 1;
    height: 500px;
    border-radius: 0;
    background-size: cover;
    background-position: center;
    border: 2px solid var(--primary);
}"""

new_hist = """.historia-image-arch {
    flex: 1;
    height: 500px;
    border-radius: 2px;
    background-size: cover;
    background-position: center;
    border: 15px solid #FDFBF7; /* Polaroid frame */
    box-shadow: 0 15px 35px rgba(53, 28, 21, 0.15); /* Shadow for depth */
}"""
css = css.replace(old_hist, new_hist)

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Polaroid cards applied.")
