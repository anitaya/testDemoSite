from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_SUCCESS_LBL = (By.TAG_NAME, "h3")
    SIGN_OFF = (By.XPATH, "//a[text()='SIGN-OFF']")
