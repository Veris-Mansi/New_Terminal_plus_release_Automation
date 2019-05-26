import pytest
import time
from utilities.Resources2 import *

@pytest.mark.usefixtures("data","driver")
class TestWalk_In():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']
        self.offline_walkin_details=data['offline_walkin_details']

    def test_login(self):
        time.sleep(3)
        time.sleep(0.5)
        permission_buttons_small_device(self.driver)
        time.sleep(1.5)
        self.driver.press_keycode(4)
        time.sleep(0.5)
        self.driver.start_activity("com.veristerminal", ".MainActivity")
        time.sleep(1)

        q=WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="domainPicker"]/android.widget.Spinner')))
        q.click()

        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')))
        r.click()
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization ID')))
        p.send_keys('N1')
        self.driver.hide_keyboard()
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization Code')))
        p.send_keys('1')

        self.driver.hide_keyboard()
        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'LOGIN')))
        r.click()

        for i in range(5):
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Check-In"]')))
            m.click()

            for i in range(10):
                m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[16]/android.view.ViewGroup')))
                m.click()

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
            r.click()

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NDA_ONLY')))
            r.click()

            time.sleep(2)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'signatureField')))
            r.click()

            """r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//android.view.ViewGroup[@content-desc="signatureField"]/android.widget.LinearLayout/android.view.View')))
            r.click()"""
            time.sleep(1)
            user_action = TouchAction(self.driver)
            user_action.press(x=221, y=901).move_to(x=393, y=911).release().perform()
            time.sleep(1)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
            r.click()

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Confirm Check-in')))
            r.click()
            print("executed "+str(i))
            time.sleep(1)
