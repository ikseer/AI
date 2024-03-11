import cv2
from pytesseract import pytesseract
import os
def text_extraction(image_path):
    img = cv2.imread( image_path) 

    H , W , __  = img.shape
    # 2.resize the image
    img = cv2.resize(img , None , fx = 0.5 , fy = 0.5 )

    # # 3. convert image to gayscale
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    # convert grayscale image into a binary image  (Binary images have only two possible pixel values, often 0 for black and 1 (or 255) for white)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                            cv2.THRESH_BINARY_INV)

    ####################    Bounding Boxes and Text Extraction  ###################################


    # We define a rectangular kernel using cv2.getStructuringElement in OpenCV.
    rect_kernel = cv2.getStructuringElement( cv2.MORPH_RECT, (12, 12) )

    # (Dilation) acts like a magnifying glass for important parts of the image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 3)

    ############# Text Detection and Cropping ##################
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_NONE)

    result=""

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Draw the bounding box on the text area
        rect=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the bounding box area
        cropped = img[y:y + h, x:x + w]

        # cv2.imwrite('rectanglebox.jpg',rect)  #optional


        # Using tesseract on the cropped image area to get text
        text = pytesseract.image_to_string(cropped)
        result+=text
        result+="\n"
        
        
        # Adding the text to the file
        


    return result


    # # Prepare a copy of the image for drawing
    # img_with_text = img.copy()
    #
    # # Iterate through each contour
    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #
    #     # Draw the bounding box around the word
    #     cv2.rectangle(img_with_text, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #     # Crop the word area
    #     cropped = img[y:y + h, x:x + w]
    #
    #     # Use pytesseract on the cropped image area to get text
    #     text = pytesseract.image_to_string(cropped)
    #
    #     # Add the text above the image
    #     cv2.putText(img_with_text, text, (x ,  y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #
    # # Save the image with boundaries and text
    # cv2.imwrite('image_with_text.jpg', img_with_text)


# 1. load the image
if __name__ == "__main__":
    image_path="Ai_model/Inputs/img.JPG"
    output=text_extraction(image_path)
    with open("text_output2.txt", "w") as file:
        file.write(output)








