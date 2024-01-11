import re
import os
import subprocess
import datetime

# Define the input and output file paths
input_file = 'hugo/content/de/portfolio/_index.md'
output_file = 'printable.docx'

# Read the input Markdown file
with open(input_file, 'r') as file:
    markdown_content = file.read()

# Define a function to remove specified elements from the Markdown content
def remove_elements(markdown_content):
    # Remove [ and ] from normal Markdown links, e.g., [LinkedIn](https://www.linkedin.com/in/dmalolepszy)
    markdown_content = re.sub(r'\[([^\[\]\(\)]*?)\]\(http[s]*:\/\/[^\)]*\)', r'\1', markdown_content)

    # Remove [ and ] from email links, e.g., [E-Mail](mailto:kontakt@dmalo.de)
    markdown_content = re.sub(r'\[([^\[\]\(\)]*?)\]\(mailto:*[^\)]*\)', r'\1', markdown_content)

    # Remove [ and ]
    markdown_content = markdown_content.replace('[', '').replace(']', '')

    # # Remove content between ({{< and >}})
    markdown_content = re.sub(r'\(\{\{< [rel]*ref (.*?) >\}\}\)', '', markdown_content)

    # Remove content between {{< and >}}
    markdown_content = re.sub(r'{{<.*?>}}', '', markdown_content)

    # Remove ({{< ref ... >}})
    markdown_content = re.sub(r'\(\{\{< ref (.*?) >\}\}\)', r'\1', markdown_content)

    # Remove content between {{< and >}}
    markdown_content = re.sub(r'<br>', '', markdown_content)
    markdown_content = re.sub(r'&nbsp;', '', markdown_content)
    markdown_content = re.sub(r'{{< rawhtml >}}', '', markdown_content)
    markdown_content = re.sub(r'{{< /rawhtml >}}', '', markdown_content)
    markdown_content = re.sub(r'date:\s+\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', '', markdown_content)

    markdown_content = re.sub(r'title: Portfolio', 'title: Portfolio Denis Malolepszy', markdown_content)

    current_date = datetime.datetime.now().strftime('%d.%m.%Y')
    markdown_content = re.sub(r'<div class="print-only">Frankfurt am Main, den <span id="current-date"></span></div>', f'Frankfurt am Main, den {current_date}', markdown_content)


    return markdown_content

# Add additional content
additional_content = """# Full Stack Developer & Software-Architekt — Java & Cloud Native

Website: https://www.dmalo.de

E-Mail: kontakt@dmalo.de

LinkedIn: https://www.linkedin.com/in/dmalolepszy

Anschrift: Denis Malolepszy Software Engineering, Postfach 62 01 39, 60350 Frankfurt

Résumé: https://dmalo.de/de/about/printable (Dieses Dokument als Webseite)

## Hallo, ich bin Denis"""
markdown_content = re.sub(r'## Hallo, ich bin Denis', additional_content, markdown_content)

# Remove specified elements from the Markdown content
markdown_content = remove_elements(markdown_content)

# Write the modified Markdown content to a temporary file
temp_file = 'temp_markdown.md'
with open(temp_file, 'w') as file:
    file.write(markdown_content)

# Convert the modified Markdown to DOCX using Pandoc
subprocess.run(['pandoc', '-o', output_file, '-f', 'markdown', '-t', 'docx', temp_file])

# Clean up temporary file
os.remove(temp_file)

print(f"Conversion completed. Output file: {output_file}")
