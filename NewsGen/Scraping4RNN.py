import requests, random, shutil, time

from requests.exceptions import HTTPError
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from bs4 import BeautifulSoup
import requests

f= open("input.txt", "w+")

i = 1

while(i < 2057):
    print(i)
    text = ""

    link = "https://olhardigital.com.br/noticias/" + str(i)
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')

    for p in soup.find_all("h3"):
        print(p.get_text().rstrip() + "\n")
        f.write(p.get_text().rstrip() + "\n\n")

    i += 1
