import pytest
from PageObjects.OptimyApp import OptimyApp
from Utilities.BaseClass import BaseClass
from time import sleep


@pytest.mark.TS04
class OptimyAppTests(BaseClass):

    def test_OptimyApp(self):

        optimyPage = OptimyApp(self.driver)

        self.sendKeys(optimyPage.email, "test@gmail.com")
        self.sendKeys(optimyPage.password, "test")
        self.clickElement(optimyPage.loginBtn)
        self.sendKeys(optimyPage.email, "test@gmail.com")
        self.sendKeys(optimyPage.password, "test")
        self.clickElement(optimyPage.loginBtn)
        self.sendKeys(optimyPage.email, "test@gmail.com")
        self.sendKeys(optimyPage.password, "test")
        self.clickElement(optimyPage.loginBtn)
        sleep(3)