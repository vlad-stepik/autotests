from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    # Т.к. изначально создали: self.browser = browser и self.url = url,
    # то в своей функции обращаемся также к self.browser и self.url
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

