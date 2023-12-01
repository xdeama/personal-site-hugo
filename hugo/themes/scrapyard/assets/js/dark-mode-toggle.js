document.addEventListener('DOMContentLoaded', function () {
    initializeThemeToggle();
});

// window.addEventListener('load', initializeThemeToggle);

function initializeThemeToggle() {
    console.log("initializeThemeToggle")
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
        updateUrlParam(mode);
    }

    function getThemeFromUrl() {
        const params = new URLSearchParams(window.location.search);
        return params.get('theme');
    }

    function updateUrlParam(theme) {
        const params = new URLSearchParams(window.location.search);
        params.set('theme', theme);
        window.history.replaceState({}, '', `${window.location.pathname}?${params}`);
        updateAllInternalLinks();
    }

    function updateAllInternalLinks() {
        console.log("updateAllInternalLinks")
        const currentParams = new URLSearchParams(window.location.search);

        document.querySelectorAll('a').forEach(link => {
            const url = new URL(link.href);

            if (url.origin === window.location.origin) {
                currentParams.forEach((value, key) => {
                    url.searchParams.set(key, value);
                });
                link.href = url.toString();
            }
        });
    }

    const urlTheme = getThemeFromUrl();
    if (urlTheme) {
        setTheme(urlTheme);
    } else {
        setTheme(prefersDarkScheme.matches ? 'dark' : 'light');
    }

    toggleButton.addEventListener('click', () => {
        console.log("click")
        const newTheme = document.body.classList.contains('dark-mode') ? 'light' : 'dark';
        setTheme(newTheme);
        console.log("theme: " + newTheme)
    });

    prefersDarkScheme.addEventListener('change', (e) => {
        if (!getThemeFromUrl()) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    updateAllInternalLinks();
}
