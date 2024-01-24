# https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-printToPDF
import datetime
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def send_devtools_command(driver, cmd, params={}):
    resource = f"/session/{driver.session_id}/chromium/send_command_and_get_result"
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')

def print_to_pdf(driver, source_url, output_file):
    driver.get(source_url)

    # A4 paper size dimensions in inches
    a4_width_in_inches = 210 / 25.4  # Convert 210mm to inches
    a4_height_in_inches = 297 / 25.4 # Convert 297mm to inches

    print_params = {
        "landscape": False,
        "printBackground": False,
        "scale": 0.75,
        "marginBottom": 0.39,
        "marginTop": 0.39,
        "marginLeft": 0.39,
        "marginRight": 0.39,
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
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options
    )

    try:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        print_to_pdf(driver,
                     "http://dmalo.de/de/portfolio?theme=light",
                     f'output/{current_date} Portfolio Denis Malolepszy_Deutsch.pdf')

        print_to_pdf(driver,
                     "http://dmalo.de/en/portfolio?theme=light",
                     f'output/{current_date} Portfolio Denis Malolepszy_English.pdf')
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
