import cv2.cv as cv

img = cv.LoadImage('ben.jpg') # input image

cascade_face = cv.Load("haarcascade_frontalface_alt.xml")
cascade_eyepair = cv.Load("haarcascade_eye.xml")
cascade_mouth = cv.Load("haarcascade_mcs_mouth.xml")

storage = cv.CreateMemStorage (0)

image_scale = 1

def detect(img):
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
    cv.EqualizeHist(gray, gray)
    faces = cv.HaarDetectObjects(gray, cascade_face, storage,
                                 1.1, 2, 1, (50, 50))
    if faces:
        ((x, y, w, h), n) = faces[0]
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 2, 8, 0)

        eyeroi = (x,int(y+(h/5.5)),w,int(h/3.0))
        mouthroi = (x,int(y+(h/1.5)),w,int(h/2.5))
        cv.SetImageROI(gray, eyeroi)
        eyes = cv.HaarDetectObjects(gray, cascade_eyepair, storage,
                                 1.15, 3, 0, (25, 15))
        cv.SetImageROI(gray, mouthroi)
        mouths = cv.HaarDetectObjects(gray, cascade_mouth, storage,
                                 1.15, 3, 0, (30, 30))
        cv.ResetImageROI(gray)
                               
        if eyes:
            for ((x, y, w, h), n) in eyes:
                pt1 = (x + eyeroi[0], y + eyeroi[1])
                pt2 = (x + w + eyeroi[0], y + h + eyeroi[1])
                cv.Rectangle(img, pt1, pt2, cv.RGB(0, 255, 0), 2, 8, 0)
                               
        if mouths:
            for ((x, y, w, h), n) in mouths:
                pt1 = (x + mouthroi[0], y + mouthroi[1])
                pt2 = (x + w + mouthroi[0], y + h + mouthroi[1])
                cv.Rectangle(img, pt1, pt2, cv.RGB(0, 255, 0), 2, 8, 0)

detect(img)
cv.NamedWindow('Face Detection', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Face Detection', img) 
cv.SaveImage("ben-detect.jpg", img)
cv.WaitKey()