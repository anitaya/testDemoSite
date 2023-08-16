from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class LoginSuccessPage(BasePage):

    def get_login_success_label(self):
        lbl_login_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGIN_SUCCESS_LBL).text
        return lbl_login_success_txt

    def click_sign_off(self):
        sign_off = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.SIGN_OFF).click()
        return sign_off
