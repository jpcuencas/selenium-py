from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPagaments():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pagaments(self):
    # Test name: pagaments
    # Step # | name | target | value
    # 1 | open | /dgc/login | 
    self.driver.get("http://development.dgc.agricultura.apps-crc.testing/dgc/login")
    # 2 | setWindowSize | 970x670 | 
    self.driver.set_window_size(970, 670)
    # 3 | click | id=nif | 
    self.driver.find_element(By.ID, "nif").click()
    # 4 | type | id=nif | 11111111H
    self.driver.find_element(By.ID, "nif").send_keys("11111111H")
    # 5 | click | css=.mn-select-icon-container | 
    self.driver.find_element(By.CSS_SELECTOR, ".mn-select-icon-container").click()
    # 6 | click | css=.ng-star-inserted:nth-child(9) | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(9)").click()
    # 7 | click | css=.button__container > .w-100 | 
    self.driver.find_element(By.CSS_SELECTOR, ".button__container > .w-100").click()
    # 8 | mouseOver | css=.button__container > .w-100 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".button__container > .w-100")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | click | linkText=Gestió econòmica | 
    self.driver.find_element(By.LINK_TEXT, "Gestió econòmica").click()
    # 10 | click | linkText=Pagaments | 
    self.driver.find_element(By.LINK_TEXT, "Pagaments").click()
    # 11 | click | css=.button__primary > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".button__primary > span").click()
  
