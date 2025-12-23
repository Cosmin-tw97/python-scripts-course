# Importing from our own package modules
from scraper import get_book_data
from data_handler import save_to_csv


def main():
    URL = "http://books.toscrape.com/"
    OUTPUT = "books_results.csv"

    print("--- Starting Modular Web Scraper ---")

    # 1. Get data
    results = get_book_data(URL)

    # 2. Save data
    if results:
        save_to_csv(results, OUTPUT)
    else:
        print("No data collected.")


if __name__ == "__main__":
    main()