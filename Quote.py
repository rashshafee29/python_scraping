from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('QuoteOfDay.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date', 'Quote'])

res = requests.get('https://www.brainyquote.com/quote_of_the_day')
soup = BeautifulSoup(res.text, 'lxml')

quote = soup.find('img', {'class': ' p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
print(quote['alt'])
date = soup.find('div', {'class': 'qotdSubt'})
print(date.text)
csv_writer.writerow([date.text, quote['alt']])
csv_file.close()

