from pages.base_page import BasePage
from pages.sign_on_page_locators import SignOnPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class SignOnPage(BasePage):

    def wait_and_type_user_name(self, userNameAndPwList):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SignOnPageLocators.USER_NAME_TXT_BOX).send_keys(
            userNameAndPwList[0])

    def type_password(self, userNameAndPwList):
        self.find_element(SignOnPageLocators.PASSWORD_BOX).send_keys(
            userNameAndPwList[1])

    def click_submit_btn(self):
        self.find_element(SignOnPageLocators.SUBMIT_BUTTON).click()
