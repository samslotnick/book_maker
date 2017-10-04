from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
username = config['UN']['user_name']
password = config['PW']['password']
pg_total = 0
chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument('--disable-print-preview')
driver = webdriver.Chrome("/Users/samslotnick/coding/book_scraper/chromedriver",chrome_options=chromeOptions)
driver.get("http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/operating-systems-and-server-administration/linux/9781785888427/kali-linux-2-assuring-security-by-penetration-testing-third-edition/toc_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODU4ODg0MjclMkZjb3Zlcl9odG1sJnF1ZXJ5PXBhZ2UlMjB2aWV3cw==")
un = driver.find_element_by_name("user")
un.send_keys(username)
pw = driver.find_element_by_name("pass")
pw.send_keys(password, Keys.RETURN)
#title = driver.find_element_by_name("title")
pages = []
def getPages(driver, pages):
    pr = driver.find_element_by_id("print").click()
    print_window = driver.window_handles[1]
    book_window = driver.window_handles[0]
    driver.switch_to_window(print_window)
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 3)
    dial_window = driver.window_handles[2]
    driver.switch_to_window(dial_window)
    driver.find_element_by_class_name("cancel").click()
    driver.switch_to_window(print_window)
    pg_url = driver.current_url
    pages.append(pg_url)
    driver.close()
    driver.switch_to_window(book_window)
    driver.find_element_by_id("next").click()
    return pages

while pg_total < 10:
    getPages(driver,pages)
    pg_total += 1

import pdfkit
wkhtmlopdf_path = './wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
pdfkit.from_url('http://www.primewire.ag/?tv','out.pdf')
#if driver.find_element_by_class_name("destination-settings-name").text != "Save as PDF":
#    driver.find_element_by_class_name("destination-settings-change-button").click()
#px = driver.find_element_by_class_name("print").click()
#pyautogui.PAUSE = 10
#pyautogui.keyDown('return')
#try:
#    WebDriverWait(driver, 5).until(EC.alert_is_present(), "waiting")
#    alert = driver.switch_to_alert()
#    alert.accept()
#    print("working")
#    
#except TimeoutException:
#    print("nope")
#pr_set.find_element_by_class_name("destination-settings-name")
#if pr_set != 
#print_dial = driver.switch_to_alert()

#element = driver.find_element_by_id("print")
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
#first_page = "http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/operating-systems-and-server-administration/linux/9781785888427/kali-linux-2-assuring-security-by-penetration-testing-third-edition/toc_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODU4ODg0MjclMkZjb3Zlcl9odG1sJnF1ZXJ5PXBhZ2UlMjB2aWV3cw=="
#ref_page = urlopen(first_page)
#soup2 = BeautifulSoup(ref_page, 'html.parser')
#printz = soup2.find_all("a")
#print(soup2)
#print(x)
#<a class="next" id="next" accesskey="3" href="/9781785888427/index_html" title="Next (Key: 3)">Next (Key: 3)</a>
#<a class="print" id="print" href="#" title="Print">Print</a>
#http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/operating-systems-and-server-administration/linux/9781785888427/kali-linux-2-assuring-security-by-penetration-testing-third-edition/toc_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODU4ODg0MjclMkZpbmRleF9odG1sJnF1ZXJ5PXBhZ2UlMjB2aWV3cw==
#http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/operating-systems-and-server-administration/linux/9781785888427/kali-linux-2-assuring-security-by-penetration-testing-third-edition/toc_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODU4ODg0MjclMkZjb3Zlcl9odG1sJnF1ZXJ5PXBhZ2UlMjB2aWV3cw==
#driver.switch_to_frame(driver.find_element_by_id("print-preview"))
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.frame_to_be_available_and_switch_to_it(driver.window_handles[1]))
#element2 = wait.until(EC.frame_to_be_available_and_switch_to_it(driver.window_handles[2]))
#x = False
#while x == False:
#    try:
#        dial_window = driver.window_handles[2]
#    except IndexError:
#        continue
#    if dial_window != NoneType:
#        x = True
##while dial_load == False:
#    try:
#        dial_window = driver.window_handles[2]
#    except IndexError: