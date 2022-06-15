import unittest
from appium import webdriver
from PageObjectModel.Locators import Locator as L


class TestResetPassword(unittest.TestCase):

    def setUp(self):
        desired_cap = L.DEVICE_MANAGER
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_reset_password_normal(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Tap(self, L.LINK_FORGET_PASSWORD)
        L.Ketik(self, L.ET_RESET_PWD, L.EMAIL)
        L.Tap(self, L.BTN_SEND_RESET_PWD)
        L.Validasi_Display(self, L.VALIDATE_RESET_PWD)

    def test_reset_password_wrong_email(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Tap(self, L.LINK_FORGET_PASSWORD)
        L.Ketik(self, L.ET_RESET_PWD, L.EMAIL_NOT_REGIST)
        L.Tap(self, L.BTN_SEND_RESET_PWD)
        L.Validasi_Text(self, L.VALIDATE_WRONG_RESET_PWD, 'Kami tidak menemukan merchant')

    def test_reset_password_email_without_at(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Tap(self, L.LINK_FORGET_PASSWORD)
        L.Ketik(self, L.ET_RESET_PWD, L.EMAIL_WITHOUT_AT)
        L.Tap(self, L.BTN_SEND_RESET_PWD)
        L.Validasi_Text(self, L.VALIDATE_WRONG_RESET_PWD, 'format email salah')

    def test_reset_password_email_kosong(self):
        L.ScrollToDownText(self, "Mulai Sekarang")
        L.Tap(self, L.BTN_MULAI_SEKARANG)
        L.Tap(self, L.LINK_FORGET_PASSWORD)
        L.Tap(self, L.BTN_SEND_RESET_PWD)
        L.Validasi_Text(self, L.VALIDATE_WRONG_RESET_PWD, 'email tidak boleh kosong')
