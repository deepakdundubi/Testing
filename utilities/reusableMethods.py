import os
import time
from os import times
from tkinter.tix import Select

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage


class page_URL_Verification:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def verify_url(self, expected_text, screenshot_path_pass, screenshot_path_fail):
          actual_url = self.driver.current_url
          if expected_text in actual_url:
              self.driver.save_screenshot(screenshot_path_pass)
              assert True
              self.logger.info("URL VERIFICATION PASS")
          else:
              self.driver.save_screenshot(screenshot_path_fail)
              self.driver.close()
              self.logger.info("URL VERIFICATION FAILED")
              assert False

    def save_screenshot(self, file_path):
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        self.driver.save_screenshot(file_path)

class GenericUtils:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    @staticmethod
    def select_value_from_custom_dropdown(click_dropdown_fn,search_value_fn,click_result_fn,value_to_select,
            logger=None,
            driver=None,
            screenshot_path=None
    ):
        click_dropdown_fn()
        search_value_fn(value_to_select)
        time.sleep(2)
        if logger:
            logger.info(f"Searching and selecting: {value_to_select}")
        if driver and screenshot_path:
            driver.save_screenshot(screenshot_path)
        time.sleep(2)
        click_result_fn()
        time.sleep(2)

class StaticDropdown:
    def __init__(self, driver):
        self.driver = driver

    def select_by_visible_text(self, locator, text):
        dropdown = self.driver.find_element(*locator)
        Select(dropdown).select_by_visible_text(text)






