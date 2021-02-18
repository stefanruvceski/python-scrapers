from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
cls = lambda: system('cls')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
if 'chrome_options'in vars(__builtins__):
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    driver = webdriver.Chrome()

url = 'https://privatni-casovi.net/sessions/new'
driver.get(url)
time.sleep(1)
email = driver.find_element_by_id('email-login-input')
email.send_keys("stefanruvceski@gmail.com")

driver.find_element_by_xpath('/html/body/main/div/div/form/div[1]/div[2]/input').click()

url = input('unesi url za prijavu: ')

#url = f'https://privatni-casovi.net/sessions/{token}/login'
driver.get(url)
time.sleep(1)
urls =  ['https://privatni-casovi.net/python/predmet',
         'https://privatni-casovi.net/c/predmet' ,
         'https://privatni-casovi.net/web-development/predmet' ,
         'https://privatni-casovi.net/objektno-orijentisano-programiranje-java-c/predmet' ,
         'https://privatni-casovi.net/baze-podataka/predmet' ,
         'https://privatni-casovi.net/iz-programiranja/predmet' ,
         'https://privatni-casovi.net/asp-net/predmet' ,
         'https://privatni-casovi.net/iz-c-i-c-plus-plusa/predmet' ,
         'https://privatni-casovi.net/informatika-i-racunarstvo/predmet'
        ]

for index in range(0,len(urls)):

    driver.get(urls[index])

    profiles = driver.find_elements_by_class_name('profile-card');

    i = 0
    for profile in profiles:
        name = profile.find_element_by_class_name('name').find_element_by_tag_name('a').text;
        i+=1
        if(name == 'Stefan Ruvceski'):
            print(f'{name} je {i} na listi za predmet {urls[index].split("/")[3]}')
            break
    
#driver.quit()