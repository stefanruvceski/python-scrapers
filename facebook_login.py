from selenium import webdriver


url = 'https://www.facebook.com/'

driver = webdriver.Chrome()
driver.get(url)

username = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

username.send_keys("email")
password.send_keys("password")

driver.find_element_by_xpath('//*[@id="u_0_b"]').click()