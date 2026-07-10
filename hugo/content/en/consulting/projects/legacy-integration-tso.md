---
translationKey: project-legacy-integration-tso
title: "Legacy Integration for a Transmission System Operator"
description: "A cloud-native adapter I built automates publishing outage planning information from legacy software to the ENTSO-E platform, reducing manual work steps to a minimum."
date: 2024-05-01T08:00:00+01:00
draft: false
layout: project
weight: 40
daterange: "May 2024 — January 2025"
role: "Software Engineer"
company: "Denis Malolepszy Software Engineering, Frankfurt am Main"
techstack:
  - "Java (v21)"
  - "Spring Boot"
  - "Kafka"
  - "Postgres"
  - "jOOQ and jOOX"
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
A newly developed automated adapter between legacy software and a publication platform of the association of 
transmission system operators (ENTSO-E) minimizes manual work steps in the context of publishing information to the 
Outage Planning Coordination (OPC) platform.

For this purpose, I:

- Developed cloud-native data integration software based on Spring Boot,
- Integrated it with the legacy system via a Kafka event streaming platform,
- Transformed multiple XML documents into a standardized format,
- Which is transmitted to an association platform for publication,
- And broken down in an Angular web app for tracking,
- Or passes error messages to collaboration systems (MS Teams) via webhook.
