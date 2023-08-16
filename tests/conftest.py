import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def login_feature():
    firstname = "charles"
    lastname = "david"
    user_name = "charles@123"
    password = "charles"

    return [firstname, lastname, user_name, password, ]


@pytest.fixture(scope="function")
def username_password():
    user_name = "dan25"
    password = "dan123"
    return [user_name, password]
