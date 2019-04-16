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

    text = ""

    #BBC
    link1 = "https://www.bbc.com/portuguese/topics/31684f19-84d6-41f6-b033-7ae08098572a"
    html1 = requests.get(link1).text
    soup = BeautifulSoup(html1, 'html.parser')
    textBBC = ""

    i = 0
    num = random.randint(1, 20)

    for p in soup.find_all('h3'):
        i = i + 1
        if num == i:
            textBBC = p.get_text().rstrip()
            break

    #G1
    link2 = "https://g1.globo.com/economia/tecnologia/"
    html2 = requests.get(link2).text
    #print(html2)
    soup = BeautifulSoup(html2, 'html.parser')
    textG1 = ""

    i = 0
    num = random.randint(1, 10)

    for p in soup.find_all("a", {"class": "feed-post-link gui-color-primary gui-color-hover"}):
        i = i + 1
        if num == i:
            textG1 = "\n" + p.get_text().rstrip()
            break

    #OlharDigital
    link3 = "https://olhardigital.com.br/noticias/"
    html3 = requests.get(link3).text
    soup = BeautifulSoup(html3, 'html.parser')
    textOD = ""

    i = 0
    num = random.randint(1, 30)

    for p in soup.find_all("h3"):
        i = i + 1
        if num == i:
            textOD = "\n" + p.get_text().rstrip()
            break

    beginSelection = random.randint(0, 2)

    if beginSelection == 0:
        array = textBBC.split()
        for str in array:
            verb = False
            text += str + ' '
            link = "https://www.dicio.com.br/pesquisa.php?q=" + str
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')

            for p in soup.find_all("li"):
                if "verb" in p.get_text():
                    verb = True
                    break
                if "substantivo":
                    break

            if verb:
                break
    elif beginSelection == 1:
        array = textG1.split()
        for str in array:
            verb = False
            text += str + ' '
            link = "https://www.dicio.com.br/pesquisa.php?q=" + str
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')

            for p in soup.find_all("li"):
                if "verb" in p.get_text():
                    verb = True
                    break
                if "substantivo":
                    break

            if verb:
                break
    elif beginSelection == 2:
        array = textOD.split()
        for str in array:
            verb = False
            text += str + ' '
            link = "https://www.dicio.com.br/pesquisa.php?q=" + str
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')

            for p in soup.find_all("li"):
                if "verb" in p.get_text():
                    verb = True
                    break
                if "substantivo":
                    break

            if verb:
                break

    print(text)

    #BBC
    link1 = "https://www.bbc.com/portuguese/topics/31684f19-84d6-41f6-b033-7ae08098572a"
    html1 = requests.get(link1).text
    soup = BeautifulSoup(html1, 'html.parser')
    textBBC = ""

    i = 0
    num = random.randint(1, 20)

    for p in soup.find_all('h3'):
        i = i + 1
        if num == i:
            textBBC = p.get_text().rstrip()
            break

    #G1
    link2 = "https://g1.globo.com/economia/tecnologia/"
    html2 = requests.get(link2).text
    #print(html2)
    soup = BeautifulSoup(html2, 'html.parser')
    textG1 = ""

    i = 0
    num = random.randint(1, 10)

    for p in soup.find_all("a", {"class": "feed-post-link gui-color-primary gui-color-hover"}):
        i = i + 1
        if num == i:
            textG1 = "\n" + p.get_text().rstrip()
            break

    #OlharDigital
    link3 = "https://olhardigital.com.br/noticias/"
    html3 = requests.get(link3).text
    soup = BeautifulSoup(html3, 'html.parser')
    textOD = ""

    i = 0
    num = random.randint(1, 30)

    for p in soup.find_all("h3"):
        i = i + 1
        if num == i:
            textOD = "\n" + p.get_text().rstrip()
            break

    ## GET ANOTHER SENTENCE TO SUM

    endSelection = random.randint(0, 2)
    verb = False

    if endSelection == 0:
        array = textBBC.split()
        for strlst in array:

            if verb:
                text += strlst + ' '
            else:
                link = "https://www.dicio.com.br/pesquisa.php?q=" + strlst
                html = requests.get(link).text
                soup = BeautifulSoup(html, 'html.parser')

                for p in soup.find_all("li"):
                    if "verb" in p.get_text():
                        verb = True
                        break
                    if "substantivo":
                        break
    elif endSelection == 1:
        array = textG1.split()
        for strlst in array:

            if verb:
                text += strlst + ' '
            else:
                link = "https://www.dicio.com.br/pesquisa.php?q=" + strlst
                html = requests.get(link).text
                soup = BeautifulSoup(html, 'html.parser')

                for p in soup.find_all("li"):
                    if "verb" in p.get_text():
                        verb = True
                        break
                    if "substantivo":
                        break
    elif endSelection == 2:
        array = textOD.split()
        for strlst in array:

            if verb:
                text += strlst + ' '
            else:
                link = "https://www.dicio.com.br/pesquisa.php?q=" + strlst
                html = requests.get(link).text
                soup = BeautifulSoup(html, 'html.parser')

                for p in soup.find_all("li"):
                    if "verb" in p.get_text():
                        verb = True
                        break
                    if "substantivo":
                        break

    print(text)
    text = "\n" + text

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
    j = random.randint(0, 1)

    for i, (img, Type) in enumerate(ActualImages):
        if i == j:
            break

    opener = urllib2.FancyURLopener({})
    opener.version = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36'
    opener.retrieve(img, 'Source.jpg')

    return text