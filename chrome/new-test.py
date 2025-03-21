# Generated by Selenium IDE
#pip install selenium pytest
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar WebDriver
driver = webdriver.Chrome()


class TestNewTest():

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_newTest(self):
    self.driver.get("http://development.dgc.agricultura.apps-crc.testing/dgc/login")
    self.driver.find_element(By.ID, "nif").click()
    self.driver.find_element(By.ID, "nif").send_keys("11111111H")
    self.driver.find_element(By.CSS_SELECTOR, ".mn-select-icon-container").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(9)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button__container > .w-100").click()
    self.driver.find_element(By.LINK_TEXT, "Gestió econòmica").click()
    self.driver.find_element(By.LINK_TEXT, "Pagaments").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button__primary > span").click()
  
