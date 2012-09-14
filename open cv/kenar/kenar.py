import sys
import cv2.cv as cv
say = 1
while(say < 7):
	resim = str(say)+".jpg"

	imcolor = cv.LoadImage(resim)
	image = cv.LoadImage(resim, cv.CV_LOAD_IMAGE_GRAYSCALE)
	cornerMap = cv.CreateMat(image.height, image.width, cv.CV_32FC1)

	cv.CornerHarris(image,cornerMap,3)

	for y in range(0, image.height):
	 for x in range(0, image.width):
	  harris = cv.Get2D(cornerMap, y, x)
	  if harris[0] > 10e-06:
	   cv.Circle(imcolor,(x,y),2,cv.RGB(155, 0, 25))

	cv.NamedWindow('Halit Alptekin', cv.CV_WINDOW_AUTOSIZE)
	cv.SaveImage("kayit -" + resim, imcolor)
	say = say+1
