import requests
from bs4 import BeautifulSoup


response = requests.get('https://tis.nhai.gov.in/TollInformation.aspx?TollPlazaID=236')
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

plaza_name = soup.find(class_='PA15').find_all('p')[0].find('lable')
print(plaza_name.text)