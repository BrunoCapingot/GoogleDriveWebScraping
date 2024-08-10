import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


class Driver(EdgeOptions):
    def __init__(self):
        super().__init__()
        # self.add_argument('--headless')
        # self.add_experimental_option('prefs', {'geolocation': {'latitude': 37.4219999, 'longitude': -122.0840575}})
        # self.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
        self.add_argument('--disable-notifications')
        self.add_argument('--disable-cache')
        self.add_argument('--incognito')
        self.add_argument('--disable-javascript')
        self.add_argument('--ignore-certificate-errors')
        self.driver = None

    def getListLink(self)->list:
        urls = []
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            urls.append(self.driver.current_url)
        return urls

    def clickFromCssSelector(self, comand:str)->None:
        self.driver.find_element(By.CSS_SELECTOR, value=str(comand)).click()

    def clickFromXpath(self, comand:str)->None:
        self.driver.find_element(By.XPATH, value=str(comand)).click()

    def close(self)->None:
        self.driver.close()

    def open(self, link:str)->None:
        self.driver = webdriver.Edge(
            service=EdgeService(executable_path=r'C:\Users\CPGT\Desktop\WebScrapingGeral\msedgedriver.exe'),
            options=self)
        self.driver.get(link)

    def quit(self)->None:
        self.driver.quit()
