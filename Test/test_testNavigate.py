# Generated by Selenium IDE
import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Testing(unittest.TestCase):
  def test_testNavigate(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://sia0.github.io/Apni-Dukaan/mobile.html")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.find_element(By.LINK_TEXT, "FAQ").click()
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 5")
    self.driver.quit()
  
if __name__ == "__main__":
  unittest.main()
