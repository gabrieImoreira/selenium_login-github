from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = Service('./chromedriver')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
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
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print(f'Erro ao clicar no Sign in{e}')

    def sign_in(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')

            input_login.send_keys('@USER_GITHUB')
            input_password.send_keys('@PASSWORD_GITHUB')
            sleep(2)
            btn_login.click()

        except Exception as e:
            print(f'Erro ao fazer login: {e}')

    def click_menu(self):
        try:
            btn_click_menu = self.chrome.find_element(By.XPATH, '/html/body/div[1]/header/div[7]/details/summary')
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
    chrome = ChromeAuto()
    chrome.access('https://github.com')
    sleep(1)
    chrome.click_menu()
    chrome.click_sign_out()

    chrome.click_sign_in()
    chrome.sign_in()
    sleep(2)

    chrome.click_menu()
    chrome.profile_verification('@USER_TO_BE_VERIFIED')
    sleep(2)
    chrome.exit()
