#-*- coding: utf-8 -*-

from wand.image import Image
import os
from pytesseract import image_to_string
from PIL import Image as pillow


imageTest = "C:\\Users\\Greg\\Pictures\\textbookPhotos\\Geography\\1784-1822 Rev Jedidiah Morse\\1784 (1784) Geography Made Easy\\IMG_0654.jpg"

images = "C:\\Users\\Greg\\Pictures\\textbookPhotos"

	
grayDir = os.path.join(images, "grayscale")
bwDir = os.path.join(images, "bw")

if not os.path.isdir(grayDir):
	os.mkdir(grayDir)
if not os.path.isdir(bwDir):
	os.mkdir(bwDir)

grayImg = os.path.join(grayDir, os.path.basename(imageTest))
bwImg = os.path.join(bwDir,  os.path.basename(imageTest))


text = image_to_string(pillow.open(grayImg))
