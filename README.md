# SeeedStudio Scraper

A scalable Selenium-based scraper for collecting product data from
SeeedStudio.

The project is structured using a simple layered architecture so we can
easily:

-   change storage (CSV, JSON, DB, API)
-   change the target website
-   add new scrapers
-   test components independently

------------------------------------------------------------------------

## ✨ Features

-   Uses Brave browser (Chromium)
-   Automatic ChromeDriver download
-   Multi-page scraping
-   Clean separation between scraping and saving
-   Export to **CSV** and **JSON**
-   Easy to extend with new repositories

------------------------------------------------------------------------

## 📁 Project Structure

    seeed_scraper/
    │
    ├── main.py
    ├── config.py
    │
    ├── domain/
    │   └── product.py
    │
    ├── application/
    │   └── scraper.py
    │
    └── infrastructure/
        ├── driver_factory.py
        └── repositories/
            ├── csv_repository.py
            └── json_repository.py

------------------------------------------------------------------------

## ⚙️ Requirements

``` bash
pip install -r requirements.txt
```

Main dependencies:

-   selenium
-   webdriver-manager

------------------------------------------------------------------------

## ▶️ Run

``` bash
python main.py
```

------------------------------------------------------------------------

## 💾 Output

After execution, you will get:

    seeed_products.csv
    seeed_products.json

------------------------------------------------------------------------

## 🧾 Data Fields

Each product contains:

-   sku
-   title
-   description
-   price
-   product_url
-   image_url

------------------------------------------------------------------------

## 🔎 Preview (sample)

Here are a few example rows produced by the scraper.

  ------------------------------------------------------------------------
  sku                  title                     price
  -------------------- ------------------------- -------------------------
  100025096            Semtech LR2021 LoRa Plus  \$99.00
                       Evaluation Kit-CN490      

  100035909            Semtech LR2021 LoRa Plus  \$99.00
                       Evaluation Kit-US915      

  100039980            Semtech LR2021 LoRa Plus  \$99.00
                       Evaluation Kit-EU868      

  100092748            Chelegance JNCRadio VNA 7 \$339.00
                       Inch 4.4GHz Vector        
                       Network Analyzer          

  100064156            reTerminal E1004 13.3"    \$279.90
                       Full-color ePaper Display 
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 How to Add New Storage

Create a new file inside:

    infrastructure/repositories/

Example:

    mongo_repository.py
    postgres_repository.py
    api_repository.py

Implement a `save(products, filename)` function, then import it in
`main.py`.

------------------------------------------------------------------------

## 🧠 Future Improvements

Possible upgrades:

-   remove sleep → use explicit waits
-   concurrency for faster scraping
-   retry & anti-bot handling
-   Docker image
-   REST API
-   scheduling jobs

------------------------------------------------------------------------

## 📜 License

Educational project.
