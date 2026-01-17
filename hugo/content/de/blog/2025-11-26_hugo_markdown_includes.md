---
translationKey: hugo-md-composition
title: Markdown Dokumente in Hugo zusammensetzen
description: Markdown Dateien in andere Markdown Dateien inkludieren mit Hugo um Wiederholungen im Content zu vermeiden
heading: Markdown Dokumente in Hugo zusammensetzen
date: 2025-11-26T10:00:00+01:00
draft: false
---

Bei der Nutzung von [Hugo](https://gohugo.io) habe ich oft Inhaltsabschnitte, die ich an mehr als einer Stelle benötige – etwa eine Liste meiner Schwerpunkte oder meine Erfahrung mit bestimmten Technologien.
Wenn ich diese per Copy-Paste an mehrere Orte kopiere, entsteht das Risiko, sie an einer Stelle zu ändern, an anderen aber zu vergessen.

Die naheliegendste aber unsaubere Lösung mit Hugo ist es, ein Template für diese Seiten zu erstellen und mehrere Markdown-Dateien in dieses Template zu laden.

Beispiel für ein Template, das zwei Markdown-Dokumente kombiniert:
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

Das ist nicht meine bevorzugte Lösung, da ich Templates als Layout-Vorlagen oder visuelle Schablonen betrachte. Sie sind nicht für die Komposition von Inhalten gedacht, sondern für deren Präsentation.

Wenn ich jedes Mal ein Template erstelle, sobald mehr als eine Markdown-Datei auf eine Seite soll, wandert der Inhalt schrittweise in die Templates ab und verteilt sich über die gesamte Ordnerstruktur.
Idealerweise möchte ich meinen Content im Content-Ordner haben und nirgendwo sonst.

Hier ist ein Beispiel, bei dem Inhalt im Template landete, was Übersetzungen unnötig erschwert:

```html
{{/* layouts/custom/composite-page.html */}}

{{ define "main" }}
<h1>{{ .Title }}</h1>

{{ .Content }}

<h2>Meine Erfahrung</h2>
<p>Meine Erfahrung verteilt sich auf folgende Technologien und Industrien.</p>

<section class="experience">
    {{ with .Site.GetPage "/sections/experience.md" }}
    {{ .Content }}
    {{ end }}
</section>
{{ end }}
```

Glücklicherweise bietet Hugo einen Weg, dies mittels [Shortcodes](https://gohugo.io) und [Headless Bundles](https://gohugo.io/quick-reference/glossary/#headless-bundle) zu lösen.

Ich bin ehrlich gesagt nicht sicher, warum die Lösung, die ich nutze, nicht standardmäßig eingebaut ist.

## Wiederverwendbares als Headless Bundle speichern

Bevor wir den Code schreiben, brauchen wir einen Ort, um unsere Schnipsel zu speichern. Wir können sie nicht einfach in das normale Post-Verzeichnis legen, da Hugo versuchen würde, daraus eigenständige, besuchbare Seiten zu bauen (z.B. `IhreSeite.de/posts/my-snippet`).

Um das zu verhindern, nutzen wir ein **Headless Bundle**. Das ist ein Verzeichnis, das Content-Ressourcen enthält, aber selbst keine Seite veröffentlicht.

1.  Erstellen Sie einen neuen Ordner unter `content/includes`.
2.  Erstellen Sie darin eine Datei namens `index.md`.
3.  Fügen Sie folgenden Frontmatter in die `index.md` ein:

```text
---
title: "Includes"
headless: true
---
```

Der Parameter `headless: true` ist hier der Schlüssel. Er sagt Hugo, dass dieser Ordner als Container für Ressourcen (Bilder, Markdown, Daten) dienen soll, auf die programmatisch zugegriffen wird, für die aber niemals eine öffentliche URL generiert werden darf.

Jetzt können Sie Ihre wiederverwendbaren Markdown-Dateien in diesen Ordner legen (z.B. `content/includes/newsletter-cta.md`).

## Shortcode erstellen

Nun, da wir einen Speicherort haben, brauchen wir einen Mechanismus, um diesen Inhalt abzurufen und in unsere Posts zu injizieren. In Hugo machen wir das mit einem Custom Shortcode.

Erstellen Sie eine neue Datei unter `layouts/shortcodes/include-md.html` und fügen Sie folgende Logik ein:

```text
{{/* Referenz auf das "headless" bundle holen */}}
{{ $headless := .Site.GetPage "/includes" }}

{{/* Die spezifische Datei finden, die als Parameter übergeben wurde */}}
{{ $snippet := $headless.Resources.GetMatch (.Get 0) }}

{{/* Wenn die Datei existiert, Inhalt rendern */}}
{{ with $snippet }}
    {{ .Content }}
{{ end }}
```

### Erklärung

* **`.Site.GetPage "/includes"`**: Dies sucht unser Headless Bundle anhand des Pfades.
* **`.Resources.GetMatch`**: Dies sucht innerhalb des Bundles nach einer Ressource, die dem Dateinamen entspricht, den Sie im Shortcode angeben.
* **`.Content`**: Das ist der entscheidende Schritt. Er nimmt das rohe Markdown aus Ihrer Schnipsel-Datei und rendert es zu HTML, genau so, als wäre es Teil des Hauptposts.

## Den Shortcode im Markdown nutzen

Der Inhalt der Markdown Dokumente lässt sich nun per Shortcode in anderen Markdown Dokumenten einfügen. Eine Beispiel eines Markdown Dokumentes in meinem `/content/..` Verzeichnis:

```text
# Meine Erfahrung

Meine Erfahrung verteilt sich auf folgende Technologien und Industrien.

{{</* include "experience.md" */>}}

# Meine Schwerpunkte

{{</* include "focus-areas.md" */>}}

# Mehr Bla Bla

{{</* include "bla.md" */>}}
```

Dieser Ansatz harmoniert mit einer mehrspraching Hugo Seite, da man den `/includes` Ordner jeweils in den Sprachordner anlegen kann.

Diese Syntax sucht sich damit die passende Übersetzung aus dem Dateibaum.
```text
{{</* include "focus-areas.md" */>}}
```
