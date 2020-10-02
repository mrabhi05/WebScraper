import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://quotes.toscrape.com/page/1/")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
weeks = soup.find_all("div", class_="quote")
#print(week[0])

# print(weeks[0].find(class_='text').get_text())
# print(weeks[0].find(class_='author').get_text())
# print(weeks[0].find(class_='tags').get_text())

quote_list = [week.find(class_='text').get_text() for week in weeks]
#print(quote_list)   
author_list = [week.find(class_='author').get_text() for week in weeks]
tag_list = [week.find(class_='tag').get_text() for week in weeks]

quote_stuff = pd.DataFrame(
    {
        'Quote': quote_list,
        'Author': author_list,
        'Tags': tag_list,
    })

print(quote_stuff)

quote_stuff.to_csv('Quotes_list.csv')