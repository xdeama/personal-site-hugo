---
translationKey: hugo-md-composition
title: Markdown Document Composition with Hugo
description: Include markdown files in other markdown files with Hugo
heading: Markdown Document Composition with Hugo
date: 2025-11-26T10:00:00+01:00
draft: false
---

Using [Hugo](https://gohugo.io) I frequently end up with sections of content that I need in more than one place, like a list of my focus areas and my experience with technology.
Having these copied and pasted over many locations creates the chance of changing them in one while forgetting others.

Hugo's most straight forward but dirty solution is to create a template for those pages and include multiple markdown files in the template.

Example of a template that combines two markdown content documents:
```html
{{/* layouts/custom/composite-page.html */}}

{{ define "main" }}
<h1>{{ .Title }}</h1>

{{ .Content }}

<section class="experience">
    {{ with .Site.GetPage "/sections/experience.md" }}
    {{ .Content }}
    {{ end }}
</section>
{{ end }}
```

This is not my preferred solution, because I regard templates as layout templates, or visual templates, not meant to solve content composition but content presentation.

Creating a template each time more than one markdown files should go into a page will eventually move content into templates, spreading content all over the folder structure.
Ideally, I want my content in the content folder and nowhere else.

Here's an example where content ended up in the template, making translation harder:
```html
{{/* layouts/custom/composite-page.html */}}

{{ define "main" }}
<h1>{{ .Title }}</h1>

{{ .Content }}

<h2>My Experience</h2>
<p>My experience is distributed across technologies and industries as follows.</p>

<section class="experience">
    {{ with .Site.GetPage "/sections/experience.md" }}
    {{ .Content }}
    {{ end }}
</section>
{{ end }}
```

Fortunately, Hugo provides a way to solve this using a [Shortcode](https://gohugo.io) combined with [Headless Bundles](https://gohugo.io/quick-reference/glossary/#headless-bundle).

I am honestly not sure why the one I'm using isn't built right in.

## Store Reusable Stuff as Headless Bundles

Before we write the code, we need a place to store our snippets. We cannot simply drop them into the standard post directory, because Hugo would try to build them into actual, visitable pages (e.g., `yoursite.com/posts/my-snippet`).

To prevent this, we use a **Headless Bundle**. This is a directory that contains content resources but does not publish a page itself.

1.  Create a new directory at `content/includes`.
2.  Inside that directory, create a file named `index.md`.
3.  Add the following Frontmatter to `index.md`:

```yaml
---
title: "Includes"
headless: true
---
````

The `headless: true` parameter is the key here. It tells Hugo to treat this folder as a container for resources (images, markdown files, data) that can be accessed programmatically, but to never render a public URL for it.

You can now place your reusable markdown files inside this folder (e.g., `content/includes/newsletter-cta.md`).

## The Shortcode

Now that we have a storage location, we need a mechanism to fetch that content and inject it into our posts. In Hugo, we do this with a custom Shortcode.

Create a new file at `layouts/shortcodes/include.html` and paste the following logic:

```html
{{/* Get the "headless" bundle page reference */}}
{{ $headless := .Site.GetPage "/includes" }}

{{/* Find the specific file passed as a parameter */}}
{{ $snippet := $headless.Resources.GetMatch (.Get 0) }}

{{/* If the file exists, render its content */}}
{{ with $snippet }}
    {{ .Content }}
{{ end }}
```

### Explained

* **`.Site.GetPage "/includes"`**: This looks up our headless bundle by its path.
* **`.Resources.GetMatch`**: This searches inside that bundle for a resource matching the filename you provide when using the shortcode.
* **`.Content`**: This is the magic step. It takes the raw Markdown from your snippet file and renders it into HTML, exactly as if it were part of the main post.

## Using the Shortcode in Markdown Content

Content from markdown documents can now be inserted into other markdown documents using the shortcode:

```markdown
# My Experience

My experience is distributed across technologies and industries as follows.

{{</* include "experience.md" */>}}

# My Focus Areas

{{</* include "focus-areas.md" */>}}

# More Blah Blah

{{</* include "bla.md" */>}}
```

This approach plays nicely with multi-language Hugo sites, as you can create the /includes folder within each language directory.

This syntax automatically picks the correct translation from the file tree.

```markdown
{{</* include "focus-areas.md" */>}}
```
