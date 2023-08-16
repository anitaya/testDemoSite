from selenium.webdriver.common.by import By


class SignOnPageLocators:
    USER_NAME_TXT_BOX = (By.NAME, "userName")
    PASSWORD_BOX = (By.NAME, "password")
    SUBMIT_BUTTON = (By.NAME, "submit")
