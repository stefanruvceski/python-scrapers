from selenium import webdriver
import time
from os import system
from selenium.webdriver.common.keys import Keys

SCROLL_PAUSE_TIME = 0.5
cls = lambda: system('cls')
instagram_url = 'https://www.instagram.com/'
profile_url = 'https://www.instagram.com/ftn.privatni.casovi/'

driver = webdriver.Chrome()


def instagram_login():
    driver.get(instagram_url)
    time.sleep(2)

    username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

    username.send_keys("ftn.privatni.casovi")
    password.send_keys("Terminator_96")

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    time.sleep(5)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    
def get_profile_page():
    driver.get(profile_url)

    time.sleep(2)
   
    
def get_followers(num_followers):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(2)
    
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    fList = []
    while len(fList) < num_followers: 
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(2)
        scroll += 1

        fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(fList)))

    print("ended")


    followers = []
    for user in fList:
        followers.append(user.find_element_by_tag_name('a').text.strip())
        
    return followers

def get_following(num_following):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(2)
    
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    fList = []
    while len(fList) < num_following: 
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(2)
        scroll += 1

        fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(fList)))

    print("ended")


    following = []
    for user in fList:
        following.append(user.find_element_by_tag_name('a').text.strip())
        
    return following

def get_numbers():
    numbers = driver.find_elements_by_class_name('g47SY')
    num_followers = int(numbers[1].get_attribute('innerHTML').strip())
    num_following = int(numbers[2].get_attribute('innerHTML').strip())
    return num_followers,num_following

def main():
    instagram_login()
    get_profile_page()
    num_followers,num_following = get_numbers()
    followers = get_followers(num_followers)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
    time.sleep(0.5)
    following = get_following(num_following)
    cls()
    print('Users to unfollow')

    for f in following:
        if f not in followers:
            print(f)
    print('-'*15)
    driver.quit()
    
if __name__ == '__main__':
    main()