from bs4 import BeautifulSoup
import requests

res = requests.get('http://quotes.toscrape.com/')

#print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
#print(soup.prettify())

for quote in soup.find_all('span', {'class': 'text'}):
    print(quote.text)
    print()

divs = soup.find_all('div', {'class': 'quote'})
for d in divs:
    msg = d.find('span', {'class': 'text'})
    a = d.span.text
    print("<-->" + a)
    print(msg.text)

    author = d.find('small')

    print(author.text)

    print()
