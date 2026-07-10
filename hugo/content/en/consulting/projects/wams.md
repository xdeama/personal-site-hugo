---
translationKey: project-wams
title: Real-time Wide Area Monitoring System (WAMS)
description: "For a strategic initiative of two European transmission system operators, I am evolving a platform for real-time grid awareness that integrates high-resolution measurement data into a modular control center architecture."
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
As part of a strategic initiative by two European transmission system operators, I am working on the further development of a platform to improve real-time grid awareness and operational decision-making.
The focus is on integrating high-resolution measurement data into a modular control center architecture for the analysis of complex grid phenomena.

Key Activities:

* Development of a software-based Phasor Data Concentrator (PDC) acting as a central gateway for processing PMU phasor measurement data according to the IEEE C37.118 standard.
* Conception and implementation of the data pipeline using Apache Druid for high-performance long-term storage (historian) and aggregation of high-frequency measurement values.
* Implementation of specialized Grafana dashboards based on Druid data sources for the real-time visualization of grid data and historical analyses.
