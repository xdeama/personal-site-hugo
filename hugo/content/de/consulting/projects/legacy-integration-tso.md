---
translationKey: project-legacy-integration-tso
title: "Legacy-Integration für einen Übertragungsnetzbetreiber"
description: "Ich habe einen Cloud-nativen Adapter entwickelt, der die Veröffentlichung von Outage-Planning-Informationen aus einer Bestandssoftware zur ENTSO-E-Plattform automatisiert und manuelle Arbeitsschritte auf ein Minimum reduziert."
date: 2024-05-01T08:00:00+01:00
draft: false
layout: project
weight: 40
daterange: "Mai 2024 — Januar 2025"
role: "Software Engineer"
company: "Denis Malolepszy Software Engineering, Frankfurt am Main"
techstack:
  - "Java (v21)"
  - "Spring Boot"
  - "Kafka"
  - "Postgres"
  - "jOOQ und jOOX"
  - "Angular"
  - "Azure DevOps"
  - "Kubernetes"
  - "Argo CD"
  - "Helm"
  - "Gradle"
  - "RESTful Microservices"
  - "Git"
technologies:
  - "Java"
  - "Spring Boot"
  - "Kafka"
  - "PostgreSQL"
  - "jOOQ"
  - "Angular"
  - "Kubernetes"
  - "Azure DevOps"
  - "Argo CD"
business-areas:
  - "Energy"
---
Ein neu entwickelter automatisierter Adapter zwischen einer Bestandssoftware und einer Veröffentlichungsplattform des Verbandes
der Übertragungsnetzbetreiber (ENTSO-E) reduziert die manuellen Arbeitsschritte im Kontext der Veröffentlichung 
von Outage Planning Coordination (OPC) Informationen auf ein Minimum.

Dazu habe ich:

- Eine Cloud-native Datenintegrationssoftware auf Spring Boot Basis entwickelt
- Diese per Event-Streaming-Plattform Kafka mit dem Bestandssystem integriert
- Mehrere XML-Dokumente in ein standardisiertes Format überführt
- Welches zur Veröffentlichung an eine Verbandsplattform übermittelt wird
- Und in einer Angular Webapp zur Nachverfolgung aufgeschlüsselt wird
- Oder per Webhook Fehlermeldungen an Kollaborationssysteme (MS Teams) übergibt
