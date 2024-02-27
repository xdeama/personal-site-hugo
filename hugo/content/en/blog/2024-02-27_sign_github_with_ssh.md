---
translationKey: githubSshSignature
title: Signing GitHub Commits with SSH Instead of GPG
heading: Signing GitHub Commits with SSH Instead of GPG
description: Sign GitHub commits with the same SSH key as you use for push, instead of GPG.
date: 2024-02-27T14:00:00+01:00
draft: false
---

If you're interested in discussing whether signing commits makes sense at all, this article might help you: [https://dlorenc.medium.com/should-you-sign-git-commits](https://dlorenc.medium.com/should-you-sign-git-commits-f068b07e1b1f).

My answer was yes, I want to sign, but managing an additional key for each Git hosting platform was tedious.

Fortunately, GitHub allows signing with the SSH key that I already use for managing my Git repositories. Moreover, the whole setup takes less than five minutes!

## Configure on Your Device

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/<your public key name>.pub
```
Pay attention to the file extension *.pub*. Never use the private key. If you have accidentally used your private key somewhere, for example, registered it at GitHub as an SSH key, generate a new one. Just to be safe.

The option *--global* configures for all Git repositories on your device. If you need different configurations, omit --global and set the option per repository, or develop a more complex configuration for your personal needs.

If you need more information, see [GitHub Documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification)

## Configure in GitHub
If you want to use your SSH public key for signing as well, you must register the key twice with GitHub: as an Authentication Key and as a Signing Key.

Add your public key as a new signing key at [https://github.com/settings/keys](https://github.com/settings/keys)

Click on "new SSH Key" in the "SSH Keys" section, then choose "Signing Key" as the key type.

If you need more information, see [GitHub Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## Signing Commits
By default, a **git commit** does not sign.

Sign with the option "-S" for each commit
```bash
git commit -S
```

or configure signing for all commits

```bash
git config --global commit.gpgsign true
```

If you need more information, see [GitHub Documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)