---
translationKey: 11ty-aliases
title: Seiten-Aliases in Eleventy konfigurieren
heading: Wie man mit Eleventy Aliases für Seiten konfiguriert
description: Eleventy bringt keine Bordmittel für Aliases mit. Mit JavaScript und Pagination Templates wird dies jedoch nachvollziehbar und wartbar möglich.
date: 2024-03-04T14:00:00+01:00
draft: false
---

Der Static Site Generator Eleventy bringt keine Bordmittel für Aliases mit. Mit einer Kombination aus JavaScript Konfiguration und Pagination Templates wird dies jedoch nachvollziehbar und wartbar möglich.

## Was ist ein Seiten-Alias
Ein Alias ist ein alternativer Name, also zusätzlicher Pfad zu einer bestehenden Seite. Mit einem Alias wird die gleiche Seite unter verschiedenen Namen auffindbar.

## Wozu braucht man einen Seiten-Alias?
Es gibt viele praktische Anwendungsmöglichkeiten, oder Umstände in denen man sich eine weitere URL wünscht, die auf eine bestehende Seite verweist.

Man könnte Beispielsweise für eine Werbemaßnahme für eine Webseite *tolle-produkte.de* einen QR-Code generieren, der von *tolle-produkte.de/qr-code* auf *tolle-produkte.de/index.html* verweist. So kann man später anhand der Webserver Logs nachvollziehen, wie viele Besucher über den QR-Code als Besucher auf die Webseite kamen.

Vielleicht hat man auch vor einiger Zeit eine beliebte Seite *tolle-produkte.de/sehr-beliebte-aber-echt-lange-URL* angelegt, für die man aus Gründen eine kürzere Version wie *tolle-produkte.de/top* wünscht, ohne die alte URL zu löschen.

Für alle diese Fälle eignen sich Seiten-Aliases. Also legen wir welche an!

## Schritt 1: Seiten-Aliases in einer Collection sammeln
Eleventy Seiten werden mit Frontmatter definiert. Das ist der Definitionsblock am Kopf jeder Seite. Je nach Technologiewahl sieht dieser Unterschiedlich aus. Ich verwende in diesem Beispiel Markdown mit YAML-Frontmatter.
Beispiel:

**Beispiel Datei index.md**
```markdown
---
title: Meine Homepage
layout: layouts/home.njk
aliases:
 - /auch-die-homepage
 - /homepage
 - /qr-code
---
```

In diesem Beispiel sind bereits drei Seiten-Aliases enthalten: */auch-die-homepage*, */homepage* und */qr-code*. Das bedeutet zusätzlich zu */index* soll diese Seiten als */auch-die-homepage*, */homepage* und */qr-code* erreichbar sein.

Falls Sie noch keine *.eleventy.js* in Ihrem Eleventy Projekt Rootverzeichnis haben, erstellen Sie die Default-Konfiguration nach der [aktuellen Dokumentation](https://www.11ty.dev/docs/config/). Beispiel:

**.eleventy.js**
```javascript
module.exports = function(eleventyConfig) {
  // Return your Object options:
  return {
    dir: {
      input: "views",
      output: "dist"
    }
  }
};
```

Erweitern Sie dann Ihre .eleventy.js-Datei mit der folgenden Logik, um 'Aliases' aus dem Frontmatter aller Ihrer Markdown-Dateien in einer Collection namens frontmatterAliases zu sammeln. Die Filteranweisung *src/**/*.md* sollte an Ihre Projektstruktur angepasst werden. 


**.eleventy.js**
```javascript
module.exports = function(eleventyConfig) {

  // Collect all aliases from frontmatter
  eleventyConfig.addCollection("frontmatterAliases", function (collectionApi) {
    const nodes = collectionApi.getFilteredByGlob("src/**/*.md");
    let frontmatterAliases = [];

    nodes.forEach(node => 
      (node.data.aliases || []).forEach(alias =>
        frontmatterAliases.push([node.data.page.url,`${alias}`])
      )
    )
    return frontmatterAliases
  })
};

  // Return your Object options:
return {
  dir: {
    input: "views",
    output: "dist"
  }
}

```

**Auszug meiner relevanten Projekt-Dateistruktur:**
```
/my-11ty-project/src/ (enthält alle Markdown Content Dateien, wie z.B. die folgenden)
/my-11ty-project/src/index.md
/my-11ty-project/src/_includes/layouts/ (enthält alle Layout Template Dateien, wie z.B. die folgenden)
/my-11ty-project/src/_includes/layouts/redirect.njk (wird in Schritt 3 erstellt)
/my-11ty-project/src/_includes/layouts/page.njk
/my-11ty-project/.eleventy.js (wird in Schritt 1 erstellt)
/my-11ty-project/redirects.njk (wird in Schritt 2 erstellt)
/my-11ty-project/node-modules/
/my-11ty-project/package.json
/my-11ty-project/package-lock.json
```

## Schritt 2: Für jeden Seiten-Alias automatisiert eine Seite anlegen
In Ihrem Content Ordner, in meinem Fall */src/* legen Sie eine Template-Datei *redirects.njk*. Ich verwende in diesem Beispiel [Nunjucks Templates](https://mozilla.github.io/nunjucks/). Der Ansatz funktioniert äquivalent mit anderen Templating Engines, sofern Sie folgende Logik abbilden:

**redirects.njk**
```markdown
---
pagination:
  data: collections.frontmatterAliases
  size: 1
  alias: redirect
permalink: "/{{redirect[1]}}/index.html"
layout: "layouts/redirect.njk"
---
```

Das Template sorgt durch *Pagination* dafür, dass pro Eintrag in der Sammlung *frontmatterAliases* eine Seite mit dem Layout aus der Definition in */layouts/redirect.njk* erstellt wird. Dieses Layout folgt in Schritt 3.

### Hinweise
An *permalink: "/{{redirect[1]}}/index.html"* ist sichtbar, dass für jeden Alias ein Ordner und eine index.html generiert wird. Dies ist aktuell Best Practice in Eleventy, um sowohl /page.html, als auch /page zum Inhalt zu routen. 

Generiert man anstelle des Ordners lediglich eine *permalink: "{{redirect[1]}}.html"*, so wird Eleventy */page* nicht zum Ziel routen, sondern auf den *.html* Suffix bestehen.

Generiert man anstelle des Ordners lediglich eine *permalink: "{{redirect[1]}}"*, so wird Eleventy */page* zwar zum Ziel routen, aber der Webserver (Bspw. Apache)den Inhalt mit hoher Wahrscheinlichkeit nicht als HTML-Webseite erkennen und als Plaintext ausliefern. Dies kann man mit *.htaccess* Overwrites zwar für Apache korrigieren, ist jedoch nicht frei von Nebenwirkungen und daher der Ordner-Lösung mit */Pfadname/index.html* unterlegen.


## Schritt 3: Layout Template mit Weiterleitung erstellen
Falls Ihre Layouts in einem anderen Pfad liegen, so passen Sie den Pfad in Schritt 2 unter *layout:* an und erstellen Sie nun *redirect.njk* am Pfad Ihrer Wahl. Ihre *redirect.njk* sollte im selben Ordner wie Ihre Index-Datei (*index.md*) liegen.

Der Inhalt des Layouts sollte eine vollständige Website sein, die Ihre Metadaten (Seitentitel und Co), CSS, einen Hinweis auf die Weiterleitung und die Weiterleitung selbst implementiert. Ein Minimalbeispiel, welches nicht Verwendung gedacht ist wäre:

**redirect.njk**
```html
<html>
<head>
    <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
</head>
<body>
    <h1>Weiterleitung</h1>
    <p>Sie werden zu <a href="{{ redirect[0] }}">{{ redirect[0] }}</a> weitergeleitet. Unterstützt Ihr Webbrowser dies nicht, so können Sie dem Link selbst durch einen Click folgen.</p>

    <script type="text/javascript">
    window.location.href = '{{ redirect[0] }}';
  </script>
</body>
```
Die Variable redirect[0] enthält die URL des Alias, jedoch nur den Pfad. Also nicht *www.deine-homepage.de/mein-erster-alias*, sondern */mein-erster-alias*.

Ich habe bereits ein Basis-Tempalte für meine Eleventy-Webseite und erweitere dieses lediglich um den Hinweis und die Weiterleitungsmechanik. 

Es gibt keine allgemeingültige Lösung für eine HTTP-Weiterleitung, daher sind in diesem Beispiel zwei Lösung integriert, die sich gegenseitig nicht behindern und den Großteil der Möglichen Endgeräte abdecken sollten.

### Weiterleitugnstechnik 1: JavaScript
Funktioniert solange JavaScript in Endgerät unterstützt wird. Die Funktion kann nach belieben angepasst werden und bspw. X Sekunden vor der Weiterleitung gewartet werden.
```html
<script type="text/javascript">
    window.location.href = '{{ redirect[0] }}';
</script>
```

### Weiterleitugnstechnik 2: Fallback als Head Meta Tag
Grundsätzlich für alle Endgeräte ohne JavaScript. Funktioniert leider nicht mehr in allen Browsern und kann ebenfalls Browserseitig deaktiviert werden.
```html
<head>
    <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
</head>
```

### Erweiterbares Layout Beispiel
Hier ist mein vollständiges Beispiel. In der Layout Datei *layouts/page.njk* sind jeweils Nunjucks Blöcke integriert, um die interessanten Stellen erweitern zu können. Sie können daher auch dieses Beispiel nutzen und sich eine äquivalente *page.njk* entwickeln, die Ihr Layout mit Nunjuck *{block }* erweiterbar macht.

**redirect.njk**
```html
{% extends 'layouts/page.njk' %}

{% block head_extensions %}
  <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
{% endblock %}

{% block intro %}
  <div class="l-section">
    <div></div>
    <div class="l-section__75 l-stack">
      <h1>Weiterleitung</h1>
      <p>Sie werden zu <a href="{{ redirect[0] }}">{{ redirect[0] }}</a> weitergeleitet. Unterstützt Ihr Webbrowser dies nicht, so können Sie dem Link selbst durch einen Click folgen.</p>
    </div>
  </div>
{% endblock %}
      
{% block scripts %}
  <script type="text/javascript">
    window.location.href = '{{ redirect[0] }}';
  </script>
{% endblock %}
```

## Aliases Verwenden
Um Ihre Aliases zu verwenden können Sie nun im Frontmatter Ihrer Seitendefinitionen Aliases definieren. Beispiel:
```markdown
---
title: Meine Homepage
layout: layouts/home.njk
aliases:
 - /auch-die-homepage
 - /homepage
 - /qr-code
---
```

Bei Ihrem nächsten Eleventy build, oder *npm start*, sollte nun automatisch für alle von Ihnen vergebenen Alias Definitionen jeweils eine Seite mit dem redirect.njk Layout erstellt werden. Falls nicht empfehle ich die Pfade erneut zu prüfen und im Anschluss die Prozesskette entlang auf Fehlersuche zu gehen. In Ihrer *.eleventy.js* Konfiguration wird JavaScript verwendet, Sie können also im Zweifel logging einbauen um zu sehen ob Eleventy Aliases findet und in die Sammlung schreibt.

Im Eleventy Build Log sollten Ihre Alias Erzeugungen sichtbar sein:
```
[11ty] Writing _site/homepage/index.html from ./src/redirects.njk
[11ty] Writing _site/auch-die-homepage/index.html from ./src/redirects.njk
[11ty] Writing _site/qr-code/index.html from ./src/redirects.njk
```
