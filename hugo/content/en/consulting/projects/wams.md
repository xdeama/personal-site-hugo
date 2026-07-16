---
translationKey: project-wams
title: Real-time Wide Area Monitoring System (WAMS)
description: "For a technical study at a European transmission system operator, I developed a cloud-native Phasor Data Concentrator (PDC) and implemented the complete data path from PMUs to LFR in compliance with IEEE C37.118."
date: 2025-12-01T08:00:00+01:00
draft: false
layout: project
weight: 10
daterange: December 2025 — March 2026
role: Software Engineer
company: DenktMit eG, Oberursel, Germany
techstack:
  - Java 21
  - Spring Boot (WebFlux & Reactive)
  - Java Operator SDK
  - Kubernetes
  - Apache Kafka (Strimzi)
  - Apache Druid
  - RabbitMQ
  - Argo CD & Helm
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
As part of a technical study at a European transmission system operator, I developed a cloud-native Phasor Data Concentrator (PDC) and implemented the complete data path from PMUs to LFR. The study showed that high-resolution synchrophasor data can be captured in compliance with IEEE C37.118, concentrated through the cloud-native PDC implementation, and integrated into a modular control center architecture.

**Key Activities:**

* **PDC Gateway:** Custom development of a software-based Phasor Data Concentrator (PDC) acting as a central gateway for processing PMU phasor measurement data according to the IEEE C37.118 standard.
* **High-Performance Ingestion:** Design and implementation of the data pipeline using Apache Druid for high-performance long-term storage (historian) and aggregation of high-frequency measurement values.
* **Visualization:** Implementation of specialized Grafana dashboards based on Druid data sources for real-time visualization of grid data and historical analyses.
