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
## Shortcodes

### rawhtml
Does exactly what it says. Beware: **hugo --minify** might delete your whitespace after the shortcode.
```
{{< rawhtml >}} {{< /rawhtml >}}
```

### to-img
```
{{< to-img src="image.png" class="profile-img frame" alt="Alt description" >}}
```
Creates an img tag with classes, style and alt text.

### embed-svg
Embed is used to embed the SVG code into the HTML code, with the advantage of supporting dark mode by fill color through CSS.
```
{{< embed-svg "static/svg/denktmit-logo.svg" >}}
```

### to-svg
Like the **img** shortcode, but with fixed CSS. SVGs in <img> tags do not support dark mode by fill color through CSS.
```
{{< to-svg src="/svg/software-engineering.svg" alt="Software Engineering" >}}
```
