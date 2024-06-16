from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import uvicorn

app = FastAPI()

def get_and_modify_text_from_main_page(driver):
    page_content = driver.page_source

    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text()

    modified_text = text.replace(
        "Trying to bypass the Fluxus key system will get you banned from using Fluxus.",
        "Error Please Try Again!"
    )

    unwanted_texts = [
        "\n\n\n\n\n\n\n\n\n\n\nFluxus | Main\n\n\n\n\n\n\n\n\nEnter your key into FluxusYour Key:\n\n\t\t\t\t",
        "\t\t\t\n\n\n\nCopy Key\n\n\n\n\n"
    ]
    for unwanted in unwanted_texts:
        modified_text = modified_text.replace(unwanted, '')

    return modified_text

@app.get("/&apikey=famzzxjova/fluxus")
async def process_link_request(request: Request):
    start_time = time.time()

    link = request.query_params.get('link')

    chrome_options = Options()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)

    print("Start Bypass")
    driver.get(link)

    if link.startswith("https://flux.li/android/external/start.php?HWID="):
        driver.execute_script("window.location.replace('https://linkvertise.com/580726/fluxus1');")
        driver.execute_script("window.location.replace('https://flux.li/android/external/check1.php');")
        driver.execute_script("window.location.replace('https://linkvertise.com/580726/fluxus');")
        driver.execute_script("window.location.replace('https://flux.li/android/external/main.php');")
        driver.refresh()
    elif "main.php" in driver.current_url:
        pass

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    text = get_and_modify_text_from_main_page(driver)

    driver.quit()

    print("Successfully!")

    end_time = time.time()
    time_taken = end_time - start_time

    response = {
        "discord": "https://discord.gg/vqnMxk4ygf",
        "key": text,
        "made_by": "jova X famzzdev", 
        "time taken": f"{time_taken:.2f} seconds"
    }

    return JSONResponse(content=response)

if __name__ == '__main__':
    uvicorn.run()
