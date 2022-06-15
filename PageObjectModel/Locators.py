import requests
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from assertpy import assert_that
import time


class Locator(object):
    # DEVICE
    DEVICE_MANAGER = {
        # "appium:udid": "e95697de0606",
        # "appium:udid": "P7Q8GAXGLNDA7D5H",
        "appium:udid": "emulator-5554",
        "platformName": "Android",
        "appium:appPackage": "com.surplus_app_merchant.staging",
        "appium:appActivity": "com.surplus_app_merchant.MainActivity",
    }

    # FUNCTION
    @staticmethod
    def ScrollToDownText(self, text):
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
            f'.scrollIntoView(new UiSelector().textContains(\"{text}\"))')

    @staticmethod
    def ScrollModal(self, a, b, c, d):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / a
        endx = screenWidth / b
        starty = screenHeight * c
        endy = screenHeight / d
        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    @staticmethod
    def ChooseExpiredDate(self):
        self.driver.find_element(By.XPATH,
                                 '//android.view.ViewGroup[@content-desc="StartDateButtonRiwayatPemasukan"]').click()
        self.driver.find_element(By.ID, 'android:id/date_picker_header_year').click()
        self.driver.find_element(By.XPATH, '//*[@text="2027"]').click()
        self.driver.find_element(By.ID, 'android:id/button1').click()

    @staticmethod
    def ChooseActiveUntillBulk(self):
        self.driver.find_element(By.XPATH,
                                 '//android.view.ViewGroup[@content-desc="kadaluarsaBtn"]').click()
        self.driver.find_element(By.ID, 'android:id/date_picker_header_year').click()
        self.driver.find_element(By.XPATH, '//*[@text="2027"]').click()
        self.driver.find_element(By.ID, 'android:id/button1').click()

    @staticmethod
    def Add_Menu_Photo_Gallery(self):
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="OpenModalBtn1"]').click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="GaleriBtn"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Tampilkan root"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Galeri"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Album"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Terkini"]').click()
        self.driver.find_element(By.ID, 'com.miui.gallery:id/pick_num_indicator').click()

    @staticmethod
    def Add_Menu_Photo_Camera(self):
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="OpenModalBtn1"]').click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="CameraBtn"]').click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="TakePhotoBtn"]').click()

    @staticmethod
    def Edit_Menu_Photo_Camera(self):
        self.driver.find_element(By.XPATH, '//*[@text="Ganti Foto"]').click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(By.XPATH,
                                 '//android.view.ViewGroup[@content-desc="CameraButtonInputFotoModalRegSerf2"]').click()
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="TakePhotoBtn"]').click()

    @staticmethod
    def Add_Menu_Kategori(self):
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="CategoryInput"]').click()
        time.sleep(0.5)
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 8 / 9
        endy = screenHeight / 9
        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="CheckBtn7"]').click()
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="SaveCatBtn"]').click()

    @staticmethod
    def Edit_Menu_Kategori(self):
        self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="CategoryInput"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@text="Makanan Berat"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="Simpan"]').click()

    @staticmethod
    def Tap(self, elem):
        self.driver.find_element(By.XPATH, elem).click()

    @staticmethod
    def Hapus(self, elem):
        self.driver.find_element(By.XPATH, elem).clear()

    @staticmethod
    def Ketik(self, elem, text):
        self.driver.find_element(By.XPATH, elem).send_keys(text)

    @staticmethod
    def Validasi_Display(self, elem):
        assert_that(self.driver.find_element(By.XPATH, elem).is_displayed()).is_equal_to(True)

    @staticmethod
    def Validasi_Text(self, elem, text):
        assert_that(self.driver.find_element(By.XPATH, elem).text).contains(text)

    @staticmethod
    def Validasi_Not_Empty(self, elem):
        assert_that(self.driver.find_element(By.XPATH, elem).text).is_not_empty()

    @staticmethod
    def Step_Login(self):
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
            f'.scrollIntoView(new UiSelector().textContains(\"Mulai Sekarang\"))')
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Mulai Sekarang"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"EmailInput")]').send_keys('mt@gmail.com')
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"PassInput")]').send_keys('12345678')
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"LoginBtn")]').click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Tutup"]').click()

    @staticmethod
    def Step_Login_Cabang(self):
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)' +
            f'.scrollIntoView(new UiSelector().textContains(\"Mulai Sekarang\"))')
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Mulai Sekarang"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"EmailInput")]').send_keys('mt2@gmail.com')
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"PassInput")]').send_keys('12345678')
        self.driver.find_element(By.XPATH, '//*[contains(@content-desc,"LoginBtn")]').click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Selanjutnya"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Tutup"]').click()

    @staticmethod
    def Api_SF_Kotak_Makan(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '1',
            'donation_price': '2500',
            'order_items[0][stock_id]': '2726',
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        req = requests.post("https://staging.adminsurplus.net/api/v2/customer/orders/self-pickup", data=param,
                            headers={
                                "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9jdXN0b21lclwvYXV0aFwvbG9naW5cL2VtYWlsIiwiaWF0IjoxNjQ1Njc0ODQxLCJleHAiOjE2NDgyNjY4NDEsIm5iZiI6MTY0NTY3NDg0MSwianRpIjoiNHFQUGFjYjJQaVFuRUpqWiIsInN1YiI6MTg4NzQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.ucCgqgh1kTunmc5nFsKGvib4UNK64iY9jLlWQs2ygJY",
                                "Accept": "application/json"})

    @staticmethod
    def Api_Finish_Order(self):
        param = {
            'type': 'ready_stock',
        }
        req = requests.get("https://staging.adminsurplus.net/api/v2/merchant/orders", params=param,
                           headers={
                               "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                               "Accept": "application/json"})
        data = req.json().get('data')[0]['registrasi_order_number']
        requests.post(f'https://staging.adminsurplus.net/api/v2/customer/orders/{data}/settlement?_method=PATCH',
                      headers={
                          "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9jdXN0b21lclwvYXV0aFwvbG9naW5cL2VtYWlsIiwiaWF0IjoxNjQ1Njc0ODQxLCJleHAiOjE2NDgyNjY4NDEsIm5iZiI6MTY0NTY3NDg0MSwianRpIjoiNHFQUGFjYjJQaVFuRUpqWiIsInN1YiI6MTg4NzQsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.ucCgqgh1kTunmc5nFsKGvib4UNK64iY9jLlWQs2ygJY",
                          "Accept": "application/json"})

    @staticmethod
    def Api_Index_Pesanan(self):
        param = {
            'type': 'ready_stock',
        }
        req = requests.get("https://staging.adminsurplus.net/api/v2/merchant/orders", params=param,
                           headers={
                               "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                               "Accept": "application/json"})
        data = len(req.json().get('data'))
        return data

    @staticmethod
    def Api_Delete_Menu(self):
        param = {
            'type': 'ready_stock',
        }
        req = requests.get("https://staging.adminsurplus.net/api/v2/merchant/menus/",
                           headers={
                               "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                               "Accept": "application/json"})
        count = len(req.json().get('data'))
        data_delete = req.json().get('data')[int(count - 1)]['id']
        req2 = requests.delete(f'https://staging.adminsurplus.net/api/v2/merchant/menus/{data_delete}',
                               headers={
                                   "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                                   "Accept": "application/json"})

    @staticmethod
    def Api_Set_Inactive_Menu(self):
        req = requests.get("https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=1",
                           headers={
                               "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                               "Accept": "application/json"})
        count = len(req.json().get('data'))
        data_delete = req.json().get('data')[int(count - 1)]['id']
        result = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/menus/{data_delete}/inactive',
                                headers={
                                    "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                                    "Accept": "application/json"})

    @staticmethod
    def Api_Set_Active_menu(self):
        data = {
            'is_tomorrow': '0',
            'stock': '789',
            'max_active_date': '2025-01-12',
        }
        result = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/menus/2894/active', data=data,
                                headers={
                                    "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDU2ODIxOTksImV4cCI6MTY0ODI3NDE5OSwibmJmIjoxNjQ1NjgyMTk5LCJqdGkiOiJ2c1FoVHRib3ZiUWFReXFxIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.3GB5pFdMc1yLQTh-4mT_Gkmse0zNq4LRFcNOQLrJ3_A",
                                    "Accept": "application/json"})

    @staticmethod
    def Api_Set_Bulk_Menu(self):
        data_menu = requests.get(f'https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=0',
                                 headers={
                                     "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                     "Accept": "application/json"})
        param = {
            'is_tomorrow': '0',
            'max_active_date': '2027-02-28',
            'menu_ids[0]': data_menu.json().get('data')[0]['id'],
            'menu_ids[1]': data_menu.json().get('data')[1]['id'],
            'stocks[0]': '10',
            'stocks[1]': '10',
        }
        active = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/bulk-menus/activate', data=param,
                                headers={
                                    "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                    "Accept": "application/json"})

    @staticmethod
    def Api_Set_Bulk_Menu_1(self):
        data_menu = requests.get(f'https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=0',
                                 headers={
                                     "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                     "Accept": "application/json"})
        param = {
            'is_tomorrow': '0',
            'max_active_date': '2027-02-28',
            'menu_ids[0]': data_menu.json().get('data')[0]['id'],
            'stocks[0]': '10',
        }
        active = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/bulk-menus/activate', data=param,
                                headers={
                                    "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                    "Accept": "application/json"})

    @staticmethod
    def Api_Delete_Bulk(self):
        for i in range(0, 2):
            param = {
                "nama_menu_makanan": f'Test Menu Bulk {i}',
                "merchant_kategori_makanan_id": '5',
                "deskripsi": 'Test Menu Bulk Desc',
                "harga_asli": '2000',
                "harga_jual": '1000',
                "is_non_halal": "0",
                "weight": "0",
            }
            file = {
                'images[0]': open("img/mie.jpg", 'rb'),
            }

            add_menu = requests.post(f'https://staging.adminsurplus.net/api/v2/merchant/menus', data=param, files=file,
                                     headers={
                                         "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                         "Accept": "application/json"})
            print(add_menu.json())

    @staticmethod
    def Api_Delete_Bulk_1(self):
        param = {
            "nama_menu_makanan": f'Test Menu Bulk 1',
            "merchant_kategori_makanan_id": '5',
            "deskripsi": 'Test Menu Bulk Desc',
            "harga_asli": '2000',
            "harga_jual": '1000',
            "is_non_halal": "0",
            "weight": "0",
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }

        add_menu = requests.post(f'https://staging.adminsurplus.net/api/v2/merchant/menus', data=param, files=file,
                                 headers={
                                     "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                     "Accept": "application/json"})

    @staticmethod
    def Api_Inactive_Bulk(self):
        menu_active = requests.get(f'https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=1',
                                   headers={
                                       "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                       "Accept": "application/json"})
        data = {
            'menu_ids[0]': menu_active.json().get('data')[1]['id'],
            'menu_ids[1]': menu_active.json().get('data')[2]['id'],
        }
        set_inactive = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/bulk-menus/inactivate',
                                      data=data,
                                      headers={
                                          "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                          "Accept": "application/json"})

    @staticmethod
    def Api_Inactive_Bulk_1(self):
        menu_active = requests.get(f'https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=1',
                                   headers={
                                       "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                       "Accept": "application/json"})
        data = {
            'menu_ids[0]': menu_active.json().get('data')[1]['id'],
        }
        set_inactive = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/bulk-menus/inactivate',
                                      data=data,
                                      headers={
                                          "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                          "Accept": "application/json"})

    @staticmethod
    def Api_Inactive_Bulk_lebih_1(self):
        menu_active = requests.get(f'https://staging.adminsurplus.net/api/v2/merchant/menus/?is_active=1',
                                   headers={
                                       "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                       "Accept": "application/json"})
        data = {
            'menu_ids[0]': menu_active.json().get('data')[1]['id'],
            'menu_ids[1]': menu_active.json().get('data')[2]['id'],
            'menu_ids[2]': menu_active.json().get('data')[3]['id'],
        }
        set_inactive = requests.patch(f'https://staging.adminsurplus.net/api/v3/merchant/bulk-menus/inactivate',
                                      data=data,
                                      headers={
                                          "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvc3RhZ2luZy5hZG1pbnN1cnBsdXMubmV0XC9hcGlcL3YyXC9tZXJjaGFudFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY3MTQxNDgsImV4cCI6MTY0OTMwNjE0OCwibmJmIjoxNjQ2NzE0MTQ4LCJqdGkiOiJCVVdOUE9uVDNPeTF6alNlIiwic3ViIjo0Mjc1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.IR-rf237bS3P4MWWSH5t755SrzA4q03COFC_2ZgUWv0",
                                          "Accept": "application/json"})

    @staticmethod
    def IZINKAN(self):
        self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()

    # DATA
    EMAIL = "mt@gmail.com"
    EMAIL_WITHOUT_AT = "mtgmail.com"
    EMAIL_NOT_REGIST = "mt99@gmail.com"
    PWD = "12345678"
    PWD_WRONG = "1234567890"
    NAMA_MENU = "Test Menu APPIUM"
    NAMA_MENU_EDIT = "Test Menu APPIUM EDIT"
    DESC_MENU = "Test Menu APPIUM Deskripsi"
    DESC_MENU_EDIT = "Test Menu APPIUM Deskripsi EDIT"
    HARGA_ASLI_MENU = "8000"
    HARGA_ASLI_MENU_EDIT = "12000"

    # LOGIN PAGE
    BTN_MULAI_SEKARANG = '//android.widget.TextView[@text="Mulai Sekarang"]'
    BTN_SELANJUTNYA = '//android.widget.TextView[@text="Selanjutnya"]'
    BTN_TUTUP = '//android.widget.TextView[@text="Tutup"]'
    ET_EMAIL = '//*[contains(@content-desc,"EmailInput")]'
    ET_PWD = '//*[contains(@content-desc,"PassInput")]'
    BTN_MASUK = '//*[contains(@content-desc,"LoginBtn")]'
    VALIDATE_LOGIN = '//android.widget.TextView[@text="Menu aktif"]'
    VALIDATE_WRONG_FORMAT = '//android.widget.TextView[@text="format email salah"]'
    VALIDATE_KURANG_PWD = '//android.widget.TextView[@text="kata sandi kurang dari 6 karakter"]'
    VALIDATE_FEEDBACK_MESSAGE = '//*[contains(@content-desc,"FeedbackModalMessagesText")]'
    VALIDATE_ERROR_MESSAGE = '//*[contains(@content-desc,"ErrorInputMessageModal")]'

    # REGISTER PAGE
    LINK_REGISTER = '//android.widget.TextView[@text="Daftar disini"]'
    BTN_REGISTER = '//android.widget.TextView[@text="Daftar Sekarang"]'
    VALIDATE_REGISTER = '//android.view.View[@text="Registrasi Rekan Surplus"]'

    # RESET PASSWORD
    LINK_FORGET_PASSWORD = '//android.widget.TextView[@text="Lupa Kata Sandi"]'
    ET_RESET_PWD = '//android.widget.EditText[@content-desc="Input"]'
    BTN_SEND_RESET_PWD = '//android.view.ViewGroup[@content-desc="KirimBtn"]'
    VALIDATE_RESET_PWD = '//android.widget.TextView[@content-desc="SuccessMessage"]'
    VALIDATE_WRONG_RESET_PWD = '//*[@content-desc="FeedbackModalMessagesText"]'

    # HOME
    VALIDATE_DATE = "//*[contains(@content-desc,'DateHome')]"
    VALIDATE_NAMA_MERCH = "//*[contains(@content-desc,'MerchantNameHome')]"
    VALIDATE_MENU_ACTIVE_TOTAl = "//*[@content-desc='BarInfoBtn']/android.widget.TextView"
    VALIDATE_BTN_MENU_ACTIVE = "//*[contains(@content-desc,'BarInfoBtn')]"
    VALIDATE_ORDER_TYPE = "//android.widget.TextView[@content-desc='OrderPickupStatusOrderNow0']"
    VALIDATE_NO_ORDER = "//android.widget.ScrollView[@content-desc='OrderNowView']//android.widget.TextView[4]"
    VALIDATE_TGL_ORDER = "//android.widget.ScrollView[@content-desc='OrderNowView']//android.widget.TextView[3]"
    VALIDATE_NAMA_CUST = "//android.widget.ScrollView[@content-desc='OrderNowView']//android.widget.TextView[2]"
    VALIDATE_DETAIL_ORDER = '//android.widget.TextView[@text="Rincian Pesanan"]'
    VALIDATE_KOTAK_MAKAN = '//android.widget.SeekBar[@content-desc="Bottom Sheet"]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView'
    VALIDATE_DETAIL_ORDER_KODE_PESANAN = '//android.widget.TextView[@content-desc="OrderIdOrderDetail"]'
    VALIDATE_DETAIL_ORDER_WAKTU_PESANAN = '//android.widget.TextView[@content-desc="PickupDateOrderDetail"]'
    VALIDATE_DETAIL_ORDER_NAMA_PEMESAN = '//android.widget.TextView[@content-desc="CustNameOrderDetail"]'
    VALIDATE_DETAIL_ORDER_METODE_PENGAMBILAN = '//android.widget.TextView[@content-desc="PickupMethodOrderDetail"]'
    VALIDATE_DETAIL_ORDER_WAKTU_PENGAMBILAN = '//android.widget.TextView[@content-desc="TimeDetailOrderDetail"]'
    VALIDATE_DETAIL_ORDER_PEMBAYARAN = '//android.widget.TextView[@content-desc="MetodePembayaranOrderDetail"]'
    VALIDATE_DETAIL_ORDER_TOTAL_PEMBAYARAN = '//android.widget.TextView[@content-desc="SubtotalOrderDetail"]'
    TAB_TOP_BESOK = '//android.widget.TextView[@text="Besok"]'
    TAB_TOP_SELESAI = '//android.widget.TextView[@text="Selesai"]'
    BTN_MULAI_JUALAN = '//android.widget.TextView[@text="Mulai jualan"]'
    LIST_PESANAN_SELESAI = '//android.view.View[@content-desc="OrderDetailButtonOrderFinish0"]'
    BTN_PHOTO_KOTAK_MAKAN = '//android.view.ViewGroup[@content-desc="KotakmakanBtn"]'
    BTN_OPEN_PHOTO_KOTAK_MAKAN = '//android.view.ViewGroup[@content-desc="OpenCameraBtn"]'
    BTN_TAKE_PHOTO_KOTAK_MAKAN = '//android.view.ViewGroup[@content-desc="TakePhotoBtn"]'
    JUMLAH_PESANAN = '//android.widget.TextView[@content-desc="TotalOrderOrderNow"]'

    # MENU
    TAB_BOT_MENU = '//android.widget.Button[@content-desc="Menu, tab, 2 of 5"]'
    TAB_TOP_MENU_NONAKTIF = '//android.widget.TextView[@text="Menu Nonaktif"]'
    BTN_SELESAI = '//android.widget.TextView[@text="Selesai"]'
    ET_SEARCH_MENU = '//android.widget.EditText[@text="Cari Menu"]'
    VALIDATE_PAGE_MENU = '//android.view.ViewGroup[@content-desc="Menu"]'
    VALIDATE_LIST_NAMA_MENU = '//android.widget.TextView[@content-desc="ListDetailName0"]'
    VALIDATE_LIST_HARGA_MENU = '//android.widget.TextView[@content-desc="ListDetailPrice0"]'
    VALIDATE_SEARCH_INAVAILABLE = '//android.widget.TextView[@text="Menu yang kamu cari tidak ada"]'

    # ADD_MENU
    TAB_BOT_ADD_MENU = '//android.widget.Button[@content-desc="Tambah, tab, 3 of 5"]'
    ET_ADD_NAMA_MENU = '//android.widget.EditText[@content-desc="NameInput"]'
    ET_DESKRIPSI = '//android.widget.EditText[@content-desc="DescInput"]'
    ET_HARGA_ASLI = '//android.widget.EditText[@content-desc="HargaAsliInput"]'
    ET_DISCOUNT_MENU = '//android.widget.ScrollView[@content-desc="Tambah"]/android.view.ViewGroup/android.widget.EditText[3]'
    BTN_SIMPAN_MENU = '//android.widget.TextView[@text="Simpan"]'
    VALIDATE_SUCCESS_ADD_MENU = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    VALIDATE_ADD_MENU_FEED_MODAL = '//android.widget.TextView[@content-desc="FeedbackModalMessagesText"]'
    VALIDATE_DISC_KURANG_50 = '//*[@text="*Diskon antara 50 - 90%"]'

    # EDIT_MENU
    TAB_BOT_EDIT_MENU = '//android.widget.Button[@content-desc="Menu, tab, 2 of 5"]'
    IMG_EDIT_MENU_SETTING = '//android.view.ViewGroup[@content-desc="ListMenu0"]/android.widget.ImageView'
    BTN_EDIT_MENU = '//*[@text="Ubah detail menu"]'
    BTN_SAVE_EDIT_MENU = '//*[@text="Simpan"]'
    ET_DISCOUNT_MENU_EDIT = '//android.widget.ScrollView[@content-desc="EditView"]/android.view.ViewGroup/android.widget.EditText[3]'

    # SET_ACTIVE_MENU
    TOGGLE_ACTIVE_MENU = '//android.widget.Switch[@content-desc="ListSwitch0"]'
    STOCK_ACTIVE_MENU = '//android.widget.EditText[@content-desc="InputStockModalActiveMenu"]'
    BTN_SAVE_ACTIVE_MENU = '//android.view.ViewGroup[@content-desc="SaveButtonCardModalNonActive"]'
    CHECKBOX_BESOK = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[8]'
    VALIDATE_SET_ACTIVE_MENU = '//*[@text="Daftar Menu"]'

    # EDIT_MENU_ACTIVE
    BTN_ATUR_MENU = '//android.view.ViewGroup[@content-desc="TimeButtonCardListActiveMenu0"]'
    BTN_UBAH_STOK = '//*[@text="Ubah stok"]'
    BTN_KADALUARSA = '//*[@text="Ubah kadaluarsa"]'
    BTN_NONACTIVE_MENU_ACTIVE = '//*[@text="Nonaktifkan menu"]'
    BTN_CONFIRM_NONACTIVE = '//android.view.ViewGroup[@content-desc="OkeButtonNonActiveModalActiveMenu"]'
    ET_EDIT_STOCK_MENU_ACTIVE = '//android.widget.EditText[@content-desc="InputStockModalActiveMenu"]'
    BTN_EDIT_SAVE_MENU_ACTIVE = '//android.view.ViewGroup[@content-desc="SaveButtonStockModalActiveMenu"]'
    TOGGLE_INACTIVE_MENU = '//android.widget.Switch[@content-desc="SwitchCardListActiveMenu0"]'

    # PROFILE
    TAB_BOT_PROFILE = '//android.widget.Button[@content-desc="Profile, tab, 5 of 5"]'
    BTN_TOKO_SAYA = '//android.view.ViewGroup[@content-desc="TokoBtn"]'
    BTN_BANTUAN = '//android.view.ViewGroup[@content-desc="HelpBtn"]'
    BTN_HELP_KEBIJAKAN_PRIVASI = '//*[@text="Kebijakan & Privasi"]'
    BTN_HELP_SYARAT_KETENTUAN = '//*[@text="Syarat & Ketentuan"]'
    BTN_HELP_FAQ = '//*[@text="FAQ"]'
    BTN_HELP_BUTUH_BANTUAN = '//*[@text="Butuh Bantuan?"]'
    BTN_HELP_KRITIK_SARAN = '//*[@text="Kritik & Saran"]'
    BTN_TS_PROFILE_TOKO = '//*[@text="Profile Toko"]'
    BTN_TS_PIC_TOKO = '//*[@text="P.I.C Toko"]'
    BTN_TS_KATA_SANDI_TOKO = '//*[@text="Kata Sandi"]'
    BTN_TS_REKENING_TOKO = '//*[@text="Rekening Toko"]'
    ET_HELP_BB_NAMA = '//android.widget.EditText[@content-desc="NamaInputBB"]'
    ET_HELP_BB_EMAIL = '//android.widget.EditText[@content-desc="EmailInputBB"]'
    ET_HELP_BB_PHONE = '//android.widget.EditText[@content-desc="TelpInputBB"]'
    ET_HELP_BB_MSG = '//android.widget.EditText[@content-desc="MessagesInputBB"]'
    BTN_HELP_BB_SEND = '//android.view.ViewGroup[@content-desc="SendButtonBB"]'
    ET_HELP_KS_NAMA = '//android.widget.EditText[@content-desc="NamaInputFeedback"]'
    ET_HELP_KS_EMAIL = '//android.widget.EditText[@content-desc="EmailInputFeedback"]'
    ET_HELP_KS_PHONE = '//android.widget.EditText[@content-desc="TelpInputFeedback"]'
    ET_HELP_KS_MSG = '//android.widget.EditText[@content-desc="MessagesInputFeedback"]'
    CHOOSE_HELP_KS_KAT = '//android.widget.Spinner[@content-desc="CategoryInputFeedback"]'
    CHOOSE_HELP_KS_KAT_KRITIK = '//*[@text="Kritik"]'
    BTN_HELP_KS_SEND = '//android.view.ViewGroup[@content-desc="SendButtonFeedback"]'
    VALIDATE_PAGE_PROFILE = '//android.view.ViewGroup[@content-desc="ProfileView"]'
    VALIDATE_NAME_MERCHANT = '//android.widget.TextView[@content-desc="MerchantNameProfile"]'
    VALIDATE_AREA_MERCHANT = '//android.widget.TextView[@content-desc="MerchantAreaProfile"]'
    VALIDATE_TS_NAMA_TOKO = '//android.widget.EditText[@content-desc="NamaDetailProfile"]'
    VALIDATE_TS_EMAIL_TOKO = '//android.widget.EditText[@content-desc="EmailDetailProfile"]'
    VALIDATE_TS_PHONE_TOKO = '//android.widget.EditText[@content-desc="TelpDetailProfile"]'
    VALIDATE_TS_DETAIL_ADDRESS_TOKO = '//android.widget.EditText[@content-desc="AlamatProfileView"]'
    VALIDATE_TS_OUTLET_NAME_TOKO = '//android.widget.EditText[@content-desc="NamaOutletProfileView"]'
    VALIDATE_TS_NAME_PIC = '//android.widget.EditText[@content-desc="NamaPIC"]'
    VALIDATE_TS_POSISI_PIC = '//android.widget.EditText[@content-desc="PosisiPIC"]'
    VALIDATE_TS_PHONE_PIC = '//android.widget.EditText[@content-desc="TelpPIC"]'
    VALIDATE_TS_NIK_PIC = '//android.widget.EditText[@content-desc="NikPIC"]'
    VALIDATE_TS_BANK_NAME = '//*[@text="Nama Bank"]/following-sibling::android.widget.EditText[1]'
    VALIDATE_TS_NO_REKENING = '//*[@text="Nama Bank"]/following-sibling::android.widget.EditText[2]'
    VALIDATE_TS_NAMA_PEMILIK_REKENING = '//*[@text="Nama Bank"]/following-sibling::android.widget.EditText[3]'
    VALIDATE_HELP_KEBIJAKAN_PRIVASI = '//*[@text="Kebijakan dan privasi"]'
    VALIDATE_HELP_SYARAT_KETENTUAN = '//*[@text="Syarat dan ketentuan"]'
    VALIDATE_HELP_FAQ = '//*[@text="F.A.Q"]'

    # CENTRAL TO CABANG
    BTN_TAMBAH_CABANG = '//android.view.ViewGroup[@content-desc="RegCabangBtn"]'
    BTN_TAMBAH_CABANG_DAFTAR_SEKARANG = '//android.view.ViewGroup[@content-desc="RegisterButtonRegisterCabang"]'
    BTN_CABANG_SAYA = '//android.view.ViewGroup[@content-desc="ListCabangBtn"]'
    BTN_PILIH_CABANG = '//android.view.ViewGroup[@content-desc="SelectCabangButtonListCabang"]'
    BTN_MASUK_CABANG = '//*[@text="Masuk mode cabang"]'
    BTN_CABANG_MODE_TOKO_SAYA = '//android.view.ViewGroup[@content-desc="DetailProfileButtonProfileCabang"]'
    BTN_CABANG_MODE_PIC_TOKO = '//android.view.ViewGroup[@content-desc="PICCabangButtonProfileCabang"]'
    BTN_CABANG_MODE_BOT_TAB_MENU = '//android.widget.Button[@content-desc="MenuCabangNav, tab, 1 of 3"]'
    BTN_CABANG_MODE_TOP_TAB_ALL_MENU = '//*[@text="Semua Menu"]'
    LIST_CABANG = '//android.view.ViewGroup[@content-desc="CardButtonListCabang1"]'
    ET_CARI_CABANG = '//*[@text="Cari Menu"]'
    VALIDATE_TAMBAH_CABANG = '//*[@text="Nama Toko Pusat Required question"]'
    VALIDATE_PAGE_MODE_CABANG = '//*[@text="Mode Cabang"]'
    VALIDATE_PAGE_MODE_CABANG_ALL_MENU = '//android.view.ViewGroup[@content-desc="SemuaMenuView"]'
    VALIDATE_MODE_CABANG_TOKO_SAYA = '//android.view.ViewGroup[@content-desc="DetailProfileCabangView"]'
    VALIDATE_MODE_CABANG_PIC = '//android.view.ViewGroup[@content-desc="PICProfileCabangView"]'
    VALIDATE_MODE_CABANG_MENU_AKTIF = '//*[@text="Menu aktif"]'
    VALIDATE_MODE_CABANG_MENU_AKTIF_NAMA = '//android.widget.TextView[@content-desc="NameCardListActiveMenu0"]'
    VALIDATE_MODE_CABANG_MENU_AKTIF_HARGA_STOCK = '//android.widget.TextView[@content-desc="HargaCardListActiveMenu0"]'
    VALIDATE_MODE_CABANG_MENU_AKTIF_WAKTU = '//android.widget.TextView[@content-desc="DateCardListActiveMenu0"]'
    VALIDATE_MODE_CABANG_MENU_ALL_NAMA = '//android.widget.TextView[@content-desc="NamaMenuSemuaMenu0"]'
    VALIDATE_MODE_CABANG_MENU_ALL_HARGA = '//android.widget.TextView[@content-desc="HargaMenuSemuaMenu0"]'

    # CABANG
    VALIDATE_CABANG = '//android.widget.TextView[@content-desc="MerchantNameHome"]'
    VALIDATE_LIST_ORDER = '//android.widget.TextView[@content-desc="OrderPickupStatusOrderNow0"]'
    VALIDATE_PAGE_MENU_CABANG = '//android.widget.TextView[@content-desc="MasterMenuBtn"]'
    VALIDATE_CABANG_MENU_NONACTIVE = '//android.view.ViewGroup[@content-desc="NonActiveView"]'
    VALIDATE_CABANG_MENU_ACTIVE = '//android.view.ViewGroup[@content-desc="ActiveView"]'
    BTN_CABANG_ATUR_MENU_ACTIVE = '	//android.view.ViewGroup[@content-desc="TimeButtonCardListActiveMenu0"]'

    # INACTIVE BULK
    BTN_PILIH_SEKALIGUS = '//*[@text="Pilih Sekaligus"]'
    BTN_NONAKTIFKAN_SEKALIGUS = '//*[@text="Nonaktifkan Menu"]'
    BTN_NONAKTIFKAN_SEKALIGUS_CONFIRM = '//*[@text="Ya, Saya yakin"]'
    CARD_1 = '//android.view.ViewGroup[@content-desc="CardListActiveMenu1"]'
    CARD_2 = '//android.view.ViewGroup[@content-desc="CardListActiveMenu2"]'

    # ACTIVE BULK
    CARD_1_Active = '//android.widget.TextView[@content-desc="ListDetailName0"]'
    CARD_2_Active = '//android.widget.TextView[@content-desc="ListDetailName1"]'
    CARD_3_Active = '//android.widget.TextView[@content-desc="ListDetailName2"]'
    ET_STOCK_BULK_1 = '//android.widget.EditText[@content-desc="stock0"]'
    ET_STOCK_BULK_2 = '//android.widget.EditText[@content-desc="stock1"]'
    ET_STOCK_BULK_3 = '//android.widget.EditText[@content-desc="stock2"]'
    BTN_AKTIFKAN_SEKALIGUS = '//*[@text="Aktifkan menu sekaligus"]'
    BTN_SAVE_ACTIVE_BULK = '//android.view.ViewGroup[@content-desc="SaveButtonCardModalNonActive"]'
    VALIDATE_EXPIRED_DATE_NULL = '//*[@text="Kadaluarsa belum diisi"]'

    # DELETE BULK
    CARD_1_DELETE = '//*[@text="Test Menu Bulk 0"]'
    CARD_2_DELETE = '//*[@text="Test Menu Bulk 1"]'
    CARD_DELETE_CANCEL = '//android.widget.TextView[@content-desc="ListDetailName0"]'
    BTN_HAPUS_SEKALIGUS = '//*[@text="Hapus menu sekaligus"]'
    BTN_HAPUS_SEKALIGUS_CONFIRM = '//*[@text="Ya, Saya yakin"]'
    BTN_HAPUS_SEKALIGUS_CANCEL = '//*[@text="Batalkan"]'
