import pytesseract
from pytesseract import Output
import cv2
import PIL.Image
import json

myConfig = r"--psm 4 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("imgs/prescription.png"), lang='eng', config=myConfig)
types = text.split('\n')

def converter(types):
    out = []
    for index in range(len(types)):
        dic = {"name": "NAN", "times": "NAN", "dose": "NAN", "notes": "NAN"}
        if len(types[index]):
            type = types[index].split()
            dic["name"] = type[0]
            if "time" in type: dic["times"] = type[type.index("time") - 1]
            if "times" in type: dic["times"] = type[type.index("times") - 1]
            if "mm" in type: dic["dose"] = type[type.index("mm") - 1]
            if "--" in type:
                note, i = "", type.index("--") + 1
                while i < len(type):
                    note += type[i] + " "
                    i += 1
                dic["notes"] = note
            to_json = json.dumps(dic)
            out.append(to_json)
    return out
print(*converter(types), sep='\n')

"""
Page segmentation modes(psm):

0- Orientation and script detection (OSD) only.
1- Automatic page segmentation with OSD.
2- Automatic page segmentation, but no OSD, or OCR. (not implemented)
3- Fully automatic page segmentation, but no OSD. (Default)
4- Assume a single column of text of variable sizes.
5- Assume a single uniform block of vertically aligned text.
6- Assume a single uniform block of text.
7- Treat the image as a single text line.
8- Treat the image as a single word.
9- Treat the image as a single word in a circle.
10- Treat the image as a single character.
11- Sparse text. Find as much text as possible in no particular order.
12- Sparse text with OSD.
13- Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
"""

"""
OCR Engine modes(oem):

0- Legacy engine only.
1- Neural nets LSTM engine only.
2- Legacy + LSTM engines.
3- Default, based on what is available.
"""
