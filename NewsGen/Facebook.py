import facebook

def postFacebook():
    page_access_token = ""
    graph = facebook.GraphAPI(page_access_token)
    graph.put_photo(image=open("Result.png",'rb'), message="Teste")