---
translationKey: project-wams
title: Real-time Wide Area Monitoring System (WAMS)
description: "Für eine technische Studie bei einem europäischen Übertragungsnetzbetreiber habe ich einen cloud-nativen Phasor Data Concentrator (PDC) entwickelt und damit den vollständigen Datenpfad von PMUs bis zum LFR IEEE C37.118-konform umgesetzt."
date: 2025-12-01T08:00:00+01:00
draft: false
layout: project
weight: 10
daterange: Dezember 2025 — März 2026
role: Software Engineer
company: DenktMit eG, Oberursel
techstack:
  - Java 21
  - Spring Boot (WebFlux & Reactive)
  - Java Operator SDK
  - Kubernetes
  - Apache Kafka (Strimzi)
  - Apache Druid
  - RabbitMQ
  - ArgoCD & Helm
  - PostgreSQL
  - Keycloak (OAuth2/OIDC)
  - Grafana with Druid Datasource
  - Prometheus
  - Testcontainers
  - Docker
  - OpenAPI
technologies:
  - Java
  - Spring Boot
  - Kafka
  - Apache Druid
  - Grafana
  - Kubernetes
  - PostgreSQL
  - Keycloak
business-areas:
  - Energy
---
Im Rahmen einer technischen Studie bei einem europäischen Übertragungsnetzbetreiber habe ich einen cloud-nativen Phasor Data Concentrator (PDC) entwickelt und damit den vollständigen Datenpfad von PMUs bis zum LFR umgesetzt. Die Studie zeigte, dass hochauflösende Synchrophasordaten IEEE C37.118-konform erfasst, über die cloud-native PDC-Implementierung konzentriert und in eine modulare Leitsystem-Architektur integriert werden können.

**Tätigkeitsschwerpunkte:**

* **PDC Gateway:** Eigenentwicklung eines software-basierten Phasor Data Concentrators (PDC) als zentrales Gateway zur Verarbeitung von PMU-Phasor-Messdaten gemäß IEEE C37.118 Standard.
* **High-Performance Ingestion:** Konzeption und Implementierung der Datenstrecke mittels Apache Druid zur performanten Langzeitspeicherung (Historian) und Aggregation hochfrequenter Messwerte.
* **Visualisierung:** Realisierung spezialisierter Grafana-Dashboards auf Basis der Druid-Datenquellen zur Echtzeit-Visualisierung von Netzdaten und historischen Analysen.
