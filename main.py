import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

# Function to capture and update the webcam feed with face detection
def display_webcam():
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    if not cap.isOpened():
        return

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        if not ret:
            break

        # Convert the OpenCV BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        haar_cascade = cv2.CascadeClassifier('Haar_Face.xml')
        faces_rect = haar_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces_rect:
            cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (255, 125, 152), thickness=3)

        # Convert the RGB frame to a Pillow Image
        pil_image = Image.fromarray(rgb_frame)

        # Convert the Pillow Image to a Tkinter PhotoImage
        img = ImageTk.PhotoImage(image=pil_image)

        # Update the label with the new image
        label.config(image=img)
        label.image = img

        
    cap.release()
    cv2.destroyAllWindows()

# Create a Tkinter window
root = tk.Tk()
root.title("Face Detection")

# Create a label to display the webcam feed
label = tk.Label(root)
label.pack()

# Create a thread to run the webcam feed with face detection
webcam_thread = threading.Thread(target=display_webcam)
webcam_thread.daemon = True  # Allow the thread to exit when the program exits
webcam_thread.start()

root.mainloop()