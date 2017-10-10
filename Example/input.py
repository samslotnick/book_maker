import configparser
config = configparser.ConfigParser()
config.read("config.ini")
username = config['UN']['user_name']
password = config['PW']['password']
book_url = "http://proquestcombo.safaribooksonline.com.ezproxy.torontopubliclibrary.ca/book/programming/python/9781449357009/firstchapter"
