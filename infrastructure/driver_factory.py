import os
import stat

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import config


def create_driver():
    options = Options()
    options.binary_location = config.BROWSER_BINARY

    driver_path = ChromeDriverManager(
        driver_version=config.CHROME_VERSION
    ).install()

    # fix path if needed
    if "THIRD_PARTY" in driver_path:
        driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver")

    # 🔥 FIX PERMISSIONS
    st = os.stat(driver_path)
    os.chmod(driver_path, st.st_mode | stat.S_IEXEC)

    return webdriver.Chrome(service=Service(driver_path), options=options)
