from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2, random, re

str1 = "Incrivelmente surpreendente. Grande exemplo."
str2 = "Uma verdadeira evolução para o mundo moderno."
str3 = "Grande impacto na tecnologia."
str4 = "Grande inovação no mercado."
str5 = "Espera-se um grande impacto na política."
str6 = "A tecnologia mudando a política."
str7 = "Hora de repensar a ética na tecnologia."
str8 = "Autoridades se surpreenderam com a notícia."
str9 = "O governo não se pronunciou ainda."
str10 = "Facebook tenta averiguar a situação."

def setHeadline(text):
    img1 = cv2.imread("Source.jpg", -1)
    img2 = cv2.imread("Template.png", -1) # this one has transparency
    h, w, c = img2.shape

    height, width = img1.shape[0:2]

    if height > 1000 and width > 800:
        img1 = img1[0: 600, 0:600]

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
    fontC = ImageFont.truetype("Arial.ttf", 10)

    txt2 = ""
    # Draw the text
    if len(text) > 45:
        array = text.split(' ')
        txt1 = ""
        txt2 = ""
        i = 0
        while(len(txt1) < 45):
            txt1 += array[i] + ' '
            i += 1

        while(i < len(array)):
            txt2 += array[i] + ' '
            i += 1

        draw.text((10, 214), txt1, font=font, fill=(0, 0, 0))
        draw.text((10, 246), txt2, font=font, fill=(0, 0, 0))

    if not re.search('[a-zA-z0-9]', txt2):
        draw.text((10, 214), text, font=font, fill=(0, 0, 0))
        rnd = random.randint(0, 9)

        if rnd == 0:
            draw.text((10, 250), str1, font=fontC, fill=(80, 80, 80))
        elif rnd == 1:
            draw.text((10, 250), str2, font=fontC, fill=(80, 80, 80))
        elif rnd == 2:
            draw.text((10, 250), str3, font=fontC, fill=(80, 80, 80))
        elif rnd == 3:
            draw.text((10, 250), str4, font=fontC, fill=(80, 80, 80))
        elif rnd == 4:
            draw.text((10, 250), str5, font=fontC, fill=(80, 80, 80))
        elif rnd == 5:
            draw.text((10, 250), str6, font=fontC, fill=(80, 80, 80))
        elif rnd == 6:
            draw.text((10, 250), str7, font=fontC, fill=(80, 80, 80))
        elif rnd == 7:
            draw.text((10, 250), str8, font=fontC, fill=(80, 80, 80))
        elif rnd == 8:
            draw.text((10, 250), str9, font=fontC, fill=(80, 80, 80))
        elif rnd == 9:
            draw.text((10, 250), str10, font=fontC, fill=(80, 80, 80))

    draw.text((12, 214), "FALLAXNEWS.COM", font=fontR, fill=(80, 80, 80))

    # Get back the image to OpenCV
    result = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imwrite('Result.png', result)
