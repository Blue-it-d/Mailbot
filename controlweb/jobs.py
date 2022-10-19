
# Function to add user data in form and submit with selenium
def add_user_data(driver, user):
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/div[1]/input').send_keys(user['name'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/div[2]/input').send_keys(user['email'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/div[3]/input').send_keys(user['password'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/div[4]/input').send_keys(user['password'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/div[5]/button').click()


