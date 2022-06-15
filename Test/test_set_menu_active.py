import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestSetMenuActive(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_set_menu_active_normal(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.TOGGLE_ACTIVE_MENU)
        L.Ketik(self, L.STOCK_ACTIVE_MENU, "888")
        L.ChooseExpiredDate(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_MENU)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)
        time.sleep(0.5)
        L.Api_Set_Inactive_Menu(self)

    def test_set_menu_active_besok(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.TOGGLE_ACTIVE_MENU)
        L.Ketik(self, L.STOCK_ACTIVE_MENU, "888")
        L.ChooseExpiredDate(self)
        L.Tap(self, L.CHECKBOX_BESOK)
        L.Tap(self, L.BTN_SAVE_ACTIVE_MENU)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)
        time.sleep(0.5)
        L.Api_Set_Inactive_Menu(self)

    def test_set_menu_active_stock_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.TOGGLE_ACTIVE_MENU)
        # L.Ketik(self, L.STOCK_ACTIVE_MENU, "888")
        L.ChooseExpiredDate(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_MENU)
        L.Validasi_Display(self, L.BTN_SAVE_ACTIVE_MENU)

    def test_set_menu_active_expired_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.TOGGLE_ACTIVE_MENU)
        L.Ketik(self, L.STOCK_ACTIVE_MENU, "888")
        # L.ChooseExpiredDate(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_MENU)
        L.Validasi_Display(self, L.BTN_SAVE_ACTIVE_MENU)
