# encoding=utf8
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')
from tesserocr import PyTessBaseAPI
from pdf2image import convert_from_path

fileName = 'output.txt'

print('Opening PDF...')
pages = convert_from_path(sys.argv[1], 500)
print('Generating image...')
index = 0;
for page in pages:
	if index == 2:
   		page.save('out.jpg', 'JPEG')
   	index += 1
print('Image Generated!')
print('Reading image text...')

images = ['out.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        #print(api.GetUTF8Text())
        file = open(fileName, 'w')
        file.write(api.GetUTF8Text())
        file.close()
os.remove("out.jpg")
print('Text saved to: ' + fileName)
