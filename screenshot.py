import numpy as np 
import cv2 as cv
from PIL import ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
"""Takes a SS, converts SS to np array, converts colors of np array to RGB, and displays this onto a separate window"""

def retrieveSS():
	screenshot = ImageGrab.grab()
	screenshot = np.array(screenshot)
	screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
	return screenshot


while(True):

	screenshot = retrieveSS()

	words_in_ss = pytesseract.image_to_string(screenshot)
	needle = "picking"
	if needle in words_in_ss.lower():
		print('Agent Select')
	else:
		print('Not in Agent Select')
	cv.imshow('Computer Vision', screenshot)

	if cv.waitKey(1) == ord('q'):
	    cv.destroyAllWindows()
	    break



print('Done')