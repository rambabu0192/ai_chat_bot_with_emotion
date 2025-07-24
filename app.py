import streamlit as st 
from emotion_text import detect_emotion_text
from emotion_video import detect_emotion_from_camera
from chatbot import generate_response
from voice import listen_to_user

st.set_page_config(page_title="Emotion-Aware AI Chatbot", layout="centered")

st.title("🤖 Emotion-Aware AI Chatbot")

# Choose input method
input_mode = st.radio("Choose Emotion Input Mode:", ["Text", "Camera","Microphone"])

if input_mode=="Text":
     user_input = st.text_input("You:", "")
     if user_input:
         emotion = detect_emotion_text(user_input)
         response = generate_response(user_input)
         st.write(f"🧠 Detected Emotion: **{emotion}**")
         st.markdown("### 🤖 Bot:")
         st.success(response)
elif input_mode=="Camera":
    st.info("Press 'q' in the webcam window to quit.")
    if st.button("Detect Emotion from Camera"):
        emotion = detect_emotion_from_camera()
        st.success(f"Detected Emotion: {emotion}")

elif input_mode=="Microphone":
    if st.button("Use Microphone"):
        st.write("🎙️Listening...")
        user_input = listen_to_user()
        if user_input:
            emotion = detect_emotion_text(user_input)
            response = generate_response(user_input)
            st.write(f"🗣️ You said: **{user_input}**")
            st.write(f"🧠 Detected Emotion: **{emotion}**")
            st.markdown("### 🤖 Bot:")
            st.success(response)
    
        
    