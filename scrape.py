from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import configparser
import os
config = configparser.ConfigParser()
config.read("config.ini")
username = config['UN']['user_name']
password = config['PW']['password']
pg_total = 0
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver",chrome_options=chromeOptions)
driver.get("http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/software-engineering-and-development/0735619670/firstchapter")
un = driver.find_element_by_name("user")
login_page = driver.current_url
un.send_keys(username)
pw = driver.find_element_by_name("pass")
pw.send_keys(password, Keys.RETURN)
session = driver.session_id
page = 1
def getPages(driver, page):
    WebDriverWait(driver, 10).until(lambda p: p.find_element_by_id('print'))
    pr = driver.find_element_by_id("print").click()
#    WebDriverWait(driver, 10).until(lambda z: len(z.window_handles) == 2)
    print_window = driver.window_handles[1]
    book_window = driver.window_handles[0]
    driver.switch_to_window(print_window)
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)
    dial_window = driver.window_handles[2]
    driver.switch_to_window(dial_window)
    printer = driver.find_element_by_class_name("destination-settings-name").text
    if printer != 'Save as PDF':
        driver.find_element_by_class_name("destination-settings-change-button").click()
#        driver.find_element_by_text("Save as PDF").click()
        driver.find_element_by_class_name("local-list").find_element_by_class_name("destination-list-item").click()
    WebDriverWait(driver, 10).until(lambda s: s.find_element_by_class_name('print'))
    driver.find_element_by_class_name("print").click()
    cmd = """osascript -e 'tell application "Google Chrome"
        activate
        set index of window 1 to 1
        tell application "System Events" to keystroke "~/coding/book_scraper/"
        tell application "System Events" to key code 76
        delay 0.75
        tell application "System Events" to keystroke "page_%d"
        delay 0.25
        tell application "System Events" to key code 76
    end tell'""" % (page)
#    os.system(cmd)
    return(os.system(cmd),page)

while pg_total < 1:
    getPages(driver,page)
    pg_total += 1
