// Carrossel horizontal suave idêntico ao projeto Ideal
function scrollCarousel(btn, dir) {
    const wrapper = btn.closest('.carousel-wrapper');
    const track = wrapper.querySelector('.services-track');
    const card = track.querySelector('.service-slide');
    if (!card) return;

    const scrollAmount = card.offsetWidth + 18; // largura do card + gap
    track.scrollBy({
        left: dir === 'right' ? scrollAmount : -scrollAmount,
        behavior: 'smooth'
    });

    setTimeout(() => {
        const leftBtn = wrapper.querySelector('.carousel-btn.left');
        const rightBtn = wrapper.querySelector('.carousel-btn.right');
        if (leftBtn && rightBtn) {
            leftBtn.disabled = track.scrollLeft <= 4;
            rightBtn.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 6;
        }
    }, 350);
}

// Atualiza o estado dos botões ao arrastar ou rolar com o dedo (touch/trackpad)
document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.services-track');
    if (track) {
        track.addEventListener('scroll', () => {
            const wrapper = track.closest('.carousel-wrapper');
            const leftBtn = wrapper.querySelector('.carousel-btn.left');
            const rightBtn = wrapper.querySelector('.carousel-btn.right');
            if (leftBtn && rightBtn) {
                leftBtn.disabled = track.scrollLeft <= 4;
                rightBtn.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 6;
            }
        });
    }
});

// Suporte a Arraste com o Mouse no Desktop (Drag-to-Scroll Fluido)
document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.services-track');
    if (!track) return;

    let isDown = false;
    let startX;
    let scrollLeft;

    track.addEventListener('mousedown', (e) => {
        isDown = true;
        track.classList.add('is-dragging');
        startX = e.pageX - track.offsetLeft;
        scrollLeft = track.scrollLeft;
    });

    track.addEventListener('mouseleave', () => {
        isDown = false;
        track.classList.remove('is-dragging');
    });

    track.addEventListener('mouseup', () => {
        isDown = false;
        track.classList.remove('is-dragging');
    });

    track.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - track.offsetLeft;
        const walk = (x - startX) * 1.6; // velocidade de arraste
        track.scrollLeft = scrollLeft - walk;
    });
});
