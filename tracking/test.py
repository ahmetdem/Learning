import cv2

# Load the trained face recognizer from file
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.xml')

# Load the face detection cascade classifier
face_cascade = cv2.CascadeClassifier(r"C:\Users\ahmet\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

# Open a video stream
cap = cv2.VideoCapture(0)

# Loop through each frame of the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through each detected face
    for (x, y, w, h) in faces:
        # Extract the face region from the grayscale image
        face_roi = gray[y:y+h, x:x+w]

        # Recognize the face using the trained model
        label, confidence = recognizer.predict(face_roi)

        # Draw a rectangle around the face and label it with the recognized name
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(label), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the video stream with the detected faces and recognized names
    cv2.imshow('Video Stream', frame)

    # Check if the user has pressed the 'q' key to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
