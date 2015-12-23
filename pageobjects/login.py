from pageobjects.base import PageObject


class LoginPage(PageObject):
    def __username(self): return self.driver.find_element_by_id('username')

    def __password(self): return self.driver.find_element_by_id('password')

    def __connect_button(self): return self.driver.find_element_by_css_selector('#signInButton')

    def login(self, username, password):
        self.__username().send_keys(username)
        self.__password().send_keys(password)
        self.__connect_button().click()
