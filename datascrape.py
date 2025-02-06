import requests
from bs4 import BeautifulSoup

def scrape_python_news():
    url = "https://www.python.org/blogs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('h3', class_='event-title')
    for item in news_items:
        print(item.text.strip())

def scrape_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('h3', class_='gs-c-promo-heading__title')
    for item in news_items:
        print(item.text.strip())

def scrape_nasa_image():
    url = "https://www.nasa.gov/multimedia/imagegallery/iotd.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_title = soup.find('h2', class_='image-feature-title')
    if image_title:
        print(image_title.text.strip())

def scrape_goodreads_quotes():
    url = "https://www.goodreads.com/quotes"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quoteText')
    for quote in quotes[:5]:  # Limit to first 5 quotes
        print(quote.get_text(strip=True, separator=' ').split('―')[0])

def scrape_wikipedia_featured():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    featured = soup.find('div', id='mp-tfa')
    if featured:
        print(featured.get_text(strip=True))


def main():
    while True:
        print("\nWeb Scraping Menu:")
        print("1. Scrape Python.org news")
        print("2. Scrape BBC News top stories")
        print("3. Scrape NASA's Image of the Day")
        print("4. Scrape Goodreads Quotes of the Day")
        print("5. Scrape Wikipedia's Featured Article")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print("\nScraping Python.org news...")
            scrape_python_news()
        elif choice == '2':
            print("\nScraping BBC News top stories...")
            scrape_bbc_news()
        elif choice == '3':
            print("\nScraping NASA's Image of the Day...")
            scrape_nasa_image()
        elif choice == '4':
            print("\nScraping Goodreads Quotes of the Day...")
            scrape_goodreads_quotes()
        elif choice == '5':
            print("\nScraping Wikipedia's Featured Article...")
            scrape_wikipedia_featured()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("\nScraping completed.")

if __name__ == "__main__":
    main()

# Update the test function
def test_main_function(monkeypatch, capsys):
    # Simulate user input '6' to exit the program
    monkeypatch.setattr('builtins.input', lambda _: '6')
    main()
    captured = capsys.readouterr()
    assert "Exiting the program..." in captured.out