import os
os.chdir("C:\\Users\\veris\\PycharmProjects\\Terminal+ new release testing - 11\\pytestpackage")

os.system("adb kill-server")
os.system("adb devices")
os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_script_small_device.py")