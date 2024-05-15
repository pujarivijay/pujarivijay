from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    def Login(self):
        self.driver.find_element(By.XPATH, "//div[@class='sc-1f95z5i-67 bEjmph']").click()

    # def closeFrame(self):
    #     try:
    #         frame = self.driver.find_element(By.XPATH, "(//span[@class='sc-gsFSXq bGTcbn'])[1]")
    #         self.wait.until(EC.frame_to_be_availab4le_and_switch_to_it((frame)))
    #         #self.driver.switch_to.frame(frame)
    #         self.driver.find_element(By.CLASS_NAME, "close").click()
    #         self.driver.switch_to.default_content()
    #     except:
    #         print("Frame is not displayed")

    def closepopup(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@role='presentation']")))
        self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()