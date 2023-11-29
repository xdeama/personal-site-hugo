---
translationKey: blog_hugolangswitcher
title: 'A Language Switch Link for Hugo Websites'
description: 'Language switch link for the Hugo Static Site Generator in Multilingual Mode, which opens the current page in other languages'
date: 2023-11-16T14:00:00-07:00
draft: false
tags: hugo
---
This website was created using [Hugo](https://gohugo.io/), a static site generator framework. While I'm certainly not going to win any awards for design, I have placed a lot of emphasis on usability and responsive design.

Hugo supports [multilingualism](https://gohugo.io/content-management/multilingual/#menus) at a very high level. What's missing out of the box can be implemented with [Hugo Methods](https://gohugo.io/methods/).

I was missing a button or link through which the currently displayed page is linked to its counterpart in another language.

So, I specifically wanted a link that does not lead to the homepage in a certain language, but rather switches between this blog article in German and English, for example. Only in the case that it does not exist in English, I would like to direct the reader to the homepage instead.

```html
<!-- Überprüfen, ob die aktuelle Sprache Deutsch ist -->
{{ if eq .Site.Language.Lang "de" }}
    
    <!-- Initialisieren einer Flagge, um zu verfolgen, ob eine englische Übersetzung gefunden wurde -->
    {{ $found := false }}
    
    <!-- Beginn der Schleife durch die verfügbaren Übersetzungen -->
    {{ range .Translations }}
        <!-- Überprüfen, ob die aktuelle Übersetzung auf Englisch ist -->
        {{ if eq .Lang "en" }} 
            <a href="{{ .Permalink }}">{{ .Language.LanguageName }}</a> 
            {{ $found = true }} 
            {{ break }} 
        {{ end }} 
    {{ end }}

    <!-- Überprüfen, ob keine englische Übersetzung gefunden wurde und Standardlink erstellen -->
    {{ if not $found }} 
        <a href="{{ .Site.BaseURL }}en/">Englisch</a> 
    {{ end }}

<!-- Überprüfen, ob die aktuelle Sprache Englisch ist -->
{{ else if eq .Site.Language.Lang "en" }}

    <!-- Initialisieren einer Flagge, um zu verfolgen, ob eine deutsche Übersetzung gefunden wurde -->
    {{ $found := false }}

    <!-- Beginn der Schleife durch die verfügbaren Übersetzungen -->
    {{ range .Translations }}
        <!-- Überprüfen, ob die aktuelle Übersetzung auf Deutsch ist -->
        {{ if eq .Lang "de" }} 
            <a href="{{ .Permalink }}">{{ .Language.LanguageName }}</a>
            {{ $found = true }} 
            {{ break }} 
        {{ end }} 
    {{ end }}

    <!-- Überprüfen, ob keine deutsche Übersetzung gefunden wurde und Standardlink erstellen -->
    {{ if not $found }} 
        <a href="{{ .Site.BaseURL }}de/">Deutsch</a> 
    {{ end }}
{{ end }}
```
