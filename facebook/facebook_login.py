from selenium import webdriver


url = 'https://www.facebook.com/'

driver = webdriver.Chrome()
driver.get(url)

email = input('enter email: ')
password = input('enter password')

email_input = driver.find_element_by_xpath('//*[@id="email"]')
password_input = driver.find_element_by_xpath('//*[@id="pass"]')

email_input.send_keys(email)
password_input.send_keys(password)

driver.find_element_by_xpath('//*[@id="u_0_b"]').click()