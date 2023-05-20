import cv2

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('boo.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_threshold=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,91,11)
text = pytesseract.image_to_string(img)
print(text)
# cv2.imshow("gray",gray)
cv2.imshow("img", img)
cv2.waitKey(0)
