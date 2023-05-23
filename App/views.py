from django.shortcuts import render
from tokenize import String
from PIL.Image import Image
from PIL import Image
import pytesseract
import re


def home(request):
    return render(request, 'home.html')

data={}
def extract_text(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        image = Image.open(image_file)

        texts = pytesseract.image_to_string(image)

        return render(request, 'extract.html', {'text': texts, 'image': image_file})
    return render(request, 'extract.html')
# Create your views here.
