import easyocr

def detect_text_with_coordinates(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read the image
    result = reader.readtext(image_path)

    # Extract text and coordinates from the result
    text_with_coordinates = []
    for detection in result:
        text = detection[1]
        bbox = detection[0]
        x_min, y_min = bbox[0][0], bbox[0][1]
        x_max, y_max = bbox[2][0], bbox[2][1]
        text_with_coordinates.append({
            'text': text,
            'coordinates': {
                'x_min': x_min,
                'y_min': y_min,
                'x_max': x_max,
                'y_max': y_max
            }
        })

    return text_with_coordinates

#usage:
image_path = 'image.jpg'
detected_text_with_coordinates = detect_text_with_coordinates(image_path)
for item in detected_text_with_coordinates:
    print("Text:", item['text'])
    print("Coordinates:", item['coordinates'])
