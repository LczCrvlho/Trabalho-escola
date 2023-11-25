import requests
from bs4 import BeautifulSoup
url = 'https://tribunademinas.com.br/notícias/esportes'

response = requests.get(url)
if response.status_code ==200:
        
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    noticia = soup.find_all("h2" , class_ = 'title')

    for k in noticia:
        print(k.text)

else:
    print("Deu erro")
