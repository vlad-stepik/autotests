

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    # Т.к. изначально создали: self.browser = browser и self.url = url,
    # то в своей функции обращаемся также к self.browser и self.url
    def open(self):
        self.browser.get(self.url)

