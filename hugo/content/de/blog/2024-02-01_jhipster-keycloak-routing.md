---
translationKey: jhkcrouting
title: jHipster Routingprobleme mit Keycloak in der Entwicklungsumgebung beheben
heading: Behebung von Routing-Fehlern bei der lokalen Entwicklung von jHipster mit Keycloak
description: Behebung von Routing-Fehlern in der lokalen Entwicklungsumgebung mit JHipster und Keycloak
date: 2024-02-01T14:59:59+01:00
draft: false
---

Verwendet man [jHipster](https://www.jhipster.tech) zur Generierung von Microservices mit Keycloak und führt seine Infrastruktur lokal auf einer Entwicklungsmaschine in Docker aus, so können Routing-Fehler auftreten, bei denen Keycloak vom Webbrowser nicht erkannt wird.

Der jHipster Anmeldelink leitet zu einer URL weiter, die wie folgt aufgebaut ist:
> http://keycloak:9080/realms/jhipster/protocol/openid-connect/auth?...

Dies wird fehlschlagen, wenn *keycloak* der DNS Auflösung des lokalen Systems unbekannt ist.

Docker verwendet Dienstnamen wie 'keycloak' für die interne Kommunikation zwischen Diensten. Webbrowser verstehen jedoch diese internen Dienstnamen nicht von Natur aus, was zu Routing-Fehlern führt, wenn der Versuch unternommen wird, auf Keycloak zuzugreifen.

Wenn dieses Problem behoben wird, indem *keycloak* manuell durch *localhost* in der URL-Leiste des Browsers ersetzt wird, wird dies wahrscheinlich die Anmeldung ermöglichen, aber beim Rückgabepfad vom Keycloak zur Webapp wird folgender Fehler auftreten:

> Anmeldung mit OAuth 2.0
> 
> Ungültige Anmeldeinformationen
> 
> http://keycloak:9080/realms/jhipster

Üblicherweise wird vorgeschlagen dieses Problem durch das Hinzufügen eines Eintrags zur Hosts-Datei des Hostsystems zu lösen, also der Entwicklermaschine auf der Docker läuft. Dies kann auf Geräten des Arbeitgebers oder Auftraggebers jedoch nicht möglich sein. Es gibt eine einfache alternative Lösung.

Um die Hosts-Datei nicht ändern zu müssen, kann eine elegantere Methode verwendet werden, indem ein Webbrowser mit Optionen zur Überschreibung der Hostauflösung genutzt wird, wie zum Beispiel Chromium. Auf macOS mit installiertem Chromium sollte der folgende Terminalbefehl verwendet werden können, um eine Chromium-Sitzung zu öffnen, die die Hostauflösung für 'keycloak' auf 'localhost' überschreibt:

```zsh
chromium --host-resolver-rules="MAP keycloak localhost" http://localhost:8081
```

Mit diesem Befehl wird Chromium so konfiguriert, dass es 'keycloak' erkennt und die Anfrage stattdessen an 'localhost' weiterleitet. Dadurch werden die meisten Routing-Fehler beim Zugriff auf Keycloak über die von jHipster generierte Webanwendung beseitigt.

Es sollte darauf geachtet werden, Chromium zuvor vollständig zu schließen, bevor es über das Terminal gestartet wird, da es die Hostauflösungsregeln in einer laufenden Sitzung möglicherweise nicht akzeptiert.
```
