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
