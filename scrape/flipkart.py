import requests 
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=mobiles'

response_text = requests.get(url).text
soup = BeautifulSoup(response_text,'html.parser')

price = soup.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
print(price.text)
