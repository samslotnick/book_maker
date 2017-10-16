# About:
Most of Toronto Public Library's eBooks are hosted on a site that is pretty unbearable to navigate and doesn't allow a user to print more than one page at a time. This project seeks to remedy that by automatically cycling through each page, saving them as a pdf in a directory under the book's name.
### Progress:
At the moment this only supports Toronto Public Library eBooks (published) before 2017 and any others hosted on SafariBooksOnline. The webdriver is currently not "headless," because I am working out various kinks--it's easier to see problems with a head on. Headless version coming as soon as Node and Puppeteer.
Currently only works on MacOS
## Use:
* Clone repo
* `pip install selenium`
* install 'merge_pdfs' service
* `$python scrape.py`
