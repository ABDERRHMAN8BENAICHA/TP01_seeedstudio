import config

from infrastructure.driver_factory import create_driver
from application.scraper import scrape

# choose storage
from infrastructure.repositories.csv_repository import save as save_csv
from infrastructure.repositories.json_repository import save as save_json


def main():
    driver = create_driver()
    all_products = []

    try:
        for page in range(config.START_PAGE, config.END_PAGE):
            all_products.extend(scrape(driver, page))
    finally:
        driver.quit()

    # 🔥 save in both formats
    save_csv(all_products, config.OUTPUT_FILE)
    save_json(all_products, config.OUTPUT_FILE)

    print("DONE")


if __name__ == "__main__":
    main()
