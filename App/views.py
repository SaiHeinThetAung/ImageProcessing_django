from django.shortcuts import render
from tokenize import String
from PIL.Image import Image
from PIL import Image
import pytesseract
import re


def home(request):
    return render(request, 'home.html')


data = {}


def extract_text(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        image = Image.open(image_file)

        res = pytesseract.image_to_string(image)
        result = res.split('\n')
        for text in result:
            if re.findall('^Ma|^Maung|^Daw|^U', text):
                data['Name'] = text[0:len(text) - 11]
            if re.findall('^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)', text):
                data['Date'] = text
            if re.findall('Ks$', text):
                data['Amount'] = text[1:]
            if re.findall('^\d{10}', text):
                data['Id'] = text
        return render(request, 'extract.html', {'data': data})
    return render(request, 'home.html')
# Create your views here.
