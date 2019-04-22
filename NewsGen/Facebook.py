import facebook

def postFacebook(text):
    page_access_token = "token"
    graph = facebook.GraphAPI(page_access_token)
    graph.put_photo(image=open("Result.png",'rb'), message=text)