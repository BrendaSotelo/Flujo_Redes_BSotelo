# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:33:32 2019

@author: Brenda Sotelo
"""

from PIL import Image
import matplotlib.pyplot as imprimir
imagen=Image.open("vegeta.jpg")
imagen1= imagen.convert('1')
imprimir.imshow(imagen)
imprimir.imshow(imagen1)

print(imagen.size)