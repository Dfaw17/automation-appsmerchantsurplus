import time
import unittest
from appium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestCabang(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_cabang_login(self):
        L.Step_Login_Cabang(self)
        L.Validasi_Display(self, L.VALIDATE_CABANG)
        L.Validasi_Text(self, L.VALIDATE_CABANG, "Merchant Test Faw 2")

    def test_cabang_get_list_order(self):
        L.Step_Login_Cabang(self)
        L.Validasi_Display(self, L.VALIDATE_LIST_ORDER)

    def test_cabang_menu_active(self):
        L.Step_Login_Cabang(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_PAGE_MENU_CABANG)

    def test_cabang_menu_nonactive(self):
        L.Step_Login_Cabang(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_NONACTIVE)

    def test_cabang_atur_stock_active(self):
        L.Step_Login_Cabang(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.BTN_CABANG_ATUR_MENU_ACTIVE)
        L.Tap(self, L.BTN_UBAH_STOK)
        stok = self.driver.find_element(By.XPATH, L.ET_EDIT_STOCK_MENU_ACTIVE).text
        L.Ketik(self, L.ET_EDIT_STOCK_MENU_ACTIVE, int(stok)-1)
        L.Tap(self, L.BTN_EDIT_SAVE_MENU_ACTIVE)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_ACTIVE)

    def test_cabang_atur_time_active(self):
        L.Step_Login_Cabang(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.BTN_CABANG_ATUR_MENU_ACTIVE)
        L.Tap(self, L.BTN_KADALUARSA)
        L.ChooseExpiredDate(self)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_ACTIVE)