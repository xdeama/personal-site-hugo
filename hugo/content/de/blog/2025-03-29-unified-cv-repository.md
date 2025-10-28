---
translationKey: generate-cv-from-website
title: CV mit SSG-Webseite generieren
description: CV und Webseite aus dem selben Markdown generieren
heading: CV mit SSG-Webseite generieren
date: 2025-03-29T14:00:00+01:00
draft: true
---

1 repo mit markdown
daraus webseite englisch und deutsch
und CV in PDF und docx generieren

=> 1 Ort für Datenpflege
=> durch CI/CD Prozess immer aktuellen Lebenslauf für Projektanfragen

Das Grundproblem: Markdown hat nicht genug layout-Anweisungen für eine ansehnliche Webseite

Probleme: 
- Layout im Markdown (multicolumn style kann nicht wissen wann und wo in zweispaltiges layout okay aussieht)
- Hugo kann kein markdown inclue ==> kann nicht 1 seite machen mit den
  - => kann ich! muss ins template;; müsste aber unterschiede wie die Striche im Portfolio entfernen und den gleichen Text nutzen
- wollte content zu 1 thema in 1 markdown file, nicht 1 file pro position in layout, oder content im layout
- jetzt habe ich layout im content

