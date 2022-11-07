
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# package for open browser with given url 
# and methods for navigiate to specific page
# do some clicks and form filling
# and close browser
class selenium_object:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    # find element by the passed value (css, xpath, id, name, class)
    def find_element(self, value):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, value)
        except:
            try:
                return self.driver.find_element(By.XPATH, value)
            except:
                try:
                    return self.driver.find_element(By.ID, value)
                except:
                    try:
                        return self.driver.find_element(By.NAME, value)
                    except:
                        try:
                            return self.driver.find_element(By.CLASS_NAME, value)
                        except:
                            return "not found"


    def finde_by_css(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)
    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
    def find_by_id(self, id):
        return self.driver.find_element(By.ID, id)
    def find_by_css(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)
    

    def navigiate_to(self, url):
        self.driver.get(url)

    # click  by css selector
    def click_css(self, css):
        self.driver.find_elements(By.CSS_SELECTOR, css).click()
    # click by id
    def click_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def fill(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def fill_by_css(self, css, text):
        self.driver.find_element(By.CSS_SELECTOR, css).send_keys(text, Keys.RETURN)

    def close(self):
        self.driver.close()




# use Selemium to open browser and navigate to specific page
control_web = selenium_object()
control_web.navigiate_to("https://www.google.com")
# click 
# try catch for exception
try:
    control_web.click_id("W0wltc")
except:
    print("error")

search_element = control_web.find_element("html body div.L3eUgb div.o3j99.ikrT4e.om7nvf form div div.A8SBwf div.RNNXgb div.SDkEP div.a4bIc input.gLFyf.gsfi")
print(search_element)
search_element.send_keys("python", Keys.RETURN)
ele2 = control_web.find_element("/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[3]/div[1]")
print(ele2)
ele2.click()





 