from selenium import webdriver

class Reusable:
    def __init__(self):
        self.driver = None

    def initialize_browser(self, browser_name="chrome"):
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        return self.driver

    def navigate_to_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()



