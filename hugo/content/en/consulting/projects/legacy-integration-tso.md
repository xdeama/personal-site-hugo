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
company: "Denis Malolepszy Software Engineering, Frankfurt am Main, Germany"
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
For a German transmission system operator, I developed a cloud-native adapter between legacy software and the publication platform of the association of transmission system operators (ENTSO-E). The adapter automates the publication of Outage Planning Coordination (OPC) information that was previously transferred manually.

For this purpose, I:

- Developed cloud-native data integration software based on Spring Boot,
- Bridged the legacy system's SFTP/MFT file transfer to an event-driven pipeline using a claim-check pattern,
- Transformed multiple XML documents into a standardized ENTSO-E format for publication,
- Implemented an Angular web app for tracking published notifications,
- And connected error notifications to MS Teams via webhook.
