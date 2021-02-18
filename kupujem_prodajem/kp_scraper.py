from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
cls = lambda: system('cls')

# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
if 'chrome_options'in vars(__builtins__):
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()

url = 'https://www.kupujemprodajem.com/'
driver.get(url)

def login(email, password):
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/a').click()
    time.sleep(1)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('submitButton').click()
    time.sleep(1)

def input_item_name(name):
    driver.find_element_by_id('data[group_suggest_text]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/input').click()

    wait_elementid = "/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[3]"
    wait_time = 1
    WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, wait_elementid)))

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/label[1]').click()
    time.sleep(1)

def input_item_details(state,price,currency,text,images):
    if state == 'Kao novo - nekorišćeno':
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[1]').click()
    elif state == 'Korišćeno':
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[2]').click()
    elif state == 'Neispravno ili oštećeno':
         driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[4]').click()
         
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[14]/div[2]/div[1]/input').send_keys(price)
    if currency == 'din':
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[14]/div[2]/div[3]/input[1]').click()
    else:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[14]/div[2]/div[3]/input[2]').click()

    driver.switch_to.frame('data[description]_ifr')
    driver.find_element_by_xpath('/html/body').send_keys(text)
    driver.switch_to.parent_frame();

    input_images = driver.find_element_by_id('upload_file');
    for image in images:
        input_images.send_keys(f'C:\\Users\\Stefan\\Downloads\\{image}.jpg')
    
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[20]/div/input').click()
    time.sleep(3)
    
def input_promotion():
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[3]/div[2]/label[1]/div[1]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[3]/div[4]/div/input').click()
    time.sleep(1)
    
def agree_to_terms():
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[4]/div[7]/div[2]/div/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[4]/div[8]/div/input').click()
import csv

def read_from_csv(name):
    with open(f'{name}.csv', newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
         
    return data

def main():
    data = read_from_csv('prodaja')
    login('','')
    input_item_name(data[1][0])
    input_item_details(data[1][1],data[1][2],data[1][3],data[1][4],['1','2'])
    input_promotion()
    agree_to_terms()
    time.sleep(5)
    driver.quit()
    
    
if __name__ == '__main__':
    main()
