class PageObject(object):
    """Base class for all page object"""

    def __init__(self, driver):
        self.driver = driver
