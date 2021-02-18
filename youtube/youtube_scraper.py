from selenium import webdriver
import time
url = 'https://www.youtube.com/'

browser = webdriver.Chrome()
browser.get(url)



    
    
    
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser.execute_script("return document.documentElement.scrollHeight")

links =[]
while True:
    contents = browser.find_elements_by_id('content')
    for content in contents:
        try:
            link = content.find_element_by_id('thumbnail').get_attribute('href')
            title = content.find_element_by_id('video-title').text
            div = content.find_element_by_id('metadata-line')
            views = div.find_elements_by_tag_name('span')[0].text
           
            if link not in links and title != '':
                if link != None:
                    links.append(link)
                    print(f'{views} - {title} - {link}')
        except:
            pass
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
browser.quit()