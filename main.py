import cv2 as cv
Cam=cv.VideoCapture(0)
while True:
    # this is to apture a frame from the camera
    ret, frame = Cam.read()

    if not ret:
        break

    haar_cascade=cv.CascadeClassifier('Haar_Face.xml')
    # and this detect faces in the frame
    faces_rect = haar_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        # Draw a rectangle around each detected face u can change the color by chnaging rgb code ani thicknes here 
        cv.rectangle(frame,(x, y), (x + w, y + h), (255, 125, 152), thickness=3)

    # and this will display the frame with detected faces 
    cv.imshow('Face Detection--Press q to exit', frame)

    # u can press 'q' to exit the loop and close the window
    ''' Exit the loop when the 'q' key is pressed
        # Here if u printing the frame data then use this code to get out of looop
        # if keyboard.read_event('q'):
        break'''
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# releasing  the camera and close all OpenCV windows
Cam.release()
cv.destroyAllWindows()

