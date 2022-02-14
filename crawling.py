import csv
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import numpy as np

#global variable

# 1. csv file variable
file_name = 'usa_stock.csv'

# web crawling variable
url = "https://finance.yahoo.com/quote/BOND/history?p=BOND"
col_data = ['date','open','High','low','close','adj Close', 'volume']


#csv file open and write mode
f = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
writer.writerow(col_data)

#url html get
response1 = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

#opening up connection and grabbing page 1
uclient = urlopen(response1)
page_html = uclient.read()
uclient.close()

#parsing data
soup = BeautifulSoup(page_html,"html.parser")

tbody = soup.find_all('tr')[1:]

#columns get 

for i in tbody:
    temp = i.find_all('td')
#exception Throw
    if len(temp) <= 1:
	continue
    col_data2 = [column.get_text().strip() for column in temp]
    writer.writerow(col_data2)

print(col_data2)

plt.plot(col_data2)
plt.show()
