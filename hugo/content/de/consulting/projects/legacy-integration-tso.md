---
translationKey: project-legacy-integration-tso
title: "Legacy-Integration für einen Übertragungsnetzbetreiber"
description: "Ein von mir entwickelter Cloud-nativer Adapter automatisiert die Veröffentlichung von Outage-Planning-Informationen aus einer Bestandssoftware zur ENTSO-E-Plattform und reduziert manuelle Arbeitsschritte auf ein Minimum."
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
  - "Spring Framework"
  - "Kafka"
  - "PostgreSQL"
  - "jOOQ"
  - "Angular"
  - "Kubernetes"
  - "Azure DevOps"
  - "Argo CD"
  - "Helm"
business-areas:
  - "Energy"
---
Für einen deutschen Übertragungsnetzbetreiber habe ich einen cloud-nativen Adapter zwischen einer Bestandssoftware und der Veröffentlichungsplattform des Verbandes der Übertragungsnetzbetreiber ENTSO-E entwickelt. Der Adapter automatisiert die Veröffentlichung von Outage Planning Coordination (OPC) Informationen, die zuvor manuell übertragen wurden.

Dazu habe ich:

- Eine cloud-native Datenintegrationssoftware auf Basis von Spring Boot entwickelt
- Die SFTP/MFT-Dateiübertragung des Bestandssystems über ein Claim-Check-Pattern an eine ereignisgesteuerte Pipeline angebunden
- Mehrere XML-Dokumente in ein standardisiertes ENTSO-E-Format zur Veröffentlichung überführt
- Eine Angular-Webapp zur Nachverfolgung veröffentlichter Meldungen implementiert
- Und Fehlermeldungen per Webhook an ein Kollaborationssystem (MS Teams) übergeben
