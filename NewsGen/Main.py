import ImageProcessing, WebScraping, Facebook
import cv2

text = WebScraping.run()

img1 = cv2.imread("Source.jpg", -1)

while(img1 is None or text == ""):
    text = WebScraping.run()
    img1 = cv2.imread("Source.jpg", -1)

ImageProcessing.setHeadline(text)
Facebook.postFacebook(text)


