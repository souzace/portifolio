import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add music notes container after the saxophone
sax_svg = '<svg class="logo-sax" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4,2A1,1 0 0,0 3,3A1,1 0 0,0 4,4A3,3 0 0,1 7,7V8.66L7,15.5C7,19.1 9.9,22 13.5,22C17.1,22 20,19.1 20,15.5V13A1,1 0 0,0 21,12A1,1 0 0,0 20,11H14A1,1 0 0,0 13,12A1,1 0 0,0 14,13V15A1,1 0 0,1 13,16A1,1 0 0,1 12,15V11A1,1 0 0,0 13,10A1,1 0 0,0 12,9V8A1,1 0 0,0 13,7A1,1 0 0,0 12,6V5.5A3.5,3.5 0 0,0 8.5,2H4Z" /></svg>'

notes_html = """<div class="floating-notes">
                        <span class="note note-1">&#x266A;</span>
                        <span class="note note-2">&#x266B;</span>
                        <span class="note note-3">&#x266A;</span>
                    </div>"""

# Replace the SVG with SVG + notes
html = html.replace(sax_svg, sax_svg + notes_html)

# Add position relative to .logo div to anchor the notes
html = html.replace('<div class="logo">', '<div class="logo" style="position: relative;">')

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

notes_css = """
/* Floating Music Notes Animation */
.floating-notes {
    position: absolute;
    right: -10px; /* Adjust based on where the sax is */
    top: -15px;
    width: 30px;
    height: 30px;
    pointer-events: none;
}
.note {
    position: absolute;
    color: var(--gold);
    font-size: 0.6rem;
    opacity: 0;
    font-family: 'Times New Roman', serif;
}

.note-1 {
    left: 0;
    animation: floatNote 3s infinite ease-in;
    animation-delay: 0s;
}
.note-2 {
    left: 10px;
    font-size: 0.8rem;
    animation: floatNote 3.5s infinite ease-in;
    animation-delay: 1s;
}
.note-3 {
    left: 20px;
    animation: floatNote 3s infinite ease-in;
    animation-delay: 2s;
}

@keyframes floatNote {
    0% {
        transform: translateY(10px) scale(0.5);
        opacity: 0;
    }
    20% {
        opacity: 0.8;
    }
    50% {
        transform: translateY(-5px) translateX(5px) scale(1);
    }
    80% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-20px) translateX(-5px) scale(1.2);
        opacity: 0;
    }
}
"""

css += notes_css

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Animated notes added.")
