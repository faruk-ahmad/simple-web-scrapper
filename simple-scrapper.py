# lets do the import
from bs4 import BeautifulSoup
import requests

# define the page link
link = 'hello.html'

# lets opent he file in read mode and pass the file handle to BS4
with open(link) as html_file:
    source = BeautifulSoup(html_file, 'lxml')

#print(source.prettify())

# soruce.find will find only the first tag in the page
article = source.find('div', class_='article')

#print(article)

# now lets get the title using the h2 tag and summary using the p tag

title = article.h2.text
summary = article.p.text

# print(f"Title: {title}")
# print(f"Summary: {summary}")


# to get all the tags with the class use find_all
articles = source.find_all('div', class_='article')

for idx, article in enumerate(articles):
    title = article.h2.text
    summary = article.p.text

    print(f"Article: {idx + 1}")

    print(f"\tTitle: {title}")
    print(f"\tSummary: {summary}")
    print()