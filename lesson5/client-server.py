from bs4 import BeautifulSoup
import requests
response=requests.get('https://mfd.ru/currency/?currency=USD')
soup=BeautifulSoup(response.text,'html.parser')
s=soup.find('table',{"class":'mfd-table mfd-currency-table'})
s=s.find_all('td')
for i in s:
    print(i)
print(s[0])
