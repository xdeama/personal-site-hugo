---
translationKey: jhkcrouting
title: Fixing jHipster Keycloak Local Routing Issues
heading: Fixing jHipster Local Development Keycloak Routing Errors
description: Fixing local dev environment Keycloak routing errors with jHipster by adjusting browser settings.
date: 2024-02-01T14:59:59+01:00
draft: false
---

When using [jHipster](https://www.jhipster.tech) to generate a service that relies on Keycloak for authorization and running your infrastructure with Docker Compose locally, you might encounter routing errors due to Keycloak not being recognized by your web browser. 

The login link will try to route you a URL like
> http://keycloak:9080/realms/jhipster/protocol/openid-connect/auth?...

Which will fail, since keycloak is unknown to your DNS.

Docker uses service names like *keycloak* for internal communication between services. However, web browsers don't inherently understand these internal service names, leading to routing errors when trying to access Keycloak.

If you're fixing this by replacing keycloak with localhost manually in your browsers URL bar, you'll likely be able to login but fail on the return URL with

> Login with OAuth 2.0
> 
> Invalid credentials
> 
> http://keycloak:9080/realms/jhipster

Typically, you'd solve this by adding an entry to your system's hosts file, but this can be inconvenient or restricted on work machines. There is a straightforward alternative solution.

To avoid modifying your hosts file, you can use a more elegant workaround using a webbrowser with host resolver overwrite options, like Chromium. On macOS with Chromium installed, you should be able to use this terminal command to open a Chromium Session with its own host resolver overwrite for *keycloak* to *localhost*:

```zsh
chromium --host-resolver-rules="MAP keycloak localhost" http://localhost:8081
```

This command configures Chromium to recognize *keycloak* and relay the request to *localhost* instead. This eliminates most routing errors when accessing Keycloak through your jHipster-generated web app.

Close Chromium completely before launching it via terminal, as it may not accept the host resolver rules in a running session.
