import cv2
from script5_fg_bg import get_bg
from ocr_script import extract_text_with_coordinates
import cv2
import random
import matplotlib.pyplot as plt


def overlay_text_on_image(img, text, coordinates, font_scale, font_thickness, color):
    # Convert the coordinates to tuple format if not already in that format
    print("In function TEXT_ON_IMAGE")
    tt = random.choice(text)
    p1, p2 = coordinates[0], coordinates[2]

    text_coord = [int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2)]

    print(f"Image shape: {img.shape}")
    img[p1[1]:p2[1], p1[0]:p2[0]] = 255
    # Overlay text on the image
    print("Coordinate parameter: ", coordinates)
    print(f"p1: {p1} | p2: {p2}")
    cv2.putText(img, tt, tuple(text_coord), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, font_thickness)

def overlay_text_from_ocr(image, text_with_coordinates, font_scale, font_thickness, color, text):
    for title, title_coordinates, context in text_with_coordinates:
        # Assuming title_coordinates is a list of coordinates, we'll take the first one
        overlay_text_on_image(image, text, title_coordinates, font_scale, font_thickness, color)

##def overlay_text_on_image(img, text, coordinates, font_scale, font_thickness, color):
##    cv2.putText(img, text, coordinates, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, font_thickness)
##
##def overlay_text_from_ocr(image, text_with_coordinates, font_scale, font_thickness, color):
##    for title, title_coordinates, context in text_with_coordinates:
##        overlay_text_on_image(image, "", title_coordinates, font_scale, font_thickness, color)
##
def overlay_text_from_chatgpt(image, generated_text, coordinates, font_scale, font_thickness, color):
    text_lines = generated_text.split("\n")
    max_lines = len(text_lines)
    for i, line in enumerate(text_lines):
        if i >= max_lines:
            break
        new_coordinates = (coordinates[0], coordinates[1] + i * font_scale * 20)
        overlay_text_on_image(image, line, new_coordinates, font_scale, font_thickness, color)


def overlay_rgba_on_rgb(logoFilePath, rgb_template_path, outputFolder, x=0, y=0, text="OpenCV contains putText() method which is used to put text on any image. The method uses following parameters. img: The Image on which you want to write the text. text: The text you want to write on the image"):
    rgba_overlay = get_bg(logoFilePath)
    rgb_image = cv2.imread(rgb_template_path)

    # rgba_overlay = cv2.imread(rgba_overlay_path, -1)
    overlay_alpha = rgba_overlay[:, :, 3] / 255.0  # Normalize alpha channel (0.0 - 1.0)

    # Convert RGB image to BGRA (for compatibility with OpenCV functions)
    bgra_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2RGBA)
    # Use alpha blending to combine the images
    for c in range(3):
        bgra_image[:80, :80, c] = (1 - overlay_alpha) * bgra_image[:80, :80, c] + overlay_alpha * rgba_overlay[:, :, c]

    # Convert back to RGB if desired
    rgb_image_with_overlay = cv2.cvtColor(bgra_image, cv2.COLOR_RGBA2RGB)
    # rgb_image_with_overlay = put_text_with_word_wrap(rgb_image_with_overlay, text, container_pos, container_size, font_scale, font_thickness, color)
    
    text_with_coordinates = extract_text_with_coordinates(rgb_image_with_overlay)

    overlay_text_from_ocr(rgb_image_with_overlay, text_with_coordinates, text=text, font_scale=1, font_thickness=2, color=(0, 0, 255))

    # overlay_text_from_chatgpt(rgb_image, chatgpt_text, coordinates=(x, y), font_scale=0.5, font_thickness=2, color=(255, 0, 0))

    cv2.imwrite(outputFolder, rgb_image_with_overlay)
    return rgb_image_with_overlay





if __name__=="__main__":
    result_image = overlay_rgba_on_rgb("static/formatTemplates/2.PNG", "noBGOutput/test.png", "static/generatedTemplates/output__1.png", x=5, y=5)

    # Display or save the result
    cv2.imshow("Image with Overlay", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

