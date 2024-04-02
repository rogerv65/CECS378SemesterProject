import requests
from bs4 import BeautifulSoup
from grab import *


# Sample list of links obtained from Sherlock
links = [
    'https://www.example.com/profile1',
    'https://www.example.com/profile2',
    # Add more links here...
]

# Function to scrape text from a single link
def scrape_text_from_link(link):
    try:
        # Send an HTTP request to the link
        response = requests.get(link)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the page
        text = soup.get_text()

        return text
    except Exception as e:
        print(f"Error scraping {link}: {e}")
        return None

# Function to scrape text from multiple links
def scrape_text_from_links(links):
    scraped_texts = []
    for link in links:
        text = scrape_text_from_link(link)
        if text:
            scraped_texts.append(text)
    return scraped_texts

# Call the function to scrape text from the provided links
# scraped_texts = scrape_text_from_links(links)

# Print or process the scraped text
# for idx, text in enumerate(scraped_texts, start=1):
#     print(f"Text from link {idx}:")
#     print(text)
#     print("=" * 50)

def main():
    username = input("Enter the username to search: ")
    urls = grab(username)
    print(urls)


if __name__ == "__main__":
    main()
