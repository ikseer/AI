import pytesseract
from pytesseract import Output
import cv2
import PIL.Image

myConfig = r"--psm 4 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("images-test/ocr-eng.png"), lang='eng', config=myConfig)
print(text)
