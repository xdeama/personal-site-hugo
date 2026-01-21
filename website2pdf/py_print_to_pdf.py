# https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-printToPDF
import argparse
import datetime
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def send_devtools_command(driver, cmd, params=None):
    if params is None:
        params = {}
    resource = f"/session/{driver.session_id}/chromium/send_command_and_get_result"
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')


def print_to_pdf(driver, source_url, output_file, dev_url=None, prod_url=None):
    driver.get(source_url)

    # After page load, replace dev URLs with prod URLs in all links
    if dev_url and prod_url:
        js_code = f"""
            const links = document.querySelectorAll('a');
            links.forEach(link => {{
              // Check if the link starts with the dev_url
              if (link.href.startsWith('{dev_url}') || link.href.startsWith('http://127.0.0.1:1313')) {{
                
                // 1. Replace text content (display text) if it contains the dev_url
                if (link.textContent.includes('http://127.0.0.1:1313')) {{
                    link.textContent = link.textContent.replace('http://127.0.0.1:1313', '{prod_url}');
                }}
                if (link.textContent.includes('{dev_url}')) {{
                    link.textContent = link.textContent.replace('{dev_url}', '{prod_url}');
                }}
        
                // 2. Remove 'theme' parameter and swap href
                try {{
                    // Create a URL object to safely manipulate params
                    const urlObj = new URL(link.href);
                    
                    // Remove the specific parameter
                    urlObj.searchParams.delete('theme');
        
                    // Update the link href: convert back to string and swap domains
                    link.href = urlObj.toString().replace('{dev_url}', '{prod_url}').replace('http://127.0.0.1:1313', '{prod_url}');
                    
                }} catch (e) {{
                    console.error("Could not parse URL for cleanup:", link.href);
                }}
              }}
            }});
        """
        driver.execute_script(js_code)
        print(f"Replaced dev URL '{dev_url}' with prod URL '{prod_url}' and cleaned params in links.")

    # Wait for fonts to be ready to prevent race conditions
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.fonts.ready.then(() => true)'))

    # A4 paper size dimensions in inches
    a4_width_in_inches = 210 / 25.4  # Convert 210mm to inches
    a4_height_in_inches = 297 / 25.4  # Convert 297mm to inches

    print_params = {
        "landscape": False,
        "printBackground": False,
        "scale": 0.75,
        # 0.39 is default for Chrome in image seleniarm/standalone-chromium:124.0
        #  "marginBottom": 0.39,
        #   "marginTop": 0.39,
        #   "marginLeft": 0.39,
        #   "marginRight": 0.39,
        "ignoreCache": True,
        "paperWidth": a4_width_in_inches,
        "paperHeight": a4_height_in_inches,
    }

    result = send_devtools_command(driver, "Page.printToPDF", print_params)

    # Ensure 'result' is a dictionary and has the 'data' key
    if isinstance(result, dict) and 'data' in result:
        pdf_data = base64.b64decode(result['data'])
        with open(output_file, "wb") as file:
            file.write(pdf_data)
    else:
        print("Error: Unexpected result structure or 'data' key not found")


def main():
    parser = argparse.ArgumentParser(description='Generate PDF from a webpage.')
    parser.add_argument('--dev-url', required=True, help='The URL of the development server.')
    parser.add_argument('--prod-url', required=True, help='The public URL of your production website.')
    args = parser.parse_args()

    DEV_SERVER_URL = args.dev_url
    PROD_SERVER_URL = args.prod_url

    current_date_iso_8601 = datetime.datetime.now().strftime('%Y-%m-%d')

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=chrome_options
    )

    try:
        print_to_pdf(driver,
                     f"{DEV_SERVER_URL}/de/portfolio?theme=light",
                     f'output/{current_date_iso_8601} Portfolio Denis Malolepszy_Deutsch.pdf',
                     DEV_SERVER_URL,
                     PROD_SERVER_URL)

        print_to_pdf(driver,
                     f"{DEV_SERVER_URL}/en/portfolio?theme=light",
                     f'output/{current_date_iso_8601} Portfolio Denis Malolepszy_English.pdf',
                     DEV_SERVER_URL,
                     PROD_SERVER_URL)

        print("pdf conversion completed")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
