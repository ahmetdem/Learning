import cv2
import os
import numpy as np

# Set up the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Set the path to the directory containing the training images
train_dir = 'faces'

# Get the image file names and corresponding labels
image_paths = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
face_labels = []
for path in image_paths:
    label = int(os.path.split(path)[-1].split(".")[0])
    face_labels.append(label)

# Train the face recognizer on the images and labels
face_images = []
for path in image_paths:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    face_images.append(img)

recognizer.train(face_images, np.array(face_labels))

# Save the trained model to a file
recognizer.write('trained_model.xml')