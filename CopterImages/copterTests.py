from __future__ import division
from PIL import Image

from os import listdir, remove, symlink
from os.path import isfile, join, getsize
from random import shuffle
import os
import sys
from shutil import copyfile
import random
import cv2
import numpy




def crop(savePath, image, x, y, width, height):
	imgwidth, imgheight = image.size
	box = (x, y, x+width, y+height)
	a = image.crop(box)
	return a
	# try:
	# 	p = join(os.getcwd(), savePath, "test.png")
	# 	print(p)
	# 	a.save(p)
	# except:
	# 	pass


backgroundFolder = "Backgrounds/"
targetFolder = "Targets/"

backgroundImages = [f for f in listdir(backgroundFolder) if isfile(join(backgroundFolder, f)) and f != ".DS_Store"]
targetImages = [f for f in listdir(targetFolder) if isfile(join(targetFolder, f)) and f != ".DS_Store"]

backgroundImagePath = backgroundImages[0]
targetImagePath = targetImages[0]

targetImage = Image.open(targetFolder + targetImagePath)

w = 200
h = 200

targetImageSizeW = 15
targetImageSizeH = 15

targetImage.thumbnail((targetImageSizeW, targetImageSizeH), Image.ANTIALIAS)


print(backgroundImagePath)

images = []
backgroundImage = Image.open(backgroundFolder + backgroundImagePath)
randWMax = backgroundImage.size[0] - w
randHMax = backgroundImage.size[1] - h

randTargetWMax = w - targetImageSizeW
randTargetHMax = h - targetImageSizeW

print(randHMax)
print(randWMax)
savePath = ""
for i in range(0, 2) :
	x = random.randint(0, randWMax)
	y = random.randint(0, randHMax)
	randImg = crop("", backgroundImage, x, y, w, h)

	tarX = random.randint(0, randTargetWMax)
	tarY = random.randint(0, randTargetHMax)

	randImg.paste(targetImage, (tarX, tarY), targetImage)
	images.append(randImg)
	p = join(os.getcwd(), savePath, "test" + str(i) + ".png")
	print(p)
	images[i].save(p)

backgroundImage.close()
cvImages = []
# Got the images now, now I need to put them in OpenCV
for im in images :
	cvImages.append(cv2.cvtColor(numpy.array(im), cv2.COLOR_BGR2RGB))

imageWithText = cv2.resize(cvImages[0], (700, 700))
cv2.namedWindow("Display Window", cv2.WINDOW_NORMAL)
cv2.imshow( "Display Window", imageWithText)
cv2.waitKey(0)





















