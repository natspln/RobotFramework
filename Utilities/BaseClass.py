import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def clickElement(self, locator):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.click()
        except Exception as ex:
            print(ex)

    def sendKeys(self, locator, value):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.clear()
            element.send_keys(value, Keys.ENTER)
        except Exception as ex:
            print(ex)

    def stringVerifier(self, locator, errorMessage):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            error = element.text
            if error == errorMessage:
                return True
        except Exception as ex:
            return False