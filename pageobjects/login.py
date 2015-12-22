from pageobjects.page import PageObject


class LoginPage(PageObject):
    to = lambda self: self.webdriver.find_element_by_css_selector("#send-presentation-overlay .to-textarea")
    subject = lambda self: self.webdriver.find_element_by_xpath("//*[@id='send-presentation-overlay']//input[@name='subject']")
    message_text = lambda self: self.webdriver.find_element_by_css_selector("#send-presentation-overlay .message-textarea")
    send_button = lambda self: self.webdriver.find_element_by_css_selector("#send-presentation-overlay .submit")


def send_message(self, to_address, subject, message):
    self.to().send_keys(to_address)
    self.subject().send_keys(subject)

    # switch message input to text input to make it easier to set the message.
    self.message_text().send_keys(message)
