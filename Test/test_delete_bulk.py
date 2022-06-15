import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestDeleteMenuActive(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_delete_bulk_menu_normal(self):
        L.Api_Delete_Bulk(self)
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.ScrollToDownText(self, "Test Menu Bulk 1")
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_1_DELETE)
        L.Tap(self, L.CARD_2_DELETE)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS_CONFIRM)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_NONACTIVE)

    def test_delete_bulk_1_menu(self):
        L.Api_Delete_Bulk_1(self)
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.ScrollToDownText(self, "Test Menu Bulk 1")
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_2_DELETE)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS_CONFIRM)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_CABANG_MENU_NONACTIVE)

    def test_delete_bulk_menu_confirm_cancel(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Tap(self, L.BTN_PILIH_SEKALIGUS)
        L.Tap(self, L.CARD_DELETE_CANCEL)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS)
        L.Tap(self, L.BTN_HAPUS_SEKALIGUS_CANCEL)
        time.sleep(0.5)
        L.Validasi_Display(self, L.BTN_HAPUS_SEKALIGUS)