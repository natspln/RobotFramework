import pytest
from PageObjects.OptimyApp import OptimyApp
from Utilities.BaseClass import BaseClass
from time import sleep


@pytest.mark.TS02
class OptimyAppTests(BaseClass):

    def test_OptimyApp(self):

        optimyPage = OptimyApp(self.driver)

        self.sendKeys(optimyPage.email, "testing123@gmail.com")
        self.sendKeys(optimyPage.password, "test")
        self.clickElement(optimyPage.loginBtn)
        sleep(3)