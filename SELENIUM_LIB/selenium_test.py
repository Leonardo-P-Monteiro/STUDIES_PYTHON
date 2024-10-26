from pathlib import Path
import time
import selenium
import selenium.webdriver
import selenium.webdriver.chrome
import selenium.webdriver.chrome.service
import selenium.webdriver.common.by
import selenium.webdriver.common.keys
import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.wait
import selenium.webdriver.support




TIME_TO_WAIT = 10
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'CHROME_DRIVER' / 'chromedriver.exe'
# CHROMEDRIVER_EXEC = 'C:\\Users\\leona\\Documents\\STUDIES_PYTHON\\SELENIUM_LIB\\CHROME_DRIVER\\chromedriver.exe'

# chrome_options = selenium.webdriver.ChromeOptions()
# chrome_services = selenium.webdriver.chrome.service.Service(executable_path=\
# CHROMEDRIVER_EXEC) #type:ignore
# chrome_browser = selenium.webdriver.Chrome(
#     service=chrome_services,
#     # options= chrome_options,
# )


# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)


# FUNCTION CHROME
def make_chrome_browser(*options: str) -> selenium.webdriver.Chrome:
    chrome_options = selenium.webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore
    chrome_service = selenium.webdriver.chrome.service.Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )
    browser = selenium.webdriver.Chrome(
        service=chrome_service, #type: ignore
        options=chrome_options
    )
    return browser


options = ()
browser = make_chrome_browser(*options)
browser.get('https://www.google.com.br/')




# ESPERANDO PARA ENCONTRAR O INPUT

search_input = selenium.webdriver.support.wait.WebDriverWait(browser,
TIME_TO_WAIT).until(
    selenium.webdriver.support.expected_conditions.presence_of_element_located((selenium.webdriver.common.by.By.NAME, 'q'))
    ) 

search_input.send_keys('amazon')
search_input.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

results = browser.find_element(selenium.webdriver.common.by.By.ID, 'search')
link = results.find_elements(selenium.webdriver.common.by.By.TAG_NAME, 'a')
link[0].click()

into_site = browser.find_element(selenium.webdriver.common.by.By.ID, 'twotabsearchtextbox')
into_site.send_keys('livro história do brasil')
into_site.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

time.sleep(10)

print('passou 1')
item_shop = into_site.find_element(selenium.webdriver.common.by.By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/span/div/div/div[2]/div[1]/h2/a')
print('passou 2')
item_choice = item_shop.find_elements(selenium.webdriver.common.by.By.TAG_NAME, 'a')
item_choice[0].click()


time.sleep(TIME_TO_WAIT)