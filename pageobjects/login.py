class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
