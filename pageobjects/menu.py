import time

from pageobjects.base import PageObject


class MainMenu(PageObject):
    def __menu_button(self): return self.driver.find_element_by_css_selector('#menuButton')

    def __logout_button(self): return self.driver.find_element_by_css_selector(
            '#contentWrapper > paper-material > paper-menu > div > a:nth-child(3)')

    def __quit_button(self): return self.driver.find_element_by_css_selector(
            '#contentWrapper > paper-material > paper-menu > div > a:nth-child(4)')

    def __open_menu(self):
        self.__menu_button().click()
        time.sleep(1)  # slide-in animation time

    def logout(self):
        """Only available if user is already logged in."""
        self.__open_menu()
        self.__logout_button().click()

    def quit(self):
        self.__open_menu()
        self.__quit_button().click()
