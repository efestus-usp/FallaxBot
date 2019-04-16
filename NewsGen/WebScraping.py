import requests, random
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
import json

def get_soup(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'html.parser')

def run():

    #BBC
    link1 = "https://www.bbc.com/portuguese/topics/31684f19-84d6-41f6-b033-7ae08098572a"
    html1 = requests.get(link1).text
    soup = BeautifulSoup(html1, 'html.parser')
    text = ""

    i = 0
    num = random.randint(1, 20)

    for p in soup.find_all('h3'):
        i = i + 1
        if num == i:
            print(p.get_text().rstrip())
            text = p.get_text().rstrip()
            break




    query = text.encode('ascii', 'ignore').decode('ascii')
    image_type = "ActiOn"
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
    soup = get_soup(url, header)

    ActualImages = []  # contains the link for Large original images, type of  image
    for a in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link, Type))

    ###print images

    j = random.randint(0, 10)
    for i, (img, Type) in enumerate(ActualImages):
        if i == j:
            break

    urllib2.urlretrieve(img, "Source.jpg")

    return text