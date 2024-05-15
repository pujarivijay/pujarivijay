import time

from pageobject.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MMTHome(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    def enterFromCity(self, fromSearch, fromCity):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='From']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(fromSearch)
        self.wait.until(EC.presence_of_element_located((By.XPATH,"(//span[contains(@class,'autoCompleteTitle')])[1]"))).click()
        # self.driver.find_element(By.XPATH,"(//span[contains(@class,'autoCompleteTitle')])[1]").click()
        time.sleep(10)
        cities = self.driver.find_elements(By.XPATH,"(//span[contains(@class,'autoCompleteTitle')])")
        for city in cities:
            if city.text == fromCity:
                city.click()
    def enterToCity(self, toSearch, toCity):
        # self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='To']"))).click()
        # self.driver.find_element(By.XPATH, "//span[normalize-space()='To']").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(toSearch)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[contains(@class,'autoCompleteTitle')])[1]"))).click()
        # self.driver.find_element(By.XPATH,"//p[normalize-space()='" + toCity + "']").click()
        time.sleep(10)
        tocities = self.driver.find_elements(By.XPATH, "(//span[contains(@class,'autoCompleteTitle')])")
        for city in tocities:
            if city.text == toCity:
                city.click()
    def enterDate(self, date):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Departure']").click()
        self.driver.find_element(By.XPATH, "//div[contains(@aria-label,'"+date+"')]").click()

    # def  enterReturn(self,  Returndate):
    #     self.driver.find_element(By.XPATH, "//span[normalize-space()='Return']']").click()
    #     self.driver.find_element(By.XPATH, " // div[ @ aria - label ,'" +  Returndate + "')]").click()


    def clickSearch(self):
        self.driver.find_element(By.XPATH, "//span[@class='sc-12foipm-72 ezNmSh']").click()

