import requests
from bs4 import BeautifulSoup

# Submit a GET requet to the URL and retrieves HTML data that the server sends back
response = requests.get("https://www.drupal.org/docs/develop/coding-standards/list-of-sql-reserved-words")

# Create beautiful soup object with HTML parser
content = response.content
parser = BeautifulSoup(content, "html.parser")

ordered_list = parser.find_all("ol")

print(ordered_list)
keywords = ordered_list[0].find_all("li")

#for keyword in keywords:
    #print(keyword.text)

