import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestMenu(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_menu_buka_halaman_menu(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_PAGE_MENU)

    def test_menu_list_nama_menu(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Validasi_Display(self, L.VALIDATE_LIST_NAMA_MENU)

    def test_menu_list_harga_menu(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Validasi_Display(self, L.VALIDATE_LIST_HARGA_MENU)

    def test_menu_search_available(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        menu = self.driver.find_element(By.XPATH, L.VALIDATE_LIST_NAMA_MENU).text
        L.Ketik(self, L.ET_SEARCH_MENU, menu)
        L.Validasi_Text(self, L.VALIDATE_LIST_NAMA_MENU, menu)

    def test_menu_search_inavailable(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        time.sleep(0.5)
        L.Ketik(self, L.ET_SEARCH_MENU, "Selesai")
        L.Validasi_Display(self, L.VALIDATE_SEARCH_INAVAILABLE)
