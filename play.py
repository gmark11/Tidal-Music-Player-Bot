from selenium import webdriver
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException


def play(name, pw, proxyin, album):  #Webdriver
    if proxyin != "Proxy":

        options = webdriver.ChromeOptions()

        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.autodetect = False
        proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = proxyin
        options.Proxy = proxy
        options.add_argument("ignore-certificate-errors")

        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://listen.tidal.com/login")
        time.sleep(3)
    else:
        driver = webdriver.Chrome()
        driver.get("https://listen.tidal.com/login")
        time.sleep(3)

    #LogIn
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div/div[1]/div/form/div/input').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div/div[1]/div/form/div/input').send_keys(name)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="recap-invisible"]/div/div').click()
    time.sleep(2)

    #No captcha
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[3]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[3]/input').send_keys(pw)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/button').click()
        time.sleep(8)

    # Captcha
    except NoSuchElementException:
        time.sleep(40)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[3]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[3]/input').send_keys(pw)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/button').click()
        time.sleep(8)

    #Find album:
    if album != "Album link":
        driver.get(album)
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/main/div[1]/div[2]/div[1]/div/header/div[2]/div[3]/button[1]').click()
        time.sleep(2)
    # Play random music:
    else:
        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div[1]/figure/div/button').click()
        time.sleep(2)
