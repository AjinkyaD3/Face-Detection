
while True:
    # this is to apture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # this convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # and this detect faces in the frame
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        # Draw a rectangle around each detected face u can change the color by chnaging rgb code ani thicknes here @AjinkyaD3
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 165, 152), thickness=3)

    # and this will display the frame with detected faces 
    cv.imshow('Face Detection', frame)

    # u can press 'q' to exit the loop and close the window
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# releasing  the camera and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
#@AjinkyaD3
