# personal-site-hugo
My personal website https://dmalo.de made with Hugo, a self made custom theme and fluid responsive CSS. Inspired by https://andy-bell.co.uk/ and his guide on CSS https://every-layout.dev. Actually, I made this website mainly because I needed an excuse to start a css project from scratch, without Bootstrap, Tailwind or readymade themes.

# status
Theme and CSS in need of cleanup and are not yet standalone usable. 


# features
- language switcher that keeps you on the current page
- dark mode switcher with minimal JS
- fluent CSS layout with https://every-layout.dev
- language switching link that keeps the visitor on the same page url
- dark mode switching without cookies
- the theme uses JavaScript for darkmode toggling and a fullscreen overlay for images, so the website is usable and all information accessible without JavaScript enabled


# Documentation

## run dev server
./hugo-serve-dev.sh

### network mode
./hugo-serve-dev.sh -n

### minify
-m turns on hugo --minify, which is helpful to check before production deployments, because it might break things like shortcodes

## frontmatter
The title is mandatory, heading is optional.
The heading can be set to overwrite title as the first h1 heading of the page

## robots meta tag
This frontmatter exampke: 
```
robots:
    index: false
    follow: false
```

inserts this html code:
```
<meta name="robots" content="noindex, follow" />
<meta name="googlebot" content="noindex">
<meta name="googlebot-news" content="noindex">
```

The frontmatter vars **index** and **follow** can be used independently.

## markdown image links with lightbox
Insert an image with a link to a lightbox fullscreen overlay:
```
[![Alt-Text](filename.png)](filename.png)
```

### file structure
The required file structure:
```
../posts/
- post-withimage/
    - index.md
    - filename.png
```
## Shortcodes
The following shortcodes are meant for usage in markdown:

### rawhtml
Does exactly what it says. Beware: **hugo --minify** might delete your whitespace after the shortcode.
```
{{< rawhtml >}} {{< /rawhtml >}}
```

### to-img
```
{{< to-img src="image.png" class="profile-img frame" alt="Alt description" >}}
```
Includes an img tag with classes, style, alt text and a relative path (i.e. next to a markdown file).

### static-img
```
{{< static-img src="denis.png" class="profile-img frame" alt="Denis" >}}
```
Includes an img tag with classes, style, alt text from the static assets folder */static/img*.

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

### add a div with custom classes around markdown
```
{{< div class="list-with-columns" >}}
### **Technologien**
- Kotlin
- Apache Solr
- Selenium
- Go
- React
{{< /div >}}
```

### linkedin-icon
The LinkedIn icon and link has a --minify problem.   
Workaround: add a html blank between it and the next word.
```
{{< linkedin-icon >}}&nbsp;nextWord
```
