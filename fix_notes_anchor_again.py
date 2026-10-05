import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Update CSS to anchor from the sax bell (right side)
css = css.replace('left: 0px;', 'left: 20px;')
css = css.replace('top: -20px;', 'top: -10px;')

# Also adjust the floating animation direction slightly to the right
old_anim = """    50% {
        transform: translateY(-5px) translateX(5px) scale(1);
    }
    80% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-20px) translateX(-5px) scale(1.2);
        opacity: 0;
    }"""
    
new_anim = """    50% {
        transform: translateY(-5px) translateX(10px) scale(1);
    }
    80% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-20px) translateX(15px) scale(1.2);
        opacity: 0;
    }"""

css = css.replace(old_anim, new_anim)

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Notes anchored to sax bell on the right.")
