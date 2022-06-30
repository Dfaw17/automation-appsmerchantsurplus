# How to run project!

- make sure python has been installed and configured
- make sure pycharm has been installed and configured
- make sure appium client has been installed and configured
- make sure android studio has been installed and configired
- make sure JAVA has been installed and configured
- clone repository in pycharm
- create new python environtment in project
- install library 
> pip install -r requirements.txt
- run android studio
- run AVD Emulator
- check emulator id in CMD 
> adb devices
- run appium server in CMD 
> appium
- configure device in folder PageObjectModel/Locators.py
> DEVICE_MANAGER
- run project 
> python -m pytest -v --html-report=./report/report.html -p no:cacheprovider --disable-pytest-warnings -W ignore::DeprecationWarning