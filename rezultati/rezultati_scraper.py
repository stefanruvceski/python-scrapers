from selenium import webdriver
import time
import winsound
from os import system
from selenium.webdriver.chrome.options import Options
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


WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(chrome_options=chrome_options)


url = 'https://www.rezultati.com/'
driver.get(url)

tabs = driver.find_elements_by_class_name('tabs__text')
for tab in tabs:
    if tab.text == 'UŽIVO':
        tab.click()
old_scores = []
first = True
while True:
    live_scores = []
    matches = driver.find_elements_by_class_name('event__match--oneLine')
   
    for match in matches:
        try:
            event_status = match.find_element_by_class_name('event__time').text
        except:
            event_status = match.find_element_by_class_name('event__stage').find_element_by_tag_name('div').text
        if event_status != 'Kraj':
            home_team =match.find_element_by_class_name('event__participant--home').text
            away_team =match.find_element_by_class_name('event__participant--away').text
            spans =match.find_element_by_class_name('event__scores').find_elements_by_tag_name('span')
        
            scores = None
            if(len(spans)==2):
                scores = spans[0].text + ':'+ spans[1].text
            if scores != None:
                if '\n' in home_team:
                    home_team= home_team.split('\n')[1]
                if '\n' in away_team:
                    away_team= home_team.split('\n')[0]
                live_scores.append(f"{event_status:<20} {home_team:<20} {scores:<10} {away_team:<20}")
    cls()
    print(bcolors.YELLOW + 'Live matches')
    print(bcolors.YELLOW + '-'*70)
    print(f"{'time':<20} {'home':<20} {'score':<10} {'away':<20}")
    print(bcolors.YELLOW + '-'*70)
    if first:
        old_scores = live_scores
        first = False
        
    if len(live_scores) != len(old_scores):
        old_scores = live_scores
    for i in range(0,len(live_scores)):
        
        live_ind = live_scores[i].find(' ')
        old_ind = old_scores[i].find(' ')
        if live_scores[i][live_ind:] != old_scores[i][old_ind:]:
           print(bcolors.OKGREEN + live_scores[i]) 
           winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
           old_scores[i] = live_scores[i]
        else:
            print(bcolors.OKBLUE + live_scores[i]) 
    print(bcolors.YELLOW + '-'*70)
    time.sleep(5)
    
driver.quit()