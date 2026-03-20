import requests
from bs4 import BeautifulSoup

import re

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

headers = { 
    "User-Agent": "lab07-web-analyzer" 
}


try: 
    response = requests.get(url, headers=headers) 
    response.raise_for_status()  # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}") 

    #     Gettign all headers and a / p tags

    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    links = soup.find_all('a')
    paragraphs = soup.find_all('p')

    print(f"Number of headings: {len(headings)}")
    print(f"Number of links: {len(links)}")
    print(f"Number of paragraphs: {len(paragraphs)}")

    #     Getting word Frequency

    text = soup.get_text().lower()
    words = re.findall(r'\b\w+\b', text)

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    top_5_words = sorted_words[:5]

    print("Top 5 most frequent words:")
    for word, count in top_5_words:
        print(f"'{word}': {count}")

except Exception as e: 
    print(f"Error fetching content: {e}") 
