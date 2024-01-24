# requirements: pyyaml (pip); pandoc (os path)

import re
import os
import subprocess
import datetime
import yaml


def remove_elements(markdown_content: str) ->str:
    # Remove [ and ] from normal Markdown links, e.g., [LinkedIn](https://www....) but keep the title
    markdown_content = re.sub(r'\[([^\[\]\(\)]*?)\]\(http[s]*:\/\/[^\)]*\)', r'\1', markdown_content)

    # Remove [ and ] from email links, e.g., [E-Mail](mailto:email@domain.de) but keep the maillink
    markdown_content = re.sub(r'\[([^\[\]\(\)]*?)\]\(mailto:*[^\)]*\)', r'\1', markdown_content)

    # Remove [ and ] but not whats between
    markdown_content = markdown_content.replace('[', '').replace(']', '')

    # # Remove content between and including ({{< and >}})
    markdown_content = re.sub(r'\(\{\{< [rel]*ref (.*?) >\}\}\)', '', markdown_content)

    # Remove content between and including {{< and >}}
    markdown_content = re.sub(r'{{<.*?>}}', '', markdown_content)

    # Remove ({{< ref ... >}}) but keep content between
    markdown_content = re.sub(r'\(\{\{< ref (.*?) >\}\}\)', r'\1', markdown_content)

    markdown_content = re.sub(r'<br>', '', markdown_content)
    markdown_content = re.sub(r'&nbsp;', '', markdown_content)
    markdown_content = re.sub(r'{{< rawhtml >}}', '', markdown_content)
    markdown_content = re.sub(r'{{< /rawhtml >}}', '', markdown_content)
    markdown_content = re.sub(r'date:\s+\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', '', markdown_content)

    return markdown_content


def transform_elements(markdown_content: str, contact_data: str) -> str:
    markdown_content = re.sub(r'## Hallo, ich bin Denis', contact_data, markdown_content)

    markdown_content = re.sub(r'title: Portfolio', 'title: Portfolio Denis Malolepszy', markdown_content)

    current_date_german = datetime.datetime.now().strftime('%d.%m.%Y')
    markdown_content = re.sub(
        r'<div class="print-only" id="current-date-placeholder">Frankfurt am Main, den <span id="current-date"></span></div>',
        f'Frankfurt am Main, den {current_date_german}', markdown_content)

    return markdown_content


def main():
    try:
        with open('config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing config.yaml: {e}")
        exit(1)

    # Validate configuration
    required_keys = ['input_file_de', 'input_file_en', 'template_file', 'header_file_de', 'header_file_en',
                     'output_file_de', 'output_file_en']
    for key in required_keys:
        if key not in config:
            print(f"Error: '{key}' is missing in config.yaml.")
            exit(1)

    # Check file extensions
    file_extensions = {
        'input_file_de': '.md',
        'input_file_en': '.md',
        'template_file': '.docx',
        'header_file_de': '.md',
        'header_file_en': '.md',
        'output_file_de': '.docx',
        'output_file_en': '.docx',
    }
    for key, expected_extension in file_extensions.items():
        if not config[key].endswith(expected_extension):
            print(f"Error: '{key}' has an incorrect file extension. Expected: {expected_extension}")
            exit(1)

    input_file = config['input_file_de']
    template_file = config['template_file']
    header_file = config['header_file_de']
    output_file = config['output_file_de']

    current_date_iso8601 = datetime.datetime.now().strftime('%Y-%m-%d')

    try:
        with open(input_file, 'r') as file:
            markdown_content = file.read()

        with open(header_file, 'r') as file:
            contact_data = file.read()

        markdown_content = remove_elements(markdown_content)

        markdown_content = transform_elements(markdown_content, contact_data)

        temp_file = 'temp_markdown.md'
        with open(temp_file, 'w') as file:
            file.write(markdown_content)

        subprocess.run(
            ['pandoc', '--reference-doc=' + template_file, '-o', f'output/{current_date_iso8601} {output_file}', '-f',
             'markdown', '-t', 'docx', temp_file])

        os.remove(temp_file)

        print(f"docx conversion completed")

    except Exception as e:
        print(f"Conversion failed: {e}")


if __name__ == "__main__":
    main()
