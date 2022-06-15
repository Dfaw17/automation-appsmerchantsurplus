import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestEditMenuActive(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_edit_menu_active_stock_normal(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        time.sleep(0.5)
        L.Tap(self, L.BTN_ATUR_MENU)
        L.Tap(self, L.BTN_UBAH_STOK)
        L.Ketik(self, L.ET_EDIT_STOCK_MENU_ACTIVE, '890')
        L.Tap(self, L.BTN_EDIT_SAVE_MENU_ACTIVE)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)

    def test_edit_menu_active_expired_date_normal(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        time.sleep(0.5)
        L.Tap(self, L.BTN_ATUR_MENU)
        L.Tap(self, L.BTN_KADALUARSA)
        L.ChooseExpiredDate(self)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)

    def test_nonactive_menu_active(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        time.sleep(0.5)
        L.Tap(self, L.BTN_ATUR_MENU)
        L.Tap(self, L.BTN_NONACTIVE_MENU_ACTIVE)
        L.Tap(self, L.BTN_CONFIRM_NONACTIVE)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)
        L.Api_Set_Active_menu(self)

    def test_nonactive_menu_active_toggle(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        time.sleep(0.5)
        L.Tap(self, L.TOGGLE_INACTIVE_MENU)
        L.Tap(self, L.BTN_CONFIRM_NONACTIVE)
        L.Validasi_Display(self, L.VALIDATE_SET_ACTIVE_MENU)
        L.Api_Set_Active_menu(self)