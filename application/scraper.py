import time
from typing import List
from selenium.webdriver.common.by import By

import config
from domain.product import Product


def scrape(driver, page: int) -> List[Product]:
    if page == 1:
        url = config.BASE
    else:
        url = config.BASE + config.PAGE + str(page)

    print("Scraping", url)
    driver.get(url)
    time.sleep(config.SLEEP_TIME)

    cards = driver.find_elements(By.CSS_SELECTOR, "div.s_ais_hit")
    products = []

    for c in cards:
        try:
            sku = c.find_element(By.CSS_SELECTOR, ".s_ais_p_sku").text
        except:
            sku = ""

        try:
            title = c.find_element(By.CSS_SELECTOR, ".s_ais_p_title").text
        except:
            title = ""

        try:
            desc = c.find_element(By.CSS_SELECTOR, ".s_ais_p_desc").text
        except:
            desc = ""

        try:
            price = c.find_element(By.CSS_SELECTOR, ".s_ais_p_price_now").text
        except:
            price = ""

        try:
            link = c.find_element(By.CSS_SELECTOR, "a.s_ais_p_img").get_attribute("href")
        except:
            link = ""

        try:
            img = c.find_element(By.CSS_SELECTOR, "a.s_ais_p_img img").get_attribute("src")
        except:
            img = ""

        products.append(Product(sku, title, desc, price, link, img))

    return products
