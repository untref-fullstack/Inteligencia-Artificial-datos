from bs4 import BeautifulSoup
import requests

# Solicitar el contenido de una página web
url = "https://www.google.com/search?q=The+Ramones&tbm=nws"
response = requests.get(url)

# Parsear el contenido con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer todos los enlaces (etiquetas <a>)

for link in soup.find_all('a'):
    print(link.get('href'))
