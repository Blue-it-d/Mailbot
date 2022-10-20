
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# package for open browser with given url 
# and methods for navigiate to specific page
# do some clicks and form filling
# and close browser
class control_web:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def navigiate_to(self, url):
        self.driver.get(url)

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def fill(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def close(self):
        self.driver.close()


