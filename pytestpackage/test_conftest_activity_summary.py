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

    @pytest.mark.order1
    @pytest.mark.dependency(name="Start activity")
    def test_start_activity(self):
        try:
            start_activity(self.driver)
        except Exception as e:
            print(e)
            print("unable to start activity ")

    @pytest.mark.order2
    @pytest.mark.dependency(name="Login activity",depends=["Start activity"])
    def test_login(self):
        try:
            login(self.driver)

        except Exception as e:
            print (e)
            assert False

    def test_activity_summary(self):

        try:
            time.sleep(5)
            checkin = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Check-Out"]')))
            checkin.click()
            contact=setting_contact(self.driver)
            Next(self.driver)
            activity_summary(self.driver,self.walkin_details)
            Next(self.driver)
            activity_checkOut(self.driver,self.walkin_details)
        except:
            print("Exception")
            takeScreenshot(self.driver)
            assert False
