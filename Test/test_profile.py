import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.Locators import Locator as L


class TestProfile(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_profile(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Validasi_Display(self, L.VALIDATE_PAGE_PROFILE)

    def test_nama_merchant(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Validasi_Display(self, L.VALIDATE_NAME_MERCHANT)
        L.Validasi_Text(self, L.VALIDATE_NAME_MERCHANT, "Merchant Test Faw")

    def test_area_merchant(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Validasi_Display(self, L.VALIDATE_AREA_MERCHANT)
        L.Validasi_Text(self, L.VALIDATE_AREA_MERCHANT, "Cikarang Selatan")

    def test_profile_toko_saya_nama_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PROFILE_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_NAMA_TOKO)
        L.Validasi_Text(self, L.VALIDATE_TS_NAMA_TOKO, "Merchant Test Faw")

    def test_profile_toko_saya_email_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PROFILE_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_EMAIL_TOKO)
        L.Validasi_Text(self, L.VALIDATE_TS_EMAIL_TOKO, "mt@gmail.com")

    def test_profile_toko_saya_phone_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PROFILE_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_PHONE_TOKO)
        L.Validasi_Text(self, L.VALIDATE_TS_PHONE_TOKO, "081386356616")

    def test_profile_toko_saya_alamat_lengkap_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PROFILE_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_DETAIL_ADDRESS_TOKO)
        # L.Validasi_Text(self, L.VALIDATE_TS_PHONE_TOKO, "081386356616")

    def test_profile_toko_saya_nama_outlet_toko(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PROFILE_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_OUTLET_NAME_TOKO)
        L.Validasi_Text(self, L.VALIDATE_TS_OUTLET_NAME_TOKO, "Mie Setan (Cikarang Selatan)")

    def test_profile_pic_toko_nama_pic(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PIC_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_NAME_PIC)
        L.Validasi_Text(self, L.VALIDATE_TS_NAME_PIC, "Fawwaz")

    def test_profile_pic_toko_posisi_pic(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PIC_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_POSISI_PIC)
        L.Validasi_Text(self, L.VALIDATE_TS_POSISI_PIC, "Kepala Cabang")

    def test_profile_pic_toko_phone_pic(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PIC_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_PHONE_PIC)
        L.Validasi_Text(self, L.VALIDATE_TS_PHONE_PIC, "081386356616")

    def test_profile_pic_toko_nik_pic(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_PIC_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_NIK_PIC)
        L.Validasi_Text(self, L.VALIDATE_TS_NIK_PIC, "3216211709010002")

    def test_profile_rekening_toko_nama_bank(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_REKENING_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_BANK_NAME)
        L.Validasi_Text(self, L.VALIDATE_TS_BANK_NAME, "MANDIRI")

    def test_profile_rekening_toko_no_rekening_bank(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_REKENING_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_NO_REKENING)
        L.Validasi_Text(self, L.VALIDATE_TS_NO_REKENING, "123321")

    def test_profile_rekening_toko_nama_rekening_bank(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_TOKO_SAYA)
        L.Tap(self, L.BTN_TS_REKENING_TOKO)
        L.Validasi_Display(self, L.VALIDATE_TS_NAMA_PEMILIK_REKENING)
        L.Validasi_Text(self, L.VALIDATE_TS_NAMA_PEMILIK_REKENING, "DAFFA FAWWAZ MAULANA")

    def test_profile_kebijakan_dan_provasi(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_BANTUAN)
        L.Tap(self, L.BTN_HELP_KEBIJAKAN_PRIVASI)
        L.Validasi_Display(self, L.VALIDATE_HELP_KEBIJAKAN_PRIVASI)

    def test_profile_syarat_dan_ketentuan(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_BANTUAN)
        L.Tap(self, L.BTN_HELP_SYARAT_KETENTUAN)
        L.Validasi_Display(self, L.VALIDATE_HELP_SYARAT_KETENTUAN)

    def test_profile_FAQ(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_BANTUAN)
        L.Tap(self, L.BTN_HELP_FAQ)
        L.Validasi_Display(self, L.VALIDATE_HELP_FAQ)

    def test_profile_butuh_bantuan(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_BANTUAN)
        L.Tap(self, L.BTN_HELP_BUTUH_BANTUAN)
        L.Ketik(self, L.ET_HELP_BB_NAMA, "Tester Surplus")
        L.Ketik(self, L.ET_HELP_BB_EMAIL, "devops.surplus@gmail.com")
        L.Ketik(self, L.ET_HELP_BB_PHONE, "081386356616")
        L.Ketik(self, L.ET_HELP_BB_MSG, "Test Bantuan")
        L.Tap(self, L.BTN_HELP_BB_SEND)
        L.Validasi_Display(self, L.VALIDATE_PAGE_PROFILE)

    def test_profile_kritik_saran(self):
        L.Step_Login(self)
        L.Tap(self, L.TAB_BOT_PROFILE)
        L.Tap(self, L.BTN_BANTUAN)
        L.Tap(self, L.BTN_HELP_KRITIK_SARAN)
        L.Ketik(self, L.ET_HELP_KS_NAMA, "Tester Surplus")
        L.Ketik(self, L.ET_HELP_KS_EMAIL, "devops.surplus@gmail.com")
        L.Ketik(self, L.ET_HELP_KS_PHONE, "081386356616")
        L.Tap(self, L.CHOOSE_HELP_KS_KAT)
        L.Tap(self, L.CHOOSE_HELP_KS_KAT_KRITIK)
        L.Ketik(self, L.ET_HELP_KS_MSG, "Test Bantuan")
        L.Tap(self, L.BTN_HELP_KS_SEND)
        L.Validasi_Display(self, L.VALIDATE_PAGE_PROFILE)
