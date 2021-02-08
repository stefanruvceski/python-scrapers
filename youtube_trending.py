from selenium import webdriver
import urllib.request,os,csv
from datetime import datetime
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.youtube.com/feed/trending'
driver.get(url)

container = driver.find_elements_by_id('grid-container')
blocks = container[0].find_elements_by_tag_name('ytd-video-renderer')
#print('Trending')
#print('-'*20)
#i = 1


trending = []
for block in blocks:
    link = block.find_element_by_tag_name('a').get_attribute('href')
    title = block.find_element_by_id('title-wrapper').text
    views = block.find_element_by_id('metadata-line').find_elements_by_tag_name('span')[0].text
    #img = block.find_element_by_class_name('yt-img-shadow').get_attribute('src')
    #print(img)
    
    # urllib.request.urlretrieve(img, f"Images/{i}.jpg")
    #i+=1
    trending.append([views,title,link])
    #print(f'{views} - {title} - {link}')
    
    
    
#print()

#print('Recently trending')
#print('-'*20)
recently_trending =[]
blocks = container[1].find_elements_by_tag_name('ytd-video-renderer')
for block in blocks:
    link = block.find_element_by_tag_name('a').get_attribute('href')
    title = block.find_element_by_id('title-wrapper').text
    views = block.find_element_by_id('metadata-line').find_elements_by_tag_name('span')[0].text
    recently_trending.append([views,title,link])
    #print(f'{views} - {title} - {link}')
    

try:    
    os.mkdir(f'{datetime.today().strftime("%d-%m-%Y")}')
except:
    pass
with open(f'{datetime.today().strftime("%d-%m-%Y")}/trending_.csv', 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Views','Title','Link'])
    for trend in trending:
        writer.writerow(trend)
        
with open(f'{datetime.today().strftime("%d-%m-%Y")}/recently_trending.csv', 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Views','Title','Link'])
    for trend in recently_trending:
        writer.writerow(trend)
        
print('Done')
driver.quit()