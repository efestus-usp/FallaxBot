import ImageProcessing, WebScraping, Facebook, ImageScraping, NeuralNetworkOutput
import cv2, random
from apscheduler.schedulers.blocking import BlockingScheduler

c = random.randint(0, 1)

if(c == 0):
    text = WebScraping.run()
else:
    text = NeuralNetworkOutput.getText()

if text != "":
    ImageScraping.getImage(text)

img1 = cv2.imread("Source.jpg", -1)

while (img1 is None or text == ""):
    c = random.randint(0, 1)

    if (c == 0):
        text = WebScraping.run()
    else:
        text = NeuralNetworkOutput.getText()

    if text != "":
        ImageScraping.getImage(text)

    img1 = cv2.imread("Source.jpg", -1)

ImageProcessing.setHeadline(text)
Facebook.postFacebook(text)

def run():
    c = random.randint(0, 1)

    if (c == 0):
        text = WebScraping.run()
    else:
        text = NeuralNetworkOutput.getText()

    if text != "":
        ImageScraping.getImage(text)

    img1 = cv2.imread("Source.jpg", -1)

    while (img1 is None or text == ""):
        c = random.randint(0, 1)

        if (c == 0):
            text = WebScraping.run()
        else:
            text = NeuralNetworkOutput.getText()

        if text != "":
            ImageScraping.getImage(text)

        img1 = cv2.imread("Source.jpg", -1)

    ImageProcessing.setHeadline(text)
    Facebook.postFacebook(text)

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', seconds=3600)
scheduler.start()




