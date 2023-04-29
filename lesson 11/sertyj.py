import cv2
from PIL import Image

image_path = 'cat1.jpg'


cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv2.imread(image_path)

cat_face = cat_face_cascade.detectMultiScale(image)

cat_mouth = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open("glasses.png")
maska = Image.open("maska1.png")

cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
maska = maska.convert("RGBA")

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))

    maska = maska.resize((w, int(h/3)))

    cat.paste(glasses, (x, int(y+h/4)), glasses)

    cat.paste(maska, (x, int(y+h/4)), maska)

    cat.save("cat_with_maska1")

    cat.save("cat_with_glasses.png")

    cat_with_glasses = cv2.imread("cat_with_glasses.png")

    cat_with_maska = cv2.imread("cat_with_maska.png")

    cv2.imshow("Cat_with_glasses", cat_with_glasses)

    cv2.imshow("Cat_with_maska", cat_with_maska)

    cv2.waitKey()





