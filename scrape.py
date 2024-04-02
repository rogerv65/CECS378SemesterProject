import requests
from bs4 import BeautifulSoup
import re

from grab import *


# Function to extract visible text from a webpage
def extract_visible_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage


            soup = BeautifulSoup(response.content, 'html.parser')
            visible_text = soup.get_text()
            visible_text_list = visible_text.split()

            # remove words that are only 1 character or longer than 20
            visible_text_list = [elem for elem in visible_text_list if (len(elem) > 1  and len(elem) <= 20)]


            # Remove punctuation marks from each element in the array
            # translator = str.maketrans('', '', string.punctuation)
            # visible_text_list = [element.translate(translator) for element in visible_text_list]

            # shorten the list to 100 words max
            if(len(visible_text_list) > 100):
                visible_text_list = visible_text_list[:100]



            return visible_text_list

        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching URL: {url}. Exception: {e}")
        return None




def main():
    username = input("Enter the username to search: ")
    urls = grab(username)
    # print(urls)

    # List of Sherlock URLs
    sherlock_urls_list = urls.strip().split('\n')

    sherlock_urls_list = sherlock_urls_list[0:50] 

    # Extract visible text from each URL
    for url in sherlock_urls_list:
        print(f"Fetching content from URL: {url}")
        visible_text = extract_visible_text(url)
        if visible_text:
            with open(username + '_words.txt', 'a') as file:
                file.write(', '.join(visible_text))
                file.write("\n")



        # print()



if __name__ == "__main__":
    main()
