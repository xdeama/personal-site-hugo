---
translationKey: githubSshSignature
title: GitHub Commits mit SSH statt GPG signieren
heading: GitHub Commits mit SSH statt GPG signieren
description: GitHub Commits können mit dem selben SSH Schlüssel signiert werden, mit dem sie gepusht werden
date: 2024-02-27T14:00:00+01:00
draft: false
---

Falls du mitdiskutieren möchtest, ob das signieren von Commits überhaupt Sinn macht, könnte dir dieser Artikel weiterhelfen: [https://dlorenc.medium.com/should-you-sign-git-commits](https://dlorenc.medium.com/should-you-sign-git-commits-f068b07e1b1f).

Meine Antwort war ja, ich möchte signieren, aber das Verwalten eines zusätzlichen Schlüssels pro Git Hosting Platform nervig.

Glücklicherweise erlaubet GitHub das signieren mit dem SSH Schlüssel, den ich ohnehin für die Verwaltung meiner Git Repositories verwende. Das ganze ist zudem in weniger als fünf Minuten eingerichtet!

## Auf deinem Endgerät konfigurieren

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/<your public key name>.pub
```
Achte auf die Dateiendung *.pub*. Niemals den Private Key verwenden. Falls du deinen Private Key versehentlich irgendwo verwendet hast, beispielsweise bei GitHub als SSH Key registriert, so erzeuge einen neuen. Zur Sicherheit.

Die Option *--global* konfiguriert für alle Git Repositories auf deinem Endgerät. Falls du verschiedene Konfigurationen benötigst, lass --global weg und setze die Option pro Repository, oder entwickle eine komplexere Konfiguration für deinen persönlichen Bedarf.

Falls du weitere Informationen benötigst, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/managing-commit-signature-verification)

## In GitHub konfigurieren
Wenn du deinen SSH Public Key ebenfalls für die Signatur verwenden möchtest, musst du den Key doppelt bei GitHub hinterlegen: als Authentication Key und als Signing Key.

Füge deinen Public Key als neuen Signing Key hinzu unter [https://github.com/settings/keys](https://github.com/settings/keys)

Clicke in der Rubruk "SSH Keys" auf "new SSH Key", dann wähle als Key type "Signing Key".

Falls du weitere Informationen benötigst, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## Commits signieren
Per default signiert ein **git commit** nicht.

Signiere per Option "-S" bei jedem Commit
```bash
git commit -S
```

oder konfiguriere das Signieren für alle Commits

```bash
git config --global commit. gpgsign true
```

Falls du weitere Informationen benötigst, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)