import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the default camera
video = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    check, frame = video.read()
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Apply a median blur to the detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.medianBlur(frame[y:y+h, x:x+w], 35)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
    
    # Display the resulting frame
    cv2.imshow("gotch !!!", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all OpenCV windows
video.release()
cv2.destroyAllWindows()
