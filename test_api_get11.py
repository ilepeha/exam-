from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class GeoLocationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_geolocation(self):
        self.driver.get("http://the-internet.herokuapp.com/geolocation")
        geolocation_button = self.driver.find_element(By.CSS_SELECTOR, '.example button')
        geolocation_button.click()
        self.driver.implicitly_wait(5)  
        latitude = self.driver.find_element(By.ID, 'lat-value').text
        longitude = self.driver.find_element(By.ID, 'long-value').text
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        self.assertTrue(latitude and longitude, "Latitude and Longitude should be displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
