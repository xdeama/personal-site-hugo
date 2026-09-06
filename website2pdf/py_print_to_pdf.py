import argparse
import datetime
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support.ui import WebDriverWait


def print_to_pdf(driver, source_url, output_file, dev_url=None, prod_url=None):
    driver.get(source_url)

    # After page load, replace dev URLs with prod URLs in all links.
    if dev_url and prod_url:
        js_code = f"""
            const prodUrl = '{prod_url}';
            const devHosts = ['127.0.0.1', 'localhost', 'host.docker.internal'];
            const devOriginPattern = /https?:\\/\\/(?:127\\.0\\.0\\.1|localhost|host\\.docker\\.internal)(?::\\d+)?/g;
            document.querySelectorAll('a').forEach(link => {{
              let url;
              try {{
                url = new URL(link.href);
              }} catch (e) {{
                console.error("Could not parse URL for cleanup:", link.href);
                return;
              }}
              if (!devHosts.includes(url.hostname)) return;

              // 1. Replace display text showing a dev origin
              link.textContent = link.textContent.replace(devOriginPattern, prodUrl);

              // 2. Remove 'theme' parameter and swap href origin
              url.searchParams.delete('theme');
              link.href = prodUrl + url.pathname + url.search + url.hash;
            }});
        """
        driver.execute_script(js_code)
        print(f"Rewrote dev-host links (any port) to prod URL '{prod_url}' and cleaned params.")

    # Wait for fonts to be ready to prevent race conditions
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.fonts.ready.then(() => true)'))

    print_options = PrintOptions()
    print_options.orientation = "portrait"
    print_options.background = False
    print_options.scale = 0.75
    print_options.page_width = 21.0
    print_options.page_height = 29.7

    pdf_data = base64.b64decode(driver.print_page(print_options))
    with open(output_file, "wb") as file:
        file.write(pdf_data)


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
