from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36', 'accept': '*/*'}
mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


print("Введите ссылку на профиль")
product = str(input())
login = 'onelifeitsme'
password = 'OneLife2019'

driver = webdriver.Chrome(options=chrome_options)

driver.get(product)

sleep(1)


def sign_ing(login, password):
    login = 'onelifeitsme'
    pasword = 'OneLife2019'
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]').click()
    login_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input')
    login_field.send_keys(login)
    password_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input')
    password_field.send_keys(pasword)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button/div').click()
    sleep(4)

# АВТОРИЗАЦИЯ
driver.get('https://www.instagram.com/')
sign_ing(login, password)
driver.get(product)
driver.find_element_by_xpath('//li[3]/a').click()
sleep(3)


actions = ActionChains(driver)
actions.send_keys(Keys.TAB * 6)
actions.perform()
sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.END)
actions.perform()
sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB * 6)
actions.perform()
sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.END)
for i in range(50):
    actions.perform()
    sleep(1)




sleep(3)

accounts = []
users = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div[2]/ul/div/li/div/div[1]/div[2]/div[1]/a')
if users:
    print("данные получены")
    print(len(users))
else:
    print('данные не получены')
for i in users:
    accounts.append('https://www.instagram.com/' + i.text)

for i in accounts:
    print(i)
print(len(accounts))









