from bs4 import BeautifulSoup
import requests

req = requests.get('https://bdnews24.com/cricket/')
#print(req.text)

soup = BeautifulSoup(req.text, 'lxml')

divs = soup.find_all('div', {'class': 'article news first default '})
for d in divs:
    title = d.find_all('div', {'class': 'text'})
    #only heading
    #title1 = d.find('div', {'class': 'text'})
    #t = title1.find_all('h2')
    #for m in t:
    #    print(m.text)
    #    print()
    #Heading + Small details
    for msg in title:
        print(msg.text)
        print("---")
    p = d.find('p', {'class': 'summary'}).text
    #print(p)
