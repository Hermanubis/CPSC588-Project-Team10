from openai import OpenAI
import requests
from bs4 import BeautifulSoup

# key = "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"
apiKey = "KEY_HERE"

client = OpenAI(
    api_key = apiKey
)

def fetch_first_article_text(keyword):
    # Step 1: Fetch the search page
    search_url = f"https://radiopaedia.org/search?q={keyword}&scope=all&lang=us"
    response = requests.get(search_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Step 2: Parse the search page to find the link to the first article
    soup = BeautifulSoup(response.text, 'html.parser')
    first_article_link = soup.find('a', class_='search-result search-result-article')  # This class may change; you need to inspect the website to determine the right one
    
    if not first_article_link:
        return None

    # Step 3: Fetch the article page
    article_url = f"https://radiopaedia.org{first_article_link['href']}"
    print(article_url)
    article_response = requests.get(article_url)
    article_response.raise_for_status()

    # Step 4: Extract all text from the article
    article_soup = BeautifulSoup(article_response.text, 'html.parser')
    article_text = article_soup.get_text()

# Eliminate empty lines
    filtered_text = '\n'.join([line.strip() for line in article_text.split('\n') if line.strip()])

    # Remove everything after "Promoted articles (advertising)"
    if "Promoted articles (advertising)" in filtered_text:
        filtered_text = filtered_text.split("Promoted articles (advertising)")[0]

    return filtered_text

def talk_to_gpt(prompt):
    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant, skilled in coming up with educational contents for university students."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
    
    )
    return chat_completion.choices[0].message

# Example
keyword = "MR enteroclysis"
text = fetch_first_article_text(keyword)
# print(text) 
user_prompt = "generate 10 questions ragarding {keyword} based on this information and provide the answer \n" + text
chatbot_response = talk_to_gpt(user_prompt)
print(chatbot_response)