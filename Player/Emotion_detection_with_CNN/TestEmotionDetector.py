import cv2
import numpy as np
import os
import time
from keras.models import model_from_json

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# load json and create model
json_file = open('C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/model/emotion_model.h5")
print("Loaded model from disk")

# start the webcam feed
#cap = cv2.VideoCapture(0)

# pass here your video path
# you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
cap = cv2.VideoCapture(0)
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # largeur d'origine de la vidéo
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def prediction(frame) -> str:

    face_detector = cv2.CascadeClassifier('C:/Users/Dev1/Desktop/standard_display/Player/Emotion_detection_with_CNN/haarcascades/haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces available on camera
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on the camera and Preprocess it
    for (x, y, w, h) in num_faces:
        
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4) 
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

        # predict the emotions
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        return emotion_dict[maxindex]
        
    return None



if not os.path.exists('images'):
    os.makedirs('images')

emotions = []

if __name__ == "__main__":
                
    print('main...')
    
    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
    
        emotion = prediction(frame)
        print("Emotion détectée: ", emotion)
        
        if emotion is not None:
            frame = cv2.resize(frame, (original_width, original_height))
            cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.imshow('Emotion Detection', frame)
            
            # Enregistrer l'image avec l'émotion détectée dans un fichier
            img_name = 'image_{}_{}.jpg'.format(len(emotions), emotion)
            img_path = os.path.join('images', img_name)
            cv2.imwrite(img_path, frame)
            
            emotions.append((img_name, emotion))  # Ajouter l'image et l'émotion détectée à la liste
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Afficher la liste d'images avec leurs émotions détectées
print(emotions)

cap.release()
cv2.destroyAllWindows()