import os

files = ['index.html', 'index-en.html', 'index-es.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove wrapper start
    wrapper_start = '<body>\n<div class="site-main-wrapper" style="position: relative; z-index: 2; background-color: var(--bg-color); box-shadow: 0 20px 40px rgba(0,0,0,0.8);">'
    content = content.replace(wrapper_start, '<body>')

    # 2. Remove footer fixed wrapper close
    footer_fixed = '</div>\n<footer style="position: fixed; bottom: 0; left: 0; width: 100%; z-index: 1;">'
    content = content.replace(footer_fixed, '<footer>')

    # 3. Remove script
    js_script = """<script>
    function updateFooterMargin() {
        const footer = document.querySelector('footer');
        const wrapper = document.querySelector('.site-main-wrapper');
        if (footer && wrapper) {
            wrapper.style.marginBottom = footer.offsetHeight + 'px';
        }
    }
    window.addEventListener('resize', updateFooterMargin);
    window.addEventListener('load', updateFooterMargin);
    
    // Fallback observer in case images/fonts load late
    const observer = new MutationObserver(updateFooterMargin);
    const footerElement = document.querySelector('footer');
    if(footerElement) {
        observer.observe(footerElement, { childList: true, subtree: true, attributes: true });
    }
    
    // Initial call
    updateFooterMargin();
    // Extra call after 500ms for safety
    setTimeout(updateFooterMargin, 500);
</script>
</body>"""
    content = content.replace(js_script, '</body>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Parallax reverted!")
