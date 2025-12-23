import requests
from bs4 import BeautifulSoup


def get_book_data(url: str) -> list:
    """
    Fetches HTML and parses book titles and prices.
    :param url: The URL of the book page.
    :return: The list of book titles and prices.
    """
    books = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all('article', class_='product_pod')
        for article in articles:
            title = article.h3.a['title']
            price = article.find('p', class_='price_color').text
            books.append({"Title": title, "Price": price})
    except requests.exceptions.RequestException as e:
        print(f"Scraping error: {e}")
    return books