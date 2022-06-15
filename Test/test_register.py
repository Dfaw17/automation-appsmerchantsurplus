import unittest
from appium import webdriver
from PageObjectModel.Locators import Locator as L


class TestRegister(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_register_normal(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Tap(self, L.LINK_REGISTER)
        L.ScrollToDownText(self, "Daftar Sekarang")
        L.Tap(self, L.BTN_REGISTER)
        L.Validasi_Display(self, L.VALIDATE_REGISTER)
