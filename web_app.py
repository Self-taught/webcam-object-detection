import streamlit as st
import cv2
import datetime

x = datetime.datetime.now()

date_local = x.strftime("%A")
time_local = x.strftime("%H:%M:%S")

st.title("Motion Detector")
col1, col2 = st.columns(2)
with col1:
    button = st.button("Start Camera")
with col2:
    stop_button = st.button("Stop Camera")

if button:
    streamlit_image = st.image([])
    video = cv2.VideoCapture(0)
    if stop_button:
        video.release()

    while True:
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=f"{date_local}", org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200), thickness=2,
                    lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=f"{time_local}", org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0), thickness=2,
                    lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
