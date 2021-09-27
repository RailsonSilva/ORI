import requests

cep = 38400165

resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json")
if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)
else:
    print("Erro no acesso à API viacep!")

print(dados['logradouro'])

# Introdução ao Web Scraping com BeautifulSoup

# Web scraping é o ato de usar uma ferramenta para coletar informações da internet sem o uso de uma API.


from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)