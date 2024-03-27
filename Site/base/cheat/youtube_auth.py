import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randrange


class Bot:
    def __init__(self, login, password):
        self.driver = uc.Chrome(headless=False, use_subprocess=True)
        self.login = login
        self.password = password

    def auth(self):
        self.driver.get('https://www.youtube.com/')
        sleep(randrange(1, 3))
        login_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, value='Войти')
        login_button.click()
        sleep(randrange(1, 3))
        identifier = self.driver.find_element(By.NAME, 'identifier')
        identifier.clear()
        identifier.send_keys(self.login)
        sleep(randrange(1, 3))
        identifier.send_keys(Keys.ENTER)
        sleep(randrange(1, 3))
        password_form = self.driver.find_element(By.NAME, 'Passwd')
        password_form.send_keys(self.password)
        sleep(randrange(1, 3))
        password_form.send_keys(Keys.ENTER)
        sleep(randrange(1, 3))

    def go_to_stream(self, url):
            self.driver.get(url)
            sleep(4)

    def send_message(self, message):
        chat = self.driver.find_element(By.CLASS_NAME, "style-scope yt-live-chat-text-input-field-renderer")
        chat.click()
        chat.send_keys(message)
        chat.send_keys(Keys.ENTER)

    def bot_terminate(self):
        self.driver.quit()


login = 'alisasabanova030@gmail.com'
password = 'Ct7gxCy8i'
account_1 = Bot(login, password)
try:
    account_1.auth()
    account_1.go_to_stream('https://www.youtube.com/live_chat?is_popout=1&v=9ZjNK0kjdnc')
    account_1.send_message(message='случайно отправил два раза сообщение')
    account_1.bot_terminate()
finally:
    account_1.bot_terminate()