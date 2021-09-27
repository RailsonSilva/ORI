from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def pegaWikiLinks( urlWiki ):
    html = urlopen(urlWiki)
    bs = BeautifulSoup(html, 'html.parser' )
    divbc = bs.find('div', {'id' : 'bodyContent'})
    expregular = re.compile('^(/wiki)((?!:).)*$')
    links = divbc.find_all( 'a' , { 'href' : expregular})
    baseURL = 'https://pt.wikipedia.org'
    links = [ baseURL + a['href'] for a in links]
    return links

javisitados = set()
links = pegaWikiLinks('https://pt.wikipedia.org/wiki/Zeca_Pagodinho')
print(links)

