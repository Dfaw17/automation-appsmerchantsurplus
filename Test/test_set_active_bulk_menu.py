import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestSetActiveBulk(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_set_active_normal(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_1_Active)
        L.Tap(self, L.CARD_2_Active)
        L.Tap(self, L.BTN_AKTIFKAN_SEKALIGUS)
        time.sleep(0.5)
        L.Ketik(self, L.ET_STOCK_BULK_1, "99")
        L.Ketik(self, L.ET_STOCK_BULK_2, "99")
        L.ScrollModal(self, 2, 2, 8/9, 9)
        L.ChooseActiveUntillBulk(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_BULK)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_ACTIVE)
        L.Api_Inactive_Bulk(self)

    def test_set_active_normal_1(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_1_Active)
        L.Tap(self, L.BTN_AKTIFKAN_SEKALIGUS)
        time.sleep(0.5)
        L.Ketik(self, L.ET_STOCK_BULK_1, "99")
        L.ScrollModal(self, 2, 2, 8/9, 9)
        L.ChooseActiveUntillBulk(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_BULK)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_ACTIVE)
        L.Api_Inactive_Bulk_1(self)

    def test_set_active_normal_lebih_1(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_1_Active)
        L.Tap(self, L.CARD_2_Active)
        L.Tap(self, L.CARD_3_Active)
        L.Tap(self, L.BTN_AKTIFKAN_SEKALIGUS)
        time.sleep(0.5)
        L.Ketik(self, L.ET_STOCK_BULK_1, "99")
        L.Ketik(self, L.ET_STOCK_BULK_2, "98")
        L.Ketik(self, L.ET_STOCK_BULK_3, "97")
        L.ScrollModal(self, 2, 2, 8/9, 9)
        L.ChooseActiveUntillBulk(self)
        L.Tap(self, L.BTN_SAVE_ACTIVE_BULK)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_ACTIVE)
        L.Api_Inactive_Bulk_lebih_1(self)

    def test_set_active_bulk_menu_expired_null(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_1_Active)
        L.Tap(self, L.BTN_AKTIFKAN_SEKALIGUS)
        time.sleep(0.5)
        L.Ketik(self, L.ET_STOCK_BULK_1, "99")
        L.ScrollModal(self, 2, 2, 8/9, 9)
        L.Tap(self, L.BTN_SAVE_ACTIVE_BULK)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_EXPIRED_DATE_NULL)
