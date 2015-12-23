class PageObject(object):
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
