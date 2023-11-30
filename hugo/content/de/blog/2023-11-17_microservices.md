---
translationKey: blog_microservices
title: 'Aufstieg und Fall der Micro Services'
description: 'Entwickler wenden sich zunehmend von Microservices Architektur ab. Eine Erklärung für Nicht-Entwickler.'
date: 2023-11-17T10:15:00-01:00
draft: false
tags: 
  - microservices
---
## Was sind Micro Services
Microservices sind eine Architekturform, bei der eine Anwendung als Sammlung kleiner, unabhängiger Dienste konzipiert ist, die jeweils spezifische Geschäftslogik oder Funktionen umsetzen. 
Diese Architektur ermöglicht eine hohe Skalierbarkeit und Flexibilität, da einzelne Dienste unabhängig voneinander entwickelt, bereitgestellt und skaliert werden können. Allerdings führt diese Verteilung auch zu Herausforderungen in Bezug auf Integration, Management und Sicherheit der Dienste.

{{< embed-svg "static/svg/microservices.svg" >}}

## Aufstieg und Fall der Micro Services
Entwickler wenden sich zunehmend von Microservices ab, da diese Architektur komplexe Herausforderungen in Bezug auf Integration, Netzwerklatenz, Datenkonsistenz und das Management mehrerer unabhängiger Dienste mit sich bringt. Zudem kann die erhöhte Komplexität bei der Fehlersuche und dem Monitoring, sowie der Bedarf an fortgeschrittenen DevOps-Fähigkeiten, einige Teams von der Verwendung von Microservices abhalten.

Als de-facto Industriestandard und Go-to-Lösung für jede Anwendung sind Microservices jedoch nicht geeignet. Sie wurde jedoch so verwendet. Und daher erlebt diese ausgeklügelte und geniale Architekturform diese Tage einen Shitstorm. 

Im Folgenden reduzierte ich das Thema Micro Services stark auf eine eingeschränkte Analogie mit Microsoft Excel, um Fachfremden einen Einblick in die Thematik zu bieten.

## Der Aufstieg
Eine Bank vergibt Kredite und zur Prüfung dieser müssen fünf Abteilungen Daten empfangen und Daten bereitstellen. Die Daten bestehen jeweils aus den Kreditantragsdaten und Informationen, die zuvor andere Abteilungen ermittelt und bereitgestellt haben.

Diese fünf Abteilungen erhalten ihre Anfragen jeweils per E-Mail vom Front Office. So vergehen Tage, bis der Kunde eine Antwort erhält. In jeder Abteilung sitzen Fachbearbeiter und kümmern sich um das Tagesgeschäft: die Daten aus den E-Mails in ihre Bewertungsmatrix eintragen und die Ergebnisse per E-Mail an das Front Office zurück übermitteln.

In allen Fällen handelt es sich bei der Bewertungsmatrix um ein komplexes Excel Sheet, welches täglich auf die neusten Parameter wie Zinsen, Währungswechselkurse, und der dergleichen aktualisiert wird.

{{< embed-svg "static/svg/spreadsheet.svg" >}}

Um die Kreditpüfung zu Beschleunigen, wird vereinbart ein einziges zusammengeführtes Exceldokument zu erstellen, welches eine Eingabemaske enthält. Die Eingabemaske wird vom Front Office mit den Daten des Kunden befüllt. Die enthaltene Logik berechnet und ermittelt die bisher von den fünf Abteilungen per E-Mail übermittelten Daten und weist diese auf der Ausgabemaske aus. Die Abteilungen sollen die Logik und verwendeten Daten stets aktuell halten, sodass die Kreditantragsprüfung in den meisten Fällen ohne Rückfragen direkt vom Front Office durchgeführt werden kann.

Bereits bei der Zusammenführung in ein einziges Exceldokument stellen die Beteiligten fest, dass von den involvierten 25 Mitarbeitern nur ein einziger zum einem Zeitpunkt die Datei bearbeiten kann. Manche Änderungen, die rein additiver Natur sind, können zwar vorbereitet werden, benötigen jedoch auch einen exklusiven Zeitraum zur Integration in das Gesamtdokument. Dies bremst den Fortschritt enorm und sorgt für Frustration, da reihum auf Zugang zum Dokument gewartet werden muss.

Zudem wird regelmäßig festgestellt, dass eine Änderung die Funktion eines anderen verfälscht hat. Beispielsweise hätte die Zinsrisikoabteilung den gültigen Zins für die übrigen Abteilungen bereitstellen sollen, aber das Feld in das es diesen geschrieben hat und die Nachkommastellen mehrmals verändert. Auf diese Weise geht zusätzliche Zeit verloren, da jede Änderung weitere abhängige Änderungen mit sich ziehen können.

Ein Excel-Architekt wird beauftragt das Projekt technisch effizienter zu gestalten, um Fortschritt zu ermöglichen und Unmut einzufangen.

Der Architekt nennt das Exceldokument (im folgenden Bank-Excel) einen Monolithen und sieht hier das Problem. Er schlägt vor es in Micro Services, also Micro-Excels, also mehrere einzelne Exceldokumente zu teilen, die technisch automatisch zusammenarbeiten.

Jede Abteilung wird fortan zusätzlich ein eigenes Exceldokument erstellen und pflegen (im folgenden Abteilungs-Excel). Zur automatisierten Zusammenarbeit wird im gemeinsamen Bank-Excel für jede Abteilung ein Arbeitsplatt erstellt für den "Input", den die jeweilige Abteilung erhält, und den "Output", den sie liefert. Exceldokumente können sowohl aus anderen Dokumenten lesen, als auch in diese Schreiben. (Falls Ihnen hier technische Probleme auffallen, ignorieren Sie diese bitte für den Zweck der Analogie.)

Der Inhalt, also die hier eingetragen Felder und deren Datenformat sind vorab vereinbart und können nicht ohne weiteres angepasst werden. Die Abteilungen haben sich somit auf Schnittstellen geeinigt.

Nun unternimmt jede Abteilung für sich mit den Eingangsdaten was nötig ist um die Ausgangsdaten zu erzeugen. Sind Zinskurven, Logik an neue Gesetzgebung, oder Stammdaten des Kunden anzupassen, so kann jede Abteilung des ohne Einbezug der anderen vornehmen.

Lediglich Änderungen am Bank-Excel, also der vereinbarten In- und Output Arbeitsblätter müssen mit allen Abteilungen abgestimmt werden.

Der Architekt wird gelobt und erfolgreich aus dem Projekt entlassen. Er hat die autonome Handlungsfähigkeit der Abteilungen wiederhergestellt und zugleich die automatisierte Zusammenarbeit mit dem Bank-Excel ermöglicht.

## Der Höhepunkt
Das Verfahren spricht sich herum, selbst der Hersteller bietet verbesserte Werkzeuge für diese Art Excel einzusetzen an. Bald werden alle Exceldokumente verteilt erstellt. Die Technologie ist sehr vielseitig und mächtig geworden. Nicht ohne Folgen: Die hausinterne IT hat das LAN der Standorte und die WAN-Verbindungen zwischen diesen mehrfach aufrüsten müssen, um dem Netzwerkverkehr zu ermöglichen.

## Der Fall
Ein Jahr später entscheidet sich die Bank auf ein anderes Excelprogramm zu setzen und im gleichen Zug vom Komma als Nachkommastellen-Trennzeichen zum Punkt zu wechseln, um International kompatibler zu sein.

Der Architekt wird erneut beauftragt, er soll den Aufwand dazu schätzen und ein Team von Beratern anbieten.

Die Aufwandschätzung ergibt: da jedes Exceldokument in bis zu 10 Teile aufgetrennt wurde, sind hier statt der 100 Bank-Excel zusätzliche 1000 Abteilungs-Excel Dokumente zu überarbeiten.

Ein zweiter Architekt wird involviert die Schätzung zu prüfen. Der Aufwand kommt allen Beteiligten enorm vor, da auf Bankebene nur 100 Exceldokumente verwendet werden.

Der zweite Architekt attestiert: durch die verteilte Architektur entstand die zehnfache Menge an Exceldokumenten und ein enormer Anstieg an Netzwerkverkehr. Man könnte deutlich die Kosten für Migrationen, Rechenleistung, Netzwerkverkehr und Datensicherung reduzieren, in dem man die Exceldokumente zentralisiert.

Die Führungsebene ist außer sich: wird man hier vom Architekt über den Tisch gezogen? Hat er diese komplexe Landschaft erschaffen, um sich später an ihnen zu bereichern?

Nach Diskussion und Verhandlung wird entschieden:
- die verteilte Architektur bleibt überall dort im Einsatz, wo sie zur organisatorischen Aufstellung der Bank passt und für Zusammenarbeit und Aktualität der Logik und Daten Vorteile bringt
- die verteilte Architektur wird an allen Stellen entfernt, in denen die Gesamthoheit über alle verteilten Exceldokumente in einer einzigen Abteilung liegt, keine Probleme durch die sequentielle Arbeit am Dokument entstehen und die Dokumente eine Maximalgröße nicht überschreiten

Die Bank prüft nun vor der Entwicklung jedes neuen Systems und während der Weiterentwicklung, ob die gewählte Architektur zum Anwendungsfall passt.

{{< embed-svg "static/svg/pros-cons.svg" >}}

## Fazit
Die Vorteile:
* Ownership dezentral
* parallele Entwicklung
* verbesserte Skalierung

kommen nicht ohne Nachteile in organisatorischer und technischer Komplexität.

Zudem sind Monolith und Micro Service nur zwei von vielen Architekturmustern, die Vorteile und Nachteile für Ihr System bieten.
