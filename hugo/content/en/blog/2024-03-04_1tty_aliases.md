---
translationKey: 11ty-aliases
title: Configuring Page Aliases in Eleventy
heading: How to Configure Aliases for Pages with Eleventy
description: Eleventy has no built-in support for aliases. A combination of JavaScript and pagination templates provides a clean solution.
date: 2024-03-04T14:00:00+01:00
draft: false
---

The Static Site Generator Eleventy does not come with built-in support for aliases. However, through a combination of JavaScript configuration and pagination templates, it becomes manageable and maintainable to implement them.

## What is a Page Alias
An alias is an alternative name, creating another path to an existing page. An alias enables the same page to be found under different names.

## Why Use a Page Alias?
There are many practical applications or circumstances in which one might desire an additional URL that points to an existing page.

For instance, for a promotional campaign for a website *great-products.com*, one could generate a QR code that directs from *great-products.com/qr-code* to *great-products.com/index.html*.  This allows for later analysis of web server logs to determine how many visitors came to the website via the QR code. 

Or perhaps, some time ago, a popular page was created at *great-products.com/very-popular-but-really-long-URL*, and for various reasons, a shorter version like *great-products.com/top* is desired without deleting the old URL.

For all these cases, page aliases are suitable. So, let's create some!

## Step 1: Collecting Page Aliases in a Collection
Eleventy pages are defined with Frontmatter, which is the definition block at the top of each page. Depending on the technology choice, this can look different. In this example, I'm using Markdown with YAML Frontmatter.
Example:

**Example file index.md**
```markdown
---
title: My Homepage
layout: layouts/home.njk
aliases:
 - /also-the-homepage
 - /homepage
 - /qr-code
---
```

In this example, three page aliases are already included: */also-the-homepage*, */homepage*, and */qr-code*. This means that in addition to */index*, this page should also be accessible as */also-the-homepage*, */homepage*, and */qr-code*.

If you don't already have an *.eleventy.js* file in your Eleventy project root directory, create the default configuration according to the [current documentation](https://www.11ty.dev/docs/config/). Example:

**.eleventy.js**
```javascript
module.exports = function(eleventyConfig) {
  // Return your Object options:
  return {
    dir: {
      input: "views",
      output: "dist"
    }
  }
};
```

Then extend your .eleventy.js file with the following logic to collect 'aliases' from the frontmatter of all your Markdown files in a collection named frontmatterAliases. The filter statement *src/**/*.md* should be adjusted to fit your project structure.

**.eleventy.js**
```javascript
module.exports = function(eleventyConfig) {

  // Collect all aliases from frontmatter
  eleventyConfig.addCollection("frontmatterAliases", function (collectionApi) {
    const nodes = collectionApi.getFilteredByGlob("src/**/*.md");
    let frontmatterAliases = [];

    nodes.forEach(node => 
      (node.data.aliases || []).forEach(alias =>
        frontmatterAliases.push([node.data.page.url,`${alias}`])
      )
    );
    return frontmatterAliases;
  });
};

// Return your Object options:
return {
  dir: {
    input: "views",
    output: "dist"
  }
}

```

**Excerpt of my relevant project folder structure:**
```
/my-11ty-project/src/ (contains all markdown content files, like the following)
/my-11ty-project/src/index.md
/my-11ty-project/src/_includes/layouts/ (contains all layout templates, like the following):
/my-11ty-project/src/_includes/layouts/redirect.njk (created in step 3)
/my-11ty-project/src/_includes/layouts/page.njk
/my-11ty-project/.eleventy.js (created in step 1)
/my-11ty-project/redirects.njk (created in step 2)
/my-11ty-project/node-modules/
/my-11ty-project/package.json
/my-11ty-project/package-lock.json
```

## Step 2: Automatically Create a Page for Each Page Alias
In your content folder, in my case */src/*, create a template file named *redirects.njk*. I am using [Nunjucks Templates](https://mozilla.github.io/nunjucks/) in this example. The approach works equivalently with other templating engines, provided you implement the following logic:

**redirects.njk**
```markdown
---
pagination:
  data: collections.frontmatterAliases
  size: 1
  alias: redirect
permalink: "/{{redirect[1]}}/index.html"
layout: "layouts/redirect.njk"
---
```

The template ensures that for each entry in the collection *frontmatterAliases*, a page is created with the layout from the definition in */layouts/redirect.njk*. This layout follows in Step 3.

### Notes
*permalink: "/{{redirect[1]}}/index.html"* indicates that a folder and an index.html are generated for each alias. This is currently best practice in Eleventy to route both /page.html and /page to the content.

If you generate just a *permalink: "{{redirect[1]}}.html"*, Eleventy will not route */page* to the target, insisting on the *.html* suffix.

If you generate just a *permalink: "{{redirect[1]}}"*, Eleventy will route */page* to the target, but the web server (e.g., Apache) will likely not recognize the content as an HTML webpage and will deliver it as plaintext. This can be corrected for Apache with *.htaccess* overwrites, but it's not without side effects and therefore inferior to the folder solution with */pathname/index.html*.


## Step 3: Create Layout Template with Redirection
If your layouts are in a different path, adjust the path in Step 2 under *layout:* and now create *redirect.njk* at the path of your choice. Your *redirect.njk* should be located in the same folder as your index file (*index.md*).

The content of the layout should be a complete website that implements your metadata (page title, etc.), CSS, a note on the redirection, and the redirection itself. A minimal example, which is not intended for use, would be:

**redirect.njk**
```html
<html>
<head>
    <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
</head>
<body>
    <h1>Redirect</h1>
    <p>You will be redirected to <a href="{{ redirect[0] }}">{{ redirect[0] }}</a>. If your web browser does not support this, you can follow the link by clicking on it.</p>

    <script type="text/javascript">
    window.location.href = '{{ redirect[0] }}

';
  </script>
</body>
```
The variable redirect[0] contains the URL of the alias, but only the path. So, not *www.your-homepage.com/my-first-alias*, but */my-first-alias*.

I already have a base template for my Eleventy website and simply extend it with the note and redirection mechanism. 

There is no one-size-fits-all solution for HTTP redirection, so this example integrates two solutions that do not interfere with each other and should cover the majority of potential end devices.

### Redirection Technique 1: JavaScript
Works as long as JavaScript is supported on the end device. The function can be adjusted as desired, e.g., to wait X seconds before redirection.
```html
<script type="text/javascript">
    window.location.href = '{{ redirect[0] }}';
</script>
```

### Redirection Technique 2: Fallback as Head Meta Tag
Basically for all devices without JavaScript. Unfortunately, it no longer works in all browsers and can also be disabled browser-side.
```html
<head>
    <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
</head>
```

### Expandable Layout Example
Here is my complete example. In the layout file *layouts/page.njk*, Nunjucks blocks are integrated to allow for extension of interesting points. Therefore, you can also use this example and develop an equivalent *page.njk* that makes your layout expandable with Nunjuck *{block }*.

**redirect.njk**
```html
{% extends 'layouts/page.njk' %}

{% block head_extensions %}
  <meta http-equiv="refresh" content="1; URL='{{ redirect[0] }}'" />
{% endblock %}

{% block intro %}
  <div class="l-section">
    <div></div>
    <div class="l-section__75 l-stack">
      <h1>Redirect</h1>
      <p>You will be redirected to <a href="{{ redirect[0] }}">{{ redirect[0] }}</a>. If your web browser does not support this, you can follow the link by clicking on it.</p>
    </div>
  </div>
{% endblock %}
      
{% block scripts %}
  <script type="text/javascript">
    window.location.href = '{{ redirect[0] }}';
  </script>
{% endblock %}
```

## Using Aliases
To use your aliases, you can now define aliases in the frontmatter of your page definitions. Example:
```markdown
---
title: My Homepage
layout: layouts/home.njk
aliases:
 - /also-the-homepage
 - /homepage
 - /qr-code
---
```

On your next Eleventy build, or *npm start*, a page with the redirect.njk layout should now automatically be created for each of the alias definitions you have provided. If not, I recommend checking the paths again and then troubleshooting along the process chain. JavaScript is used in your *.eleventy.js* configuration, so you can add logging to see if Eleventy finds aliases and writes them to the collection if in doubt.

In the Eleventy build log, your alias creations should be visible:
```
[11ty] Writing _site/homepage/index.html from ./src/redirects.njk
[11ty] Writing _site/also-the-homepage/index.html from ./src/redirects.njk
[11ty] Writing _site/qr-code/index.html from ./src/redirects.njk
```
