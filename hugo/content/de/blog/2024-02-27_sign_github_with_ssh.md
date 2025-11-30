---
translationKey: githubSshSignature
title: GitHub Commits mit SSH statt GPG signieren
heading: GitHub Commits mit SSH statt GPG signieren
description: GitHub Commits mit dem selben SSH Schlüssel signieren, mit dem sie übermittelt werden.
date: 2024-02-27T14:00:00+01:00
draft: false
---

Falls Sie mitdiskutieren möchten, ob das signieren von Commits überhaupt Sinn macht, könnte Ihnen dieser Artikel weiterhelfen: [https://dlorenc.medium.com/should-you-sign-git-commits-f068b07e1b1f](https://dlorenc.medium.com/should-you-sign-git-commits-f068b07e1b1f).

Meine Antwort war ja, ich möchte signieren, aber das Verwalten eines zusätzlichen Schlüssels pro Git Hosting Platform ist nervig.

Glücklicherweise erlaubt GitHub das signieren mit dem SSH Schlüssel, den ich ohnehin für die Verwaltung meiner Git Repositories verwende. Das ganze ist zudem in weniger als fünf Minuten eingerichtet!

## Auf Ihrem Endgerät konfigurieren

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/<your public key name>.pub
```
Achten Sie auf die Dateiendung *.pub*. Niemals den Private Key verwenden. Falls Sie Ihren Private Key versehentlich irgendwo verwendet haben, beispielsweise bei GitHub als SSH Key registriert, so erzeugen Sie einen neuen. Zur Sicherheit.

Die Option *--global* konfiguriert für alle Git Repositories auf Ihrem Endgerät. Falls Sie verschiedene Konfigurationen benötigen, lassen Sie --global weg und setzen Sie die Option pro Repository, oder entwickeln Sie eine komplexere Konfiguration für Ihren persönlichen Bedarf.

Falls Sie weitere Informationen benötigen, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/managing-commit-signature-verification)

## In GitHub konfigurieren
Wenn Sie Ihren SSH Public Key ebenfalls für die Signatur verwenden möchten, müssen Sie den Key doppelt bei GitHub hinterlegen: als Authentication Key und als Signing Key.

Fügen Sie Ihren Public Key als neuen Signing Key hinzu unter [https://github.com/settings/keys](https://github.com/settings/keys)

Klicken Sie in der Rubrik "SSH Keys" auf "new SSH Key", dann wählen Sie als Key type "Signing Key".

Falls Sie weitere Informationen benötigen, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## Commits signieren
Per default signiert ein **git commit** nicht.

Signieren Sie per Option "-S" bei jedem Commit
```bash
git commit -S
```

oder konfigurieren Sie das Signieren für alle Commits

```bash
git config --global commit. gpgsign true
```

Falls Sie weitere Informationen benötigen, siehe [GitHub Dokumentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
