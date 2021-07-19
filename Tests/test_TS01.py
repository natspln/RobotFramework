import pytest
from PageObjects.OptimyApp import OptimyApp
from Utilities.BaseClass import BaseClass
from time import sleep


@pytest.mark.TS01
class OptimyAppTests(BaseClass):

    def test_OptimyApp(self):

        optimyPage = OptimyApp(self.driver)

        self.clickElement(optimyPage.loginBtn)
        sleep(3)