import time
import unittest
from appium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestCentralToCabang(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_central_tambah_cabang(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TAMBAH_CABANG)
        L.ScrollToDownText(self, "Daftar Sekarang")
        L.Tap(self, L.BTN_TAMBAH_CABANG_DAFTAR_SEKARANG)
        L.Validasi_Display(self, L.VALIDATE_TAMBAH_CABANG)

    def test_central_list_cabang(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Validasi_Display(self, L.LIST_CABANG)

    def test_central_search_cabang_inavailable(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Ketik(self, L.ET_CARI_CABANG, "Fawz")
        assert_that(L.LIST_CABANG).does_not_exist()

    def test_central_search_cabang_available(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Ketik(self, L.ET_CARI_CABANG, "Faw")
        L.Validasi_Display(self, L.LIST_CABANG)

    def test_central_choose_cabang(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        time.sleep(0.5)
        L.Validasi_Display(self, L.VALIDATE_PAGE_MODE_CABANG)

    def test_central_cabang_toko_saya(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_TOKO_SAYA)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_TOKO_SAYA)

    def test_central_cabang_pic_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_PIC_TOKO)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_PIC)

    def test_central_cabang_menu_aktif(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_AKTIF)

    def test_central_cabang_menu_aktif_nama(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_AKTIF_NAMA)

    def test_central_cabang_menu_aktif_harga(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_AKTIF_HARGA_STOCK)

    def test_central_cabang_menu_aktif_stock(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_AKTIF_HARGA_STOCK)

    def test_central_cabang_menu_aktif_waktu(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_AKTIF_WAKTU)

    def test_central_cabang_all_menu(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Tap(self, L.BTN_CABANG_MODE_TOP_TAB_ALL_MENU)
        L.Validasi_Display(self, L.VALIDATE_PAGE_MODE_CABANG_ALL_MENU)

    def test_central_cabang_all_menu_nama(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Tap(self, L.BTN_CABANG_MODE_TOP_TAB_ALL_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_ALL_NAMA)

    def test_central_cabang_all_menu_harga(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_CABANG_SAYA)
        L.Tap(self, L.LIST_CABANG)
        L.Tap(self, L.BTN_PILIH_CABANG)
        L.Tap(self, L.BTN_MASUK_CABANG)
        L.Tap(self, L.BTN_CABANG_MODE_BOT_TAB_MENU)
        L.Tap(self, L.BTN_CABANG_MODE_TOP_TAB_ALL_MENU)
        L.Validasi_Display(self, L.VALIDATE_MODE_CABANG_MENU_ALL_HARGA)