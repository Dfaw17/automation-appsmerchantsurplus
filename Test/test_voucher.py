import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestVoucher(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_home_voucher(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Validasi_Display(self, L.VALIDATE_PAGE_PROFILE)