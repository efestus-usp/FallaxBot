import ImageProcessing, WebScraping, Facebook
import cv2
from apscheduler.schedulers.blocking import BlockingScheduler

text = WebScraping.run()

img1 = cv2.imread("Source.jpg", -1)

while (img1 is None or text == ""):
    text = WebScraping.run()
    img1 = cv2.imread("Source.jpg", -1)

ImageProcessing.setHeadline(text)
Facebook.postFacebook(text)

def run():
    text = WebScraping.run()

    img1 = cv2.imread("Source.jpg", -1)

    while (img1 is None or text == ""):
        text = WebScraping.run()
        img1 = cv2.imread("Source.jpg", -1)

    ImageProcessing.setHeadline(text)
    Facebook.postFacebook(text)

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', seconds=7200)
scheduler.start()




