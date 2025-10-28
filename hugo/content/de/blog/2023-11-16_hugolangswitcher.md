---
translationKey: blog_hugolangswitcher
title: 'Ein Sprachwechsel-Link für Hugo Webseiten'
description: 'Ein Sprachwechsel-Link für den Hugo Static Site Generator im Multilingual Mode, welcher die aktuelle Seite in anderen Sprachen öffnet.'
date: 2023-11-16T14:00:00-07:00
draft: false
tags: hugo
---
Diese Webseite wurde mit Hugo erstellt, einem Framework zur Generierung statischer Seiten. Auch wenn ich sicherlich keine Preise für das Design gewinnen werde, habe ich viel Wert auf Bedienbarkeit und responsives Design gelegt.

Hugo unterstützt Mehrsprachigkeit auf sehr hohem Niveau. Mir fehlte ein Button oder Link, über den die aktuell angezeigte Seite mit dem Gegenstück in einer anderen Sprache verknüpft wird.

Ich wollte also gezielt einen Link, der nicht zur Startseite in einer bestimmten Sprache führt, sondern den gerade gezeigten Inhalt in einer anderen Sprache darstellt. Nur für den Fall, dass er nicht auf Englisch existiert, möchte ich den Leser stattdessen auf die Startseite leiten.
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
