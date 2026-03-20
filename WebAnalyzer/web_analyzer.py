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

    #Getting all headers and a / p tags

    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    links = soup.find_all('a')
    paragraphs = soup.find_all('p')

    print(f"Number of headings: {len(headings)}")
    print(f"Number of links: {len(links)}")
    print(f"Number of paragraphs: {len(paragraphs)}")

    #Getting word Frequency

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

    print("\nTop 5 most frequent words:")
    for word, count in top_5_words:
        print(f"'{word}': {count}")

    # Part 5: According to the hint given, we are using get_text() and count() here which might produce different results than the way we compared words above
    # This counts substring matches, so it may count the keyword appearing for words like "other" for "the" keyword

    keyword = input("Please enter a keyword to search: ")

    keyword_count = text.count(keyword.lower())

    print(f"The keyword '{keyword}' appears {keyword_count} times in the text.\n")

    """
    Separate Implementation of the above code if we want words only (uses the same words list as before):

    keyword = input("Please enter a keyword to search: ").lower()

    keyword_count = words.count(keyword)

    print(f"The keyword '{keyword}' appears {keyword_count} times in the text")
    """

    #Part 6:

    longest_paragraph = ""
    longest_para_wc = 0

    for para in paragraphs:
        para_text = para.get_text().strip()

        para_words = re.findall(r'\b\w+\b', para_text)

        if len(para_words) < 5:
            continue

        if len(para_words) > longest_para_wc:
            longest_para_wc = len(para_words)
            longest_paragraph = para_text

    print("Longest paragraph:")
    print(longest_paragraph)
    print(f"\nWord count of longest paragraph: {longest_para_wc}")

    #Part 7: Visualizing results

    import matplotlib.pyplot as plt


    headings_count = len(headings)
    links_count = len(links)
    paragraphs_count = len(paragraphs)

    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings_count, links_count, paragraphs_count]
    plt.bar(labels, values)
    plt.title('Group 09')
    plt.ylabel('Count')
    #plt.savefig('web_analysis_results.png')
    plt.show()
 
except Exception as e: 
    print(f"Error fetching content: {e}") 
