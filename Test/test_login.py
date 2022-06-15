import time
import unittest
from appium import webdriver
from PageObjectModel.Locators import Locator as L


class TestLogin(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_login_normal(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL)
        L.Ketik(self, L.ET_PWD, L.PWD)
        L.Tap(self, L.BTN_MASUK)
        L.Tap(self, L.BTN_SELANJUTNYA)
        time.sleep(1)
        L.Tap(self, L.BTN_SELANJUTNYA)
        time.sleep(1)
        L.Tap(self, L.BTN_SELANJUTNYA)
        time.sleep(1)
        L.Tap(self, L.BTN_SELANJUTNYA)
        time.sleep(1)
        L.Tap(self, L.BTN_TUTUP)
        time.sleep(1)
        L.Validasi_Display(self, L.VALIDATE_LOGIN)

    def test_login_email_belum_diregister(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL_NOT_REGIST)
        L.Ketik(self, L.ET_PWD, L.PWD)
        L.Tap(self, L.BTN_MASUK)
        L.Validasi_Display(self, L.VALIDATE_FEEDBACK_MESSAGE)

    def test_login_password_salah(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL)
        L.Ketik(self, L.ET_PWD, L.PWD_WRONG)
        L.Tap(self, L.BTN_MASUK)
        L.Validasi_Display(self, L.VALIDATE_FEEDBACK_MESSAGE)

    def test_login_password_kosong(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL)
        L.Tap(self, L.BTN_MASUK)
        L.Validasi_Display(self, L.VALIDATE_ERROR_MESSAGE)

    def test_login_email_tanpa_at(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL_WITHOUT_AT)
        L.Ketik(self, L.ET_PWD, L.PWD)
        L.Tap(self, L.BTN_MASUK)
        L.Validasi_Display(self, L.VALIDATE_WRONG_FORMAT)

    def test_login_password_kurang_dari_6_char(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Ketik(self, L.ET_EMAIL, L.EMAIL_WITHOUT_AT)
        L.Ketik(self, L.ET_PWD, 123)
        L.Tap(self, L.BTN_MASUK)
        L.Validasi_Display(self, L.VALIDATE_KURANG_PWD)
