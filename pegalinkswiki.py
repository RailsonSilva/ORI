from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


""" função que recebe uma URL de um artigo da wikipedia e retorna
uma lista com links para outros artigos da wikipedia contidos nesse
artigo """
def pegaWikiLinks( urlWiki ):
    html = urlopen(urlWiki)
    bs = BeautifulSoup( html, 'html.parser' )
    divbc = bs.find('div', {'id': 'bodyContent'} )
    expregular = re.compile( '^(/wiki)((?!:).)*$' )      # ^ é para fazer a expressão regular casar do ínicio da string. (?!:) é para dizer que NÃO queremos o caracter ':'. O '.' casa com qualquer caracter, ((?!:).) casará então com qualquer caractere exceto :, o * após ((?!:).) casará esse último padrão um número arbitrário de vezes, e, por fim, $ força o casamento até o final da string!
    links = divbc.find_all( 'a', {'href': expregular} )
    baseURL = 'https://pt.wikipedia.org'
    links = [ baseURL + a['href'] for a in links ]
    return links

javisitados = set()

url = 'https://pt.wikipedia.org/wiki/'

filalinks = []

while True:

  javisitados.add(url)
  links = pegaWikiLinks(url)

  print(links)

  for link in links:
    if link not in javisitados:
      filalinks.append( link )
  
  if filalinks == []:
    break
  
  url = filalinks.pop(0)