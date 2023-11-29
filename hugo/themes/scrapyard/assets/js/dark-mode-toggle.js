document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('dark-mode-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    function setTheme(mode) {
        const sunIcon = document.getElementById('icon-sun');
        const moonIcon = document.getElementById('icon-moon');

        if (mode === 'dark') {
            document.body.classList.add('dark-mode');
            sunIcon.style.display = 'block';
            moonIcon.style.display = 'none';
        } else {
            document.body.classList.remove('dark-mode');
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'block';
        }
    }

    setTheme(prefersDarkScheme.matches ? 'dark' : 'light');

    toggleButton.addEventListener('click', () => {
        const currentTheme = document.body.classList.contains('dark-mode') ? 'light' : 'dark';
        setTheme(currentTheme);
    });

    prefersDarkScheme.addEventListener('change', (e) => {
        setTheme(e.matches ? 'dark' : 'light');
    });
});
