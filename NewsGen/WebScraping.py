import random, time
import cogroo_interface as Cogroo

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

cogroo = Cogroo.Cogroo.Instance()

def get_soup(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'html.parser')

def checkVerb(string):
    doc = cogroo.analyze(string)

    if('#v' in str(doc.sentences[0].tokens) and not string[0].isupper()):
        return True

    return False

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
            textBBC = p.get_text().rstrip().replace("'", "").replace('- ', '')
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
            textG1 = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '')
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
            textOD = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '')
            break

    #GIZMODO
    link = "https://gizmodo.uol.com.br/"
    html = requests.get(link)
    html.raise_for_status()
    html.encoding = "UTF-8"
    soup = BeautifulSoup(html.text, 'html.parser')
    textGiz = ""

    i = 0
    num = random.randint(1, 10)

    for p in soup.find_all("a", {"rel": "bookmark"}):
        i = i + 1
        if num == i:
            textGiz = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '')
            break

    beginSelection = random.randint(0, 3)

    if beginSelection == 0:
        array = textBBC.split()
        for index, str in enumerate(array):
            verb = False

            text += array[index] + ' '

            if checkVerb(array[index]):
                verb = True

            if verb:
                if checkVerb(array[index + 1]):
                    text += array[index + 1] + ' '
                break
    elif beginSelection == 1:
        array = textG1.split()
        for index, str in enumerate(array):
            verb = False

            text += array[index] + ' '

            if checkVerb(array[index]):
                verb = True

            if verb:
                if checkVerb(array[index + 1]):
                    text += array[index + 1] + ' '
                break
    elif beginSelection == 2:
        array = textOD.split()
        for index, str in enumerate(array):
            verb = False

            text += array[index] + ' '

            if checkVerb(array[index]):
                verb = True

            if verb:
                if checkVerb(array[index + 1]):
                    text += array[index + 1] + ' '
                break
    elif beginSelection == 3:
        array = textGiz.split()
        for index, str in enumerate(array):
            verb = False

            text += array[index] + ' '

            if checkVerb(array[index]):
                verb = True

            if verb:
                if checkVerb(array[index + 1]):
                    text += array[index + 1] + ' '
                break

    print(text)

    time.sleep(3)

    ## NEW SENTENCES

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
            textBBC = p.get_text().rstrip().replace("'", "").replace('- ', '').replace(':','')
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
            textG1 = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '').replace(':','')
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
            textOD = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '').replace(':','')
            break

    #GIZMODO
    link = "https://gizmodo.uol.com.br/"
    html = requests.get(link)
    html.raise_for_status()
    html.encoding = "UTF-8"
    soup = BeautifulSoup(html.text, 'html.parser')
    textGiz = ""

    i = 0
    num = random.randint(1, 10)

    for p in soup.find_all("a", {"rel": "bookmark"}):
        i = i + 1
        if num == i:
            textGiz = "\n" + p.get_text().rstrip().replace("'", "").replace('- ', '').replace(':','')
            break

    ## GET ANOTHER SENTENCE TO SUM

    text2 = ""
    verb = False
    check = True

    while(text2 == ""):
        endSelection = random.randint(0, 3)
        if endSelection == 0:
            array = textBBC.split()
            for strlst in array:
                if verb:
                    if check:
                        ## CHECK IF IT'S A CASE OF TWO VERBS
                        if(checkVerb(strlst)):
                            check = False

                        if check:
                            text2 += strlst + ' '

                        check = False
                    else:
                        text2 += strlst + ' '
                else:
                    if(checkVerb(strlst)):
                            verb = True

        elif endSelection == 1:
            array = textG1.split()
            for strlst in array:
                if verb:
                    if check:
                        ## CHECK IF IT'S A CASE OF TWO VERBS
                        if (checkVerb(strlst)):
                            check = False

                        if check:
                            text2 += strlst + ' '

                        check = False
                    else:
                        text2 += strlst + ' '
                else:
                    if (checkVerb(strlst)):
                        verb = True

        elif endSelection == 2:
            array = textOD.split()
            for strlst in array:
                if verb:
                    if check:
                        ## CHECK IF IT'S A CASE OF TWO VERBS
                        if (checkVerb(strlst)):
                            check = False

                        if check:
                            text2 += strlst + ' '

                        check = False
                    else:
                        text2 += strlst + ' '
                else:
                    if (checkVerb(strlst)):
                        verb = True
        elif endSelection == 3:
            array = textGiz.split()
            for strlst in array:
                if verb:
                    if check:
                        ## CHECK IF IT'S A CASE OF TWO VERBS
                        if (checkVerb(strlst)):
                            check = False

                        if check:
                            text2 += strlst + ' '

                        check = False
                    else:
                        text2 += strlst + ' '
                else:
                    if (checkVerb(strlst)):
                        verb = True

    text = text + text2
    text = "\n" + text
    print(text)

    if len(text) > 100:
        return ""

    return text