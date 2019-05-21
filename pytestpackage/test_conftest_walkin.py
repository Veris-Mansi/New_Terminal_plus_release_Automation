import pytest
import unittest
from utilities.Resources2 import *

@pytest.mark.usefixtures("data","driver")
class TestWalkIn(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']

    def test_fresh(self):
        walkin_visitor(self.driver, self.walkin_details)

    def test_autofetch_user_(self):
        autofetch_user(self.driver,self.walkin_details)

    def test_member_check_in(self):

        try:
            user_action = TouchAction(self.driver)
            checkIn(self.driver)
            time.sleep(0.5)
            setting_contact_member(self.driver)
            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_details)
            emergency_details_autofetch(self.driver, self.member_details)
            unique_id_autofetch(self.driver, self.member_details['unique_id'])
            self.driver.find_element_by_accessibility_id('nextButton').click()
            NDA_screen(self.driver)
            Govt_Id_Retake(self.driver)
            time.sleep(1)
            takeScreenshot(self.driver)
            user_action.tap(x=285, y=809).perform()
            time.sleep(0.5)
            takeScreenshot(self.driver)
            user_action.tap(x=482, y=810).perform()
            activity_complete(self.driver, self.member_details)
            check_out(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise


