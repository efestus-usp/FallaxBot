import facebook

def postFacebook(text):
    page_access_token = "token"
    graph = facebook.GraphAPI(page_access_token)
    facebook_page_id = "309166486447185"
    graph.put_photo(image=open("Result.png",'rb'), message=text)