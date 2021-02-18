from selenium import webdriver
import time
from os import system
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
cls = lambda: system('cls')

driver = webdriver.Chrome()

url = 'https://meridianbet.rs/sr/kladjenje/uzivo/fudbal'
driver.get(url)

container = driver.find_element_by_id('matches')
matches = container.find_elements_by_class_name('live-match')
print(len(matches))

for match in matches:
    time = match.find_element_by_class_name('period').get_attribute('innerHTML')
    rivals = match.find_element_by_class_name('rivals')
    results = match.find_element_by_class_name('result')
    home = rivals.find_element_by_class_name('home').get_attribute('innerHTML')
    away = rivals.find_element_by_class_name('away').get_attribute('innerHTML')
    result = results.find_element_by_class_name('home').get_attribute('innerHTML') +':' +results.find_element_by_class_name('away').get_attribute('innerHTML')
    game = match.find_element_by_class_name('game')
    games = game.find_elements_by_tag_name('live-match-game')
    try:
        one = games[0].find_element_by_tag_name('div').get_attribute('innerHTML')
        x = games[1].find_element_by_tag_name('div').get_attribute('innerHTML')
        two = games[2].find_element_by_tag_name('div').get_attribute('innerHTML')
        print(f'{time.strip():<10} {home.strip():<40} {result.strip():<10} {away.strip():<40} {one.strip():<10} {x.strip():<10} {two.strip():<10}')
    except:
        continue
driver.quit()