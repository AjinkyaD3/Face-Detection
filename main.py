import cv2 as cv
img=cv.imread('Two.jpg')
# cv.imshow('Grayperson',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade=cv.CascadeClassifier('Haar_Face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=2.2,minNeighbors=3)
print(f'Number Of Faces Are ={len(faces_rect)}')
for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)
        cv.imshow('Person',img)
cv.waitKey(0)