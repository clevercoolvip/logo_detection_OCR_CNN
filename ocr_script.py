import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_with_coordinates(image):
    if isinstance(image, str):  # Check if image is a file path
        image = cv2.imread(image)  # Read the image using cv2 if it's a file path
    
    result = reader.readtext(image)  # Pass the image to readtext() function

    text_with_coordinates = []
    title = None
    context=""
    for detection in result:
        text = detection[1]
        coordinates = detection[0]
        if text.isupper():
            if title:
                text_with_coordinates.append((title, title_coordinates, context))
            title = text
            title_coordinates = coordinates
            context = ""
        else:
            context += text + " "
    if title:
        text_with_coordinates.append((title, title_coordinates, context))

    return text_with_coordinates



##def extract_text_with_coordinates(image):
##    result = reader.readtext(image)
##
##    text_with_coordinates = []
##    title = None
##    for detection in result:
##        text = detection[1]
##        coordinates = detection[0]
##        if text.isupper():
##            if title:
##                text_with_coordinates.append((title, title_coordinates, context))
##            title = text
##            title_coordinates = coordinates
##            context = ""
##        else:
##            context += text + " "
##    if title:
##        text_with_coordinates.append((title, title_coordinates, context))
##
##    return text_with_coordinates

"""
import easyocr
import cv2
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_with_coordinates(image_path):

    image = cv2.imread(image_path)

    result = reader.readtext(image)

    # Extract text and coordinates
    text_with_coordinates = []
    title = None
    for detection in result:
        text = detection[1]
        coordinates = detection[0]
        if text.isupper():
            if title:
                text_with_coordinates.append((title, title_coordinates, context))
            title = text
            title_coordinates = coordinates
            context = ""
        else:
            context += text + " "
    if title:
        text_with_coordinates.append((title, title_coordinates, context))

    return text_with_coordinates
"""
    

if __name__ == "__main__":
    image_path = 'tp201-sasi5-presentation169-10-360-403.jpg'

    text_with_coordinates = extract_text_with_coordinates(image_path)


    for title, title_coordinates, context in text_with_coordinates:
        print("Title:", title)
        print("Title Coordinates:", title_coordinates)
        print("Context:", context)
        print()

