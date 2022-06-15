import unittest
from appium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
from PageObjectModel.Locators import Locator as L


class TestHome(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_home_menampilkan_tanggal_hari_ini(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_DATE)

    def test_home_menampilkan_nama_merchant(self):
        L.Step_Login(self)
        L.Validasi_Text(self, L.VALIDATE_NAMA_MERCH, 'Merchant Test Faw')

    def test_home_menampilkan_menu_aktif(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_MENU_ACTIVE_TOTAl)

    def test_home_menampilkan_button_menu_aktif(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_BTN_MENU_ACTIVE)

    def test_home_list_pesanan_jenis_pengambilan(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_ORDER_TYPE)
        assert_that(self.driver.find_element(By.XPATH, L.VALIDATE_ORDER_TYPE).text).is_in("Self Pickup", "Delivery")

    def test_home_list_pesanan_no_order(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_NO_ORDER)
        L.Validasi_Not_Empty(self, L.VALIDATE_NO_ORDER)

    def test_home_list_pesanan_tgl_pemesanan(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_TGL_ORDER)
        L.Validasi_Not_Empty(self, L.VALIDATE_TGL_ORDER)

    def test_home_list_pesanan_nama_customer(self):
        L.Step_Login(self)
        L.Validasi_Display(self, L.VALIDATE_NAMA_CUST)
        L.Validasi_Not_Empty(self, L.VALIDATE_NAMA_CUST)

    def test_home_list_pesanan_detail(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER)
        L.Validasi_Text(self, L.VALIDATE_DETAIL_ORDER, "Rincian Pesanan")

    def test_home_list_pesanan_detail_kode_order(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_KODE_PESANAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_KODE_PESANAN)

    def test_home_list_pesanan_detail_waktu_order(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_WAKTU_PESANAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_WAKTU_PESANAN)

    def test_home_list_pesanan_detail_nama_customer(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_NAMA_PEMESAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_NAMA_PEMESAN)

    def test_home_list_pesanan_detail_metode_pengambilan(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_METODE_PENGAMBILAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_METODE_PENGAMBILAN)

    def test_home_list_pesanan_detail_waktu_pengambilan(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_WAKTU_PENGAMBILAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_WAKTU_PENGAMBILAN)
        assert_that(self.driver.find_element(By.XPATH, L.VALIDATE_DETAIL_ORDER_WAKTU_PENGAMBILAN).text).is_in(
            "Hari ini", "Besok")

    def test_home_list_pesanan_detail_jenis_pembayaran(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_PEMBAYARAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_PEMBAYARAN)

    def test_home_list_pesanan_detail_total_pembayaran(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_TOP_SELESAI)
        L.Tap(self, L.LIST_PESANAN_SELESAI)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_TOTAL_PEMBAYARAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_TOTAL_PEMBAYARAN)

    def test_home_pesanan_self_pickup_nama_pemesan(self):
        L.Step_Login(self)
        L.Tap(self, L.VALIDATE_ORDER_TYPE)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_NAMA_PEMESAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_NAMA_PEMESAN)

    def test_home_pesanan_self_pickup_methode(self):
        L.Step_Login(self)
        L.Tap(self, L.VALIDATE_ORDER_TYPE)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_METODE_PENGAMBILAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_METODE_PENGAMBILAN)

    def test_home_pesanan_self_pickup_methode_payment(self):
        L.Step_Login(self)
        L.Tap(self, L.VALIDATE_ORDER_TYPE)
        L.Validasi_Display(self, L.VALIDATE_DETAIL_ORDER_PEMBAYARAN)
        L.Validasi_Not_Empty(self, L.VALIDATE_DETAIL_ORDER_PEMBAYARAN)

    def test_home_pesanan_self_pickup_ambil_foto(self):
        L.Api_SF_Kotak_Makan(self)
        L.Step_Login(self)
        L.Tap(self, L.VALIDATE_ORDER_TYPE)
        L.Tap(self, L.BTN_PHOTO_KOTAK_MAKAN)
        L.IZINKAN(self)
        L.IZINKAN(self)
        L.Tap(self, L.BTN_OPEN_PHOTO_KOTAK_MAKAN)
        L.IZINKAN(self)
        L.Tap(self, L.BTN_TAKE_PHOTO_KOTAK_MAKAN)
        L.Validasi_Display(self, L.VALIDATE_KOTAK_MAKAN)
        L.Api_Finish_Order(self)

    def test_home_menampilkan_jumlah_pesanan(self):
        L.Step_Login(self)
        jumlah_pesanan = self.driver.find_element(By.XPATH, L.JUMLAH_PESANAN).text
        assert_that(str(jumlah_pesanan[0:1])).is_equal_to(str(L.Api_Index_Pesanan(self)))
