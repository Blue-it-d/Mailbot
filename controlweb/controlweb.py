
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# package for open browser with given url 
# and methods for navigiate to specific page
# do some clicks and form filling
# and close browser
class control_web:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def fill(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def close(self):
        self.driver.close()


# test case
if __name__ == '__main__':
    # create object of class control_web
    # and pass url as argument
    obj = control_web('https://www.google.com/')
    # call method click
    obj.click('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    # call method fill
    obj.fill('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input', 'selenium')
    # call method close