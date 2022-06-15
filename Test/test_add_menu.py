import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestAddMenu(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_add_menu_use_file(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Gallery(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.VALIDATE_SUCCESS_ADD_MENU)
        L.Api_Delete_Menu(self)

    def test_add_menu_without_photo(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.BTN_SIMPAN_MENU)

    def test_add_menu_use_camera(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.VALIDATE_SUCCESS_ADD_MENU)
        L.Api_Delete_Menu(self)

    def test_add_menu_nama_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Camera(self)
        # L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.BTN_SIMPAN_MENU)

    def test_add_menu_kategori_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        # L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.BTN_SIMPAN_MENU)

    def test_add_menu_deskripsi_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        # L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU)
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.VALIDATE_ADD_MENU_FEED_MODAL)

    def test_add_menu_harga_jual_kurang_50(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_ADD_MENU)
        L.Add_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU)
        L.Add_Menu_Kategori(self)
        L.ScrollToDownText(self, "Simpan")
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU)
        self.driver.find_element(By.XPATH, L.ET_DISCOUNT_MENU).clear()
        L.Ketik(self, L.ET_DISCOUNT_MENU, "30")
        L.Tap(self, L.BTN_SIMPAN_MENU)
        L.Validasi_Display(self, L.VALIDATE_DISC_KURANG_50)

