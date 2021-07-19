from selenium.webdriver.common.by import By


class OptimyApp:

    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//*[@id='tab-login']/form/div[1]/input")
    password = (By.XPATH, "//*[@id='tab-login']/form/div[2]/input")
    loginBtn = (By.XPATH, "//*[@id='tab-login']/form/button")
    loginError = (By.XPATH, "//*[@id='login-invalid']")