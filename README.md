# personal-site-hugo
Personal website with Hugo, custom theme and fluid responsive CSS. Inspired by https://andy-bell.co.uk/ and his guide on CSS https://every-layout.dev. Actually, I made this website mainly because I needed an excuse to start a css project scratch.

# status
Theme and CSS in need of cleanup

# features
- language switcher that keeps you on the current page
- dark mode switcher with minimal JS
- fluent CSS layout with https://every-layout.dev
- fullscreen modal for images with lightbox

# Documentation

## run dev server
./hugo-serve-dev.sh

## frontmatter
title is mandatory, heading is optional
-> heading can be set to overwrite title as the first h1 heading of the page

## robots meta tag
```
robots:
    index: false
    follow: false
```

inserts
```
<meta name="robots" content="noindex, follow" />
<meta name="googlebot" content="noindex">
<meta name="googlebot-news" content="noindex">
```

**index** and **follow** can be used independently.

## markdown image links with lightbox
```
[![Alt-Text](filename.png)](filename.png)
```

### file structure
```
../posts/
- post-withimage/
    - index.md
    - filename.png
```
