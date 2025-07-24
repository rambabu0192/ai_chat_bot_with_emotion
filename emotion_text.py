from transformers import pipeline

def detect_emotion_text(text):
    classifier=pipeline("sentiment-analysis",model="j-hartmann/emotion-english-distilroberta-base")
    result=classifier(text)
    return result[0]['label']

# print(detect_emotion_text("I hate you"))