from bs4 import BeautifulSoup
import requests 

url = 'https://automatetheboringstuff.com/'

response = requests.get(url)
print(response)
print(response.status_code)
# print the HTML content 

#print(response.content)  # binary format        b'a string'

# lets store the content in a file 

# with open('data.txt','w') as f:
#     f.writelines(response.text)


# Lets use BeautifulSoup to convert our HTML content into a BeautfulSoup object

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())


test = soup.find('h1')
print(test.text)

    



