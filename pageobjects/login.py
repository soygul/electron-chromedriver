from pageobjects.base import PageObject


class LoginPage(PageObject):
    def __to(self): return self.driver.find_element_by_css_selector("#send-presentation-overlay .to-textarea")


def send_message(self, to_address):
    self.to().send_keys(to_address)
