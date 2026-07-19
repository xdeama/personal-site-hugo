document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.menu-toggle');
    if (!buttons.length) {
        return;
    }
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const open = document.body.classList.toggle('nav-open');
            buttons.forEach(b => b.setAttribute('aria-expanded', String(open)));
        });
    });
});
