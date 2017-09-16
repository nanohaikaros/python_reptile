from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path="phantomjs")
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameFiled = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

### 方法1 ###
firstnameFiled.send_keys('Ryan')
lastnameField.send_keys('Mitchell')
submitButton.click()
################

### 方法2 ###
actions = ActionChains(driver).click(firstnameFiled).send_keys('Ryan').click(lastnameField).send_keys('Mitchell').send_keys(Keys.RETURN)
actions.perform()
################

print(driver.find_element_by_tag_name('body').text)

driver.close()