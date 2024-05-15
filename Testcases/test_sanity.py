import time

import pytest

from pageobject.BasePage import BasePage
from pageobject.MMTHome import MMTHome

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service as chromeservice


class Test_MMT():

    def test_title(self):
        #Launch Browser
        expectedTitle = "Goibibo - Best Travel Website. Book Hotels, Flights, Trains, Bus and Cabs with upto 50% off"
        title = self.driver.title
        print(title)
        assert title == expectedTitle
        basepage = BasePage(self.driver)
        # basepage.closeFrame()
        basepage.closepopup()
        basepage.Login()
        #Close Browser


    def test_flightBooking(self):
        fromSearch = 'Mum'
        fromCity = 'Mumbai'
        toSearch = 'beng'
        toCity = 'Bengaluru'
        date = 'May 25 2024'
        # Returndate = 'May 13 2024'
        #Launch Browser

        home = MMTHome(self.driver)

        #Closing both the popups
        # home.closeFrame()
        home.closepopup()

        #Enter from city
        home.enterFromCity(fromSearch, fromCity)

        #Enter To city
        home.enterToCity(toSearch, toCity)

        #Enter Date
        home.enterDate(date)

        # #Enter Return Date
        # home.enterReturn( Returndate )

        #Click on Search
        home.clickSearch()

        #Flight search result
        # time.sleep(10)
        # results = self.driver.find_elements(By.XPATH, "//div[@class='listingCard  appendBottom5']")
        # print(len(results))
        #Close Browser