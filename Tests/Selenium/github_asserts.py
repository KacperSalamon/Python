from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class GithubTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/")

    def test_github(self):
        driver = self.driver
        assert "GitHub" in driver.title

        search_box = driver.find_element_by_name("q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
