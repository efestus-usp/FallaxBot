from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

def setHeadline(text):
    img1 = cv2.imread("Source.jpg", -1)
    img2 = cv2.imread("Template.png", -1) # this one has transparency
    h, w, c = img2.shape

    img1 = cv2.resize(img1, (w, h), interpolation = cv2.INTER_CUBIC)
    result = np.zeros((h, w, 3), np.uint8)

    alpha = img2[:, :, 3] / 255.0
    result[:, :, 0] = (1. - alpha) * img1[:, :, 0] + alpha * img2[:, :, 0]
    result[:, :, 1] = (1. - alpha) * img1[:, :, 1] + alpha * img2[:, :, 1]
    result[:, :, 2] = (1. - alpha) * img1[:, :, 2] + alpha * img2[:, :, 2]

    # Convert the image to RGB (OpenCV uses BGR)
    cv2_im_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # Pass the image to PIL
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)
    # use a truetype font
    font = ImageFont.truetype("arial-bold.ttf", 13)
    fontR = ImageFont.truetype("Arial.ttf", 9)

    # Draw the text
    if len(text) > 50:
        array = text.split(' ')
        str1 = ""
        str2 = ""
        i = 0
        while(len(str1) < 50):
            str1 += array[i] + ' '
            i += 1

        while(i < len(array)):
            str2 += array[i] + ' '
            i += 1

        draw.text((10, 214), str1, font=font, fill=(0, 0, 0))
        draw.text((10, 246), str2, font=font, fill=(0, 0, 0))
    else:
        draw.text((10, 214), text, font=font, fill=(0, 0, 0))

    draw.text((12, 214), "FALLAXNEWS.COM", font=fontR, fill=(80, 80, 80))

    # Get back the image to OpenCV
    result = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()