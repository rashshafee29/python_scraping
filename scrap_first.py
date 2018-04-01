from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

pretty = soup.prettify()

_1st = soup.find('div', class_='1st')
#print(_1st.text)

val = _1st.h1.text
#print(val)

for div in soup.find_all('div'):
    h1 = div.h1.text
    print(h1)
    p = div.p.text
    print(p)
    print()
