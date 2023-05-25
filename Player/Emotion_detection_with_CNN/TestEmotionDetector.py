import cv2
import numpy as np
import os
from keras.models import model_from_json

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# Load json and create model
json_file = open('C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# Load weights into the model
emotion_model.load_weights("C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/model/emotion_model.h5")
print("Loaded model from disk")

# Start the webcam feed
cap = cv2.VideoCapture(0)
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Original width of the video
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a list to store detected emotions and face coordinates
emotions = []

# Load face cascade classifier
face_detector = cv2.CascadeClassifier('C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/haarcascades/haarcascade_frontalface_default.xml')

def predict_emotion(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # Iterate over each detected face
    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

        # Predict the emotion
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        emotion = emotion_dict[maxindex]

        # Display emotion label on the face
        cv2.putText(frame, emotion, (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Store the emotion and face coordinates
        emotions.append((emotion, (x, y, w, h)))

    return frame


if not os.path.exists('images'):
    os.makedirs('images')

if __name__ == "__main__":
    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        
        # Perform emotion detection
        frame_with_emotions = predict_emotion(frame)
        
        # Display the frame with emotions
        cv2.imshow('Emotion Detection', frame_with_emotions)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

