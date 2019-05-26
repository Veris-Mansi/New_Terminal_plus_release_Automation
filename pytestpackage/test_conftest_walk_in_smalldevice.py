
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

    @pytest.mark.order3
    @pytest.mark.dependency(name="fresh_user_walkin",depends=["Login activity"])
    def test_fresh_user_walkin(self):
        walkin_visitor(self.driver,self.walkin_details)

