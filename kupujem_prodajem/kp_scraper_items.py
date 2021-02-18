from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,csv,ssl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




def login(driver,email, password):
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[9]/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/a').click()
    time.sleep(1)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('submitButton').click()
    time.sleep(1)

def input_item_name(driver,name):
    driver.find_element_by_id('data[group_suggest_text]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/input').click()

    wait_elementid = "/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[3]"
    wait_time = 1
    WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, wait_elementid)))

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/label[1]').click()
    time.sleep(1)

def input_item_details(driver,state,price,din,text,images):
    if state == 'novo':
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[1]').click()
    elif state == 'korisceno':
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[2]').click()
    elif state == 'neispravno':
         driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[13]/div[2]/div[1]/input[4]').click()
         
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[2]/div[2]/div[14]/div[2]/div[1]/input').send_keys(price)
    if din == True:
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
    
def input_promotion(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[3]/div[2]/label[1]/div[1]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[3]/div[4]/div/input').click()
    time.sleep(1)
    
def agree_to_terms(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[4]/div[7]/div[2]/div/div/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div/div/div[4]/div[8]/div/input').click()

            
    
def get_all_links(driver):
    items =[]
    end = False
    while True: 
        pages = driver.find_element_by_class_name('pagesList').find_elements_by_tag_name('li')
        pages_num = len(pages)
        page = pages[pages_num-1]
        if end:
            break
        if page.text != 'Sledeća >':
            end = True
        
        time.sleep(1)
        elements = driver.find_elements_by_class_name('adName')
        for el in elements:
            items.append([el.get_attribute('href')])
            
        page.click()
    print(len(items))
    print(items)
    write_to_csv('links',items)
    
def write_to_csv(name,items):
    with open(f'{name}.csv', 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in items:
            writer.writerow(item)
def read_from_csv(name):
    with open(f'{name}.csv', newline='',encoding='utf-8') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     links = []
     for row in reader:
         links.append(row)   
         
    return links 

def get_details_from_links(driver,links):
    items = []
    i = 0
    items.append(['name','state','price','currency','text','category','subcategory'])
    for link in links:
        item = []
        driver.get(link)
        time.sleep(0.2)
        #name
        item.append(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/section/div[1]/div[1]').text)
        #state
        try:
            item.append(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/section/div[1]/div[2]').text[1:-1])
        except:
            item.append('nepoznato')
        
        price_currency = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/section/div[3]/div[2]/div[1]').text
        #price
        if '.' in price_currency:
            price = int(price_currency.split(' ')[1].replace('.', ''))
        elif ',' in price_currency:
            price = int(price_currency.split(' ')[1].replace(',', ''))/100
        #currency
        currency = price_currency.split(' ')[2]
        
        item.append(price)
        item.append(currency)
        #text
        item.append(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/section/div').text)
        #category                                 '/html/body/div[1]/div/div[3]/div/div/div[2]/section/div/div/div[1]/span/div[1]/a[1]
        item.append(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/section/div/div/div[1]/span/div[1]/a[1]').text)
        #subcategory
        item.append(driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/section/div/div/div[1]/span/div[1]/a[2]').text)
        items.append(item)
        i+=1
        print(i)
    return items

def create_headless_driver(headless):
    if headless:
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        return webdriver.Chrome(chrome_options=chrome_options)
    else:
        return webdriver.Chrome()

def main():
    email = input('unesite email: ')
    password = input('unesite lozinku: ')
    
    driver = create_headless_driver(False)
    url = 'https://www.kupujemprodajem.com/'
    driver.get(url)
    
    login(driver,email,password)
    
    #get_all_links()
    links = read_from_csv('links')
    
    items = get_details_from_links(driver,links)
    write_to_csv('prodaja',items)
        
   
    print('-'*20)
    print('KRAJ')
    print('-'*20)
    driver.quit()
    
    
if __name__ == '__main__':
    main()
