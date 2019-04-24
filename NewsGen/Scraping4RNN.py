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

# OLHAR DIGITAL
while(i < 4581):
    print(i)

    link = "https://gizmodo.uol.com.br/page/"+ str(i) +"/"
    html = requests.get(link)
    html.raise_for_status()
    html.encoding = "UTF-8"
    soup = BeautifulSoup(html.text, 'html.parser')

    for p in soup.find_all("a", {"rel": "bookmark"}):
        print(p.get_text().rstrip() + "\n")
        f.write(p.get_text().rstrip() + "\n\n")

    i += 1
