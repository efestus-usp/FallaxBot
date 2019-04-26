import facebook
import cogroo_interface as Cogroo

cogroo = Cogroo.Cogroo.Instance()

def postFacebook(text):
    page_access_token = ""
    graph = facebook.GraphAPI(page_access_token)
    graph.put_photo(image=open("Result.png",'rb'), message=text)

