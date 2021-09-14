""" TestCases for checking increase and decrease functionality """
import os
import pathlib
from selenium import webdriver
import unittest

"""Here browser Safari is used for testing"""
driver = webdriver.Safari()

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpagesTests(unittest.TestCase):

    def test_title(self):
        """Title is Counter"""
        driver.get(file_uri('counter.html'))
        self.assertEqual(driver.title, 'Counter')

    def test_increase(self):
        """Make sure header is updated to 1 on click of increase button"""
        driver.get(file_uri('counter.html'))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        """Make sure header is updated to -1 on click of decrease button"""
        driver.get(file_uri('counter.html'))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_multipleincrease(self):
        """Make sure header is updated to 3 after 3 clicks of increase button"""
        driver.get(file_uri('counter.html'))
        increase = driver.find_element_by_id('increase')
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "3")

if __name__ == "__main__":
    unittest.main()


