from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

LOGIN = 'your@login.com'
PWD = 'yourpassword'
URL = 'https://panel.home.pl/'


def home_downloader():
    # edge driver/options
    edge_driver_path = "msedgedriver.exe"
    service = Service(executable_path=edge_driver_path)
    options = Options()
    options.headless = True
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')
    driver = webdriver.Edge(service=service, options=options)

    # download path
    """used "\\" instead of "/" because downloading
    a file with headless mode was not possible"""
    params = {'behavior': 'allow', 'downloadPath': 'C:\\your\\path'}
    driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

    driver.get(url="https://panel.home.pl/")

    #shadow-host (open)
    time.sleep(3)
    shadow_host = driver.find_element(By.ID, "cmpwrapper")
    shadow_root = shadow_host.shadow_root
    shadow_root.find_element(By.CSS_SELECTOR, ".cmpboxbtn").click()
    
    login = driver.find_element(By.NAME, "login")
    password = driver.find_element(By.NAME, "password")

    login.click()
    # enter login
    login.send_keys(LOGIN)
    password.click()
    # enter pwd
    password.send_keys(PWD)
    # Log in
    driver.find_element(By.CSS_SELECTOR, ".o-cta__btn .a-btn").click()

    # selecting "mailboxes" element on site
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Poczta").click()
    time.sleep(5)

    """changing current frame to iframe,
    clicking exportall button, saving it to your path"""
    driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[1])
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    buttons[4].click()
    time.sleep(5)

    driver.quit()
