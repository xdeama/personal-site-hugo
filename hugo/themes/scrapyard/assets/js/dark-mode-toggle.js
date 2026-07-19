document.addEventListener('DOMContentLoaded', function () {
    initializeThemeToggle();
});

function initializeThemeToggle() {
    const toggleButtons = document.querySelectorAll('.dark-mode-toggle');
    const themeOptions = document.querySelectorAll('.theme-option');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    function setTheme(mode, updateUrl = true) {
        document.body.classList.toggle('dark-mode', mode === 'dark');
        document.querySelectorAll('.icon-sun').forEach(icon => {
            icon.style.display = mode === 'dark' ? 'block' : 'none';
        });
        document.querySelectorAll('.icon-moon').forEach(icon => {
            icon.style.display = mode === 'dark' ? 'none' : 'block';
        });
        themeOptions.forEach(option => {
            const active = option.dataset.theme === mode;
            option.classList.toggle('current', active);
            option.setAttribute('aria-pressed', String(active));
        });
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

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const newTheme = document.body.classList.contains('dark-mode') ? 'light' : 'dark';
            setTheme(newTheme);
        });
    });

    themeOptions.forEach(option => {
        option.addEventListener('click', () => {
            setTheme(option.dataset.theme);
        });
    });

    prefersDarkScheme.addEventListener('change', (e) => {
        if (!getThemeFromUrl()) {
            setTheme(e.matches ? 'dark' : 'light', false);
        }
    });

    updateAllInternalLinks();
}

function getThemeFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('theme');
}
