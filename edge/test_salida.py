# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

class TestSalida():
  
  def teardown_method(driver):
    driver.quit()
  
  def test_salida(driver):
    driver.get("https://checkio.connectis.es/checkio/gestion/fichar")
    driver.set_window_size(968, 528)
    driver.find_element(By.CSS_SELECTOR, ".cdk-focused > .mat-button-wrapper > div > div").click()
  
TestSalida.test_salida(driver)

TestSalida.teardown_method(driver)