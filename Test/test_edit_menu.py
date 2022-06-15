import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestEditMenu(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_edit_menu_normal(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_EDIT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Tap(self, L.IMG_EDIT_MENU_SETTING)
        L.Tap(self, L.BTN_EDIT_MENU)
        L.Edit_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU_EDIT)
        L.Edit_Menu_Kategori(self)
        L.ScrollModal(self, 2, 2, 8 / 9, 9)
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU_EDIT)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU_EDIT)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        time.sleep(1)
        L.Validasi_Display(self, L.VALIDATE_PAGE_MENU)

    def test_edit_menu_foto_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_EDIT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Tap(self, L.IMG_EDIT_MENU_SETTING)
        L.Tap(self, L.BTN_EDIT_MENU)
        # L.Edit_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU_EDIT)
        L.Edit_Menu_Kategori(self)
        L.ScrollModal(self, 2, 2, 8 / 9, 9)
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU_EDIT)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU_EDIT)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        time.sleep(1)
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").is_displayed()

    def test_edit_menu_nama_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_EDIT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Tap(self, L.IMG_EDIT_MENU_SETTING)
        L.Tap(self, L.BTN_EDIT_MENU)
        L.Edit_Menu_Photo_Camera(self)
        L.Hapus(self, L.ET_ADD_NAMA_MENU)
        L.Edit_Menu_Kategori(self)
        time.sleep(0.5)
        L.ScrollModal(self, 2, 2, 8 / 9, 9)
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU_EDIT)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU_EDIT)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        L.Validasi_Display(self, L.VALIDATE_ADD_MENU_FEED_MODAL)

    def test_edit_menu_desc_kosong(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_EDIT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Tap(self, L.IMG_EDIT_MENU_SETTING)
        L.Tap(self, L.BTN_EDIT_MENU)
        L.Edit_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU_EDIT)
        L.Edit_Menu_Kategori(self)
        L.ScrollModal(self, 2, 2, 8 / 9, 9)
        L.Hapus(self, L.ET_DESKRIPSI)
        L.Ketik(self, L.ET_HARGA_ASLI, L.HARGA_ASLI_MENU_EDIT)
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        L.Validasi_Display(self, L.VALIDATE_ADD_MENU_FEED_MODAL)

    def test_edit_menu_disc_kurang_50(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_EDIT_MENU)
        L.Tap(self, L.BTN_SELANJUTNYA)
        L.Tap(self, L.BTN_SELESAI)
        L.Tap(self, L.TAB_TOP_MENU_NONAKTIF)
        L.Tap(self, L.IMG_EDIT_MENU_SETTING)
        L.Tap(self, L.BTN_EDIT_MENU)
        L.Edit_Menu_Photo_Camera(self)
        L.Ketik(self, L.ET_ADD_NAMA_MENU, L.NAMA_MENU_EDIT)
        L.Edit_Menu_Kategori(self)
        L.ScrollModal(self, 2, 2, 8 / 9, 9)
        L.Ketik(self, L.ET_DESKRIPSI, L.DESC_MENU_EDIT)
        L.Hapus(self, L.ET_DISCOUNT_MENU_EDIT)
        L.Ketik(self, L.ET_DISCOUNT_MENU_EDIT, "20")
        L.Tap(self, L.BTN_SAVE_EDIT_MENU)
        L.Validasi_Display(self, L.VALIDATE_DISC_KURANG_50)
