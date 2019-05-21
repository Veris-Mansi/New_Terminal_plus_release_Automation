import pytest
from utilities.Resources2 import *
import unittest

@pytest.mark.usefixtures("data","driver")
class TestLogin():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']

    def test_login(self):
            time.sleep(2)
            login(self.driver)
            checkIn(self.driver)
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,'mobileNumberTab')))
            p.click()
            setting_contact(self.driver)
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NextButton')))
            p.click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'back')))
            p.click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'emailTab')))
            p.click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'emailAddress')))
            p.send_keys('m@gmail.com')
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
            p.click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'back')))
            p.click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'iHaveQR')))
            p.click()

            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Cancel')))
            p.click()

            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'settingsScreen')))
            p.click()
            assert True
