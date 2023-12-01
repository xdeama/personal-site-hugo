document.addEventListener('DOMContentLoaded', function () {
    initializeThemeToggle();
});

function initializeThemeToggle() {
    console.log("initializeThemeToggle")
    const toggleButton = document.getElementById('dark-mode-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    function setTheme(mode, updateUrl = true) {
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
        if (updateUrl) {
            updateUrlParam(mode);
        }
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
        setTheme(urlTheme, false);
    } else {
        setTheme(prefersDarkScheme.matches ? 'dark' : 'light', false);
    }

    toggleButton.addEventListener('click', () => {
        const newTheme = document.body.classList.contains('dark-mode') ? 'light' : 'dark';
        setTheme(newTheme);
    });

    prefersDarkScheme.addEventListener('change', (e) => {
        if (!getThemeFromUrl()) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    updateAllInternalLinks();
}

function getThemeFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('theme');
}
