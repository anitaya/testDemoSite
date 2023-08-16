from pages.base_page import BasePage
from pages.log_out_page_locators import LogOutPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignOn(BasePage):
    def click_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LogOutPageLocators.CLICK_BUTTON).click()
