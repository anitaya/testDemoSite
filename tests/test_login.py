from test_utils import *

from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.sign_on_page import SignOnPage
from pages.login_success_page import LoginSuccessPage
from pages.log_out_page import SignOn
from resources.constants import TEST_SITE_URL


class TestLogin:

    # Test Case 1 ( Registering the user)
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"
        sign_in = RegisterSuccessPage(driver)
        sign_in.click_sign_in()

    def test_sign_in(self, driver, username_password):
        sign_on_page = SignOnPage(driver)
        sign_on_page.wait_and_type_user_name(username_password)
        sign_on_page.type_password(username_password)
        sign_on_page.click_submit_btn()
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert login_success_lbl == "Login Successfully", "User login failed!"
        sign_off = LoginSuccessPage(driver)
        sign_off.click_sign_off()

    def test_log_out(self, driver):
        log_out_page = SignOn(driver)
        log_out_page.click_btn()
        assert sign_on_link is not None, "Log out failed!"

