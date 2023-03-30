import kv_secrets
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = Service('chromedriver')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.options.add_argument("--disable-logging")
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-web-security")
        self.options.add_argument("--start-maximized")
        self.chrome = webdriver.Chrome(
            service = self.driver_path,
            options=self.options
        )

    def access(self, site):
        self.chrome.get(site)

    def exit(self):
        self.chrome.quit()

    def click_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]")
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro ao clicar no Sign in{e}')

    def sign_in(self, username, password):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')
            input_login.send_keys(username)
            input_password.send_keys(senha)
            sleep(2)
            btn_login.click()

        except Exception as e:
            print(f'Erro ao fazer login: {e}')

    def click_menu(self):
        try:
            btn_click_menu = self.chrome.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[7]/details/summary/span[2]')
            btn_click_menu.click()
            sleep(2)
        except Exception as e:
            print(f'Erro ao clicar clicar no menu: {e}')

    def click_sign_out(self):
        try:
            btn_click_sign_out = self.chrome.find_element(By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')
            btn_click_sign_out.click()
            sleep(2)
        except Exception as e:
            print(f'Erro ao clicar clicar no Sign out: {e}')

    def profile_verification(self, user):
        profile_link = self.chrome.find_element(By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a')
        profile_link_hmtl = profile_link.get_attribute('innerHTML')
        assert user in profile_link_hmtl

if __name__ == '__main__':
    print('inicio')
    chrome = ChromeAuto()
    chrome.access('https://github.com')
    sleep(1)

    result = kv_secrets.retrieve_credentials()
    if result[0]:
        username, senha = result[1], result[2]
        chrome.click_sign_in()
        sleep(1.5)
        print('fazer login')
        chrome.sign_in(username, senha)
        sleep(5)

        chrome.click_menu()
        sleep(2)
        # chrome.profile_verification('gabrieimoreira')
        sleep(2)
        chrome.exit()
        print('fim')
