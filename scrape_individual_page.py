import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import sqlite3


conn = sqlite3.connect('data_store.db')


response = requests.get('https://tis.nhai.gov.in/TollInformation.aspx?TollPlazaID=236')
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

plaza_name = soup.find(class_='PA15').find_all('p')[0].find('lable')
print(plaza_name.text)

table = soup.find_all('table', class_='tollinfotbl')[0]
x = str(table)
y = pd.read_html(x)[0].dropna(axis=0, how='all')

cols = y.columns.tolist()
cols.insert(0, 'Date Scrapped')
cols.insert(1, 'Plaza Name')
y['Plaza Name'] = plaza_name.text
y['Date Scrapped'] = date.today()
y = y[cols]
y.to_sql('toll_info', conn, if_exists='append', index=False)

print('a')