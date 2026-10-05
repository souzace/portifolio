import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the placeholder background block
old_card_img = """.card-img {
    height: 200px;
    background-color: #eaddc7;
    /* We will replace these with real images later */
}"""

new_card_img = """.card-img {
    height: 200px;
    background-size: cover;
    background-position: center;
}
.placeholder-paes { background-image: url('product1.jpg'); }
.placeholder-doces { background-image: url('product2.jpg'); }
.placeholder-cafe { background-image: url('product3.jpg'); }
.placeholder-frios { background-image: url('product4.jpg'); }
"""

css = css.replace(old_card_img, new_card_img)

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Product images assigned.")
