import requests
from bs4 import BeautifulSoup

# PASO 01
# url = "https://quotes.toscrape.com/"
# html = requests.get(url).text
# soup = BeautifulSoup(html, "html.parser")

# quotes = soup.find_all("span", class_="text")
# for quote in quotes:
#     print(quote.text)

# PASO 02
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

data = []

for item in soup.select("div.quote"):
    quote = item.find("span", class_="text").text
    author = item.find("small", class_="author").text
    data.append((quote, author))

# PASO 03
def limpiar(texto):
    return texto.replace("“", "").replace("”", "").strip()

data_limpia = [(limpiar(q), a) for q, a in data]

print(data_limpia)

# PASO 04
import csv

with open("citas.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Cita", "Autor"])
    writer.writerows(data_limpia)
