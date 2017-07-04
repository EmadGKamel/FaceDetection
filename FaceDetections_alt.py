import cv2

#read image (1)
gray = cv2.imread('baby1.jpg', 0)

#load Haar cascade file (2)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

#convert image to grayscale (3)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#display image in grayscale
cv2.imshow('gray', gray)

#detecting faces in images and return it's X and Y coordinate plus it's wedith and height (4)
face = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

#draw a rectangle around the detected faces and write a string "Baby" in the left upper side (5)
for (x,y,w,h) in face:
	cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
	cv2.putText(img,'Baby',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,150,0),1,cv2.LINE_AA)

	#displaying the image after detecting (6)
cv2.imshow('face', img)

#wait for pressing 'q' to exit
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
