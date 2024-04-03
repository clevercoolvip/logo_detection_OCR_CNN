from script5_fg_bg import get_bg
import cv2
import numpy as np

def transformImageUpload(logoFilepath, templateFilePath, outputFolder):
    bg_img = get_bg(logoFilepath)
    output = bg_img
    template1 = cv2.imread(templateFilePath)

    coord = [5, 5, 5+output.shape[0], 5+output.shape[1]]

    template1[coord[0]:coord[2], coord[1]:coord[3]] = output
    cv2.imwrite(outputFolder, template1)
    return