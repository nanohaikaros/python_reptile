from selenium import webdriver
service_args = [ '--proxy=localhost:9159', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path="phantomjs", service_args=service_args)
driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()