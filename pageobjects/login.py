from pageobjects.base import PageObject


class LoginPage(PageObject):
    def __username(self): return self.driver.find_element_by_css_selector(
            '#cards > div.cards.style-scope.task-cards > task-card > sign-in > div > div > paper-input:nth-child(3) > paper-input-container > div.input-content.style-scope.paper-input-container #labelAndInputContainer #input')

    def __password(self): return self.driver.find_element_by_css_selector(
            '#cards > div.cards.style-scope.task-cards > task-card > sign-in > div > div > paper-input:nth-child(4) > paper-input-container > div.input-content.style-scope.paper-input-container #labelAndInputContainer #input')

    def __connect_button(self): return self.driver.find_element_by_css_selector('#signInButton')

    def login(self, username, password):
        self.__username().send_keys(username)
        self.__password().send_keys(password)
        self.__connect_button().click()
