from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
    def go_to_login_page(self):
        #login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 
    
    def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


# не забываем оставить пустую строку в конце файла
        
