import cv2
from deepface import DeepFace

def detect_emotion_from_camera():
    cap = cv2.VideoCapture(0)
    emotion = "Neutral"
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        try:
            analysis=DeepFace.analyze(frame, actions=['emotion'])
            emotion = analysis[0]['dominant_emotion']
        except:
            pass
        cv2.putText(frame, emotion, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Emotion Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return emotion

# emotion = detect_emotion_from_camera()
# print("Detected emotion:", emotion)