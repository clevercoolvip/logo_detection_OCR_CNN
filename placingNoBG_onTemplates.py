import cv2
from script5_fg_bg import get_bg
from ocr_script import extract_text_with_coordinates
import cv2

def overlay_text_on_image(img, text, coordinates, font_scale, font_thickness, color):
    # Convert the coordinates to tuple format if not already in that format
    p1, p2 = coordinates[0], coordinates[2]
    # Overlay text on the image
    cv2.putText(img, text, tuple(p1), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, font_thickness)

def overlay_text_from_ocr(image, text_with_coordinates, font_scale, font_thickness, color):
    for title, title_coordinates, context in text_with_coordinates:
        # Assuming title_coordinates is a list of coordinates, we'll take the first one
        overlay_text_on_image(image, "Honda Motors", title_coordinates, font_scale, font_thickness, color)

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

# def overlay_rgba_on_rgb(logoFilePath, rgb_template_path, outputFolder, x=0, y=0, chatgpt_text="ChatGPT generated text"):
#     rgba_overlay = get_bg(logoFilePath)
#     rgb_image = cv2.imread(rgb_template_path)

#     text_with_coordinates = extract_text_with_coordinates(rgb_image)

#     overlay_text_from_ocr(rgb_image, text_with_coordinates, font_scale=0.5, font_thickness=2, color=(0, 0, 0))

#     # overlay_text_from_chatgpt(rgb_image, chatgpt_text, coordinates=(x, y), font_scale=0.5, font_thickness=2, color=(255, 0, 0))

#     cv2.imwrite(outputFolder, rgb_image)
#     return rgb_image





# def put_text_with_word_wrap(img, text, container_pos, container_size, font_scale, font_thickness, color):
#     # Create a copy of the image to draw on
#     img_with_text = img.copy()

#     # Define the position and size of the container
#     container_x, container_y = container_pos
#     container_width, container_height = container_size

#     # Define the padding for the text
#     padding_x = 10
#     padding_y = 10

#     # Split the text into words
#     words = text.split()

#     # Initialize variables to track the current line and position
#     current_line = ''
#     current_width = 0
#     current_height = 0

#     # Loop through each word in the text
#     for word in words:
#         # Get the size of the current line with the new word added
#         size = cv2.getTextSize(current_line + word, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)

#         # If adding the new word would make the line too wide, start a new line
#         if current_width + size[0][0] + padding_x > container_width:
#             current_line = ''
#             current_height += size[0][1] + padding_y
#             current_width = 0

#         # Add the word to the current line
#         current_line += word + ' '
#         current_width += size[0][0] + padding_x

#         # If the current line exceeds the height of the container, stop adding words
#         if current_height + size[0][1] > container_height:
#             break

#         # Draw the current line on the image
#         cv2.putText(img_with_text, current_line, (container_x + padding_x, container_y + current_height + size[0][1]), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, font_thickness)

#     return img_with_text



def overlay_rgba_on_rgb(logoFilePath, rgb_template_path, outputFolder, x=0, y=0, text="OpenCV contains putText() method which is used to put text on any image. The method uses following parameters. img: The Image on which you want to write the text. text: The text you want to write on the image"):
    rgba_overlay = get_bg(logoFilePath)
    rgb_image = cv2.imread(rgb_template_path)

    text_with_coordinates = extract_text_with_coordinates(rgb_image)

    overlay_text_from_ocr(rgb_image, text_with_coordinates, font_scale=0.5, font_thickness=2, color=(0, 0, 0))

    # overlay_text_from_chatgpt(rgb_image, chatgpt_text, coordinates=(x, y), font_scale=0.5, font_thickness=2, color=(255, 0, 0))

    cv2.imwrite(outputFolder, rgb_image)



    # rgba_overlay = cv2.imread(rgba_overlay_path, -1)
    overlay_alpha = rgba_overlay[:, :, 3] / 255.0  # Normalize alpha channel (0.0 - 1.0)

    # Convert RGB image to BGRA (for compatibility with OpenCV functions)
    bgra_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2RGBA)
    # Use alpha blending to combine the images
    for c in range(3):
        bgra_image[:80, :80, c] = (1 - overlay_alpha) * bgra_image[:80, :80, c] + overlay_alpha * rgba_overlay[:, :, c]

    # Convert back to RGB if desired
    rgb_image_with_overlay = cv2.cvtColor(bgra_image, cv2.COLOR_RGBA2RGB)




    container_pos = (100, 100)
    container_size = (300, 200)
    font_scale=0.3
    font_thickness = 1
    color = (0, 0, 255)

    # rgb_image_with_overlay = put_text_with_word_wrap(rgb_image_with_overlay, text, container_pos, container_size, font_scale, font_thickness, color)
    
    text_with_coordinates = extract_text_with_coordinates(rgb_image_with_overlay)

    overlay_text_from_ocr(rgb_image_with_overlay, text_with_coordinates, font_scale=0.5, font_thickness=2, color=(0, 0, 0))

    # overlay_text_from_chatgpt(rgb_image, chatgpt_text, coordinates=(x, y), font_scale=0.5, font_thickness=2, color=(255, 0, 0))

    cv2.imwrite(outputFolder, rgb_image_with_overlay)
    return rgb_image_with_overlay





if __name__=="__main__":
    result_image = overlay_rgba_on_rgb("static/formatTemplates/1.PNG", "noBGOutput/test.png", "static/generatedTemplates/output__1.png", x=5, y=5)

    # Display or save the result
    cv2.imshow("Image with Overlay", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

