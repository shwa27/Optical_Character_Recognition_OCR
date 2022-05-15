import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('woman.jpg')
text = tess.image_to_string(img)

print(text)
