from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
#import configparser
#config = configparser.ConfigParser()
#config.read("config.ini")
#username = config['UN']['user_name']
#password = config['PW']['password']        
book_url = input("Please enter url: ")
print("Please enter log in credentials: ")
username = input("Username(Library Card Number): ")
password = input("PIN(last four digits of phone number): " )

chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument('--headless')
driver = webdriver.Chrome("./driver/chromedriver",chrome_options=chromeOptions)
#driver.get(book_url)
un = driver.find_element_by_name("user")
login_page = driver.current_url
un.send_keys(username)
pw = driver.find_element_by_name("pass")
pw.send_keys(password, Keys.RETURN)
session = driver.session_id
page = 1
title = driver.find_element_by_class_name("meta_title").text
#==============================================================================
# Removing illegal attr/chars for OSX directory names
#==============================================================================
file_name = title.replace(":","-")
if len(file_name) > 255:
    file_name = file_name[0:255]
if not os.path.exists(os.path.expanduser("~/Desktop/Scraped_Books")):
    os.mkdir(os.path.expanduser("~/Desktop/Scraped_Books"))
if not os.path.exists(os.path.expanduser("~/Desktop/Scraped_Books/%s" % (file_name))):
    os.mkdir(os.path.expanduser("~/Desktop/Scraped_Books/%s" % (file_name)))
    
def lastPage(driver):
    try:
        driver.get_element_by_class_name("navigationDisabled")
    except:
        return False
    
def firstPage(driver, page, file_name):
    WebDriverWait(driver, 10).until(lambda p: p.find_element_by_id('print'))
    driver.find_element_by_id("print").click()
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)
    dial_window = driver.window_handles[2]
    driver.switch_to_window(dial_window)
    printer = driver.find_element_by_class_name("destination-settings-name").text
    if printer != 'Save as PDF':
        driver.find_element_by_class_name("destination-settings-change-button").click()
        WebDriverWait(driver,10).until(lambda i: i.find_element_by_class_name("destination-list-item"))
        driver.find_element_by_class_name("local-list").find_element_by_class_name("destination-list-item").click()
    WebDriverWait(driver, 10).until(lambda s: s.find_element_by_class_name('print'))
    driver.find_element_by_class_name("print").click()
    cmd = """osascript -e 'tell application "Google Chrome"
        activate
        set index of window 1 to 1
        delay 2
        tell application "System Events" 
        keystroke "~/Desktop/Scraped_Books/%s"
        key code 76
        delay 1
        keystroke "%d"
        delay 1.5
        key code 76
        end tell
    end tell'""" % (file_name, page)
    return (os.system(cmd), page)

def getPages(driver, page):
    WebDriverWait(driver, 10).until(lambda p: p.find_element_by_id('print'))
    pr = driver.find_element_by_id("print").click()
    print_window = driver.window_handles[1]
    book_window = driver.window_handles[0]
    driver.switch_to_window(print_window)
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)
    dial_window = driver.window_handles[2]
    driver.switch_to_window(dial_window)
    WebDriverWait(driver, 10).until(lambda s: s.find_element_by_class_name('print'))
    driver.find_element_by_class_name("print").click()
    return page

firstPage(driver, page, file_name)
page += 1
driver.switch_to_window(driver.window_handles[1])
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_id("next").click()
while lastPage(driver) != True:
    getPages(driver,page)
    cmd = """osascript -e 'tell application "Google Chrome"
        activate
        set index of window 1 to 1
        delay 0.75
        tell application "System Events"
        keystroke "%d"
        delay 0.25
        key code 76
        end tell
    end tell'""" % (page)
    os.system(cmd)
    page += 1
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    try:
        WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id('next'))
        driver.find_element_by_id("next").click()
    except:
        print("Pages gathered")
    driver.close()
    
command = """osascript -e 'do shell script "open ~/coding/book_scraper/%s/"
delay 1
tell application "System Events"
	key code 0 using command down
	delay 1
	key code 120 using control down
	key code 124
	key code 125
	key code 1
	key code 124
	key code 76
end tell
'""" % (file_name)
os.system(command)