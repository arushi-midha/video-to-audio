import streamlit as st
import moviepy.editor as mp
import os

st.title("Video to Audio Converter")

# Allow users to upload a video file
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if video_file is not None:
    st.video(video_file)
    
    # Save the uploaded video file temporarily
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.getbuffer())
    
    # Extract audio from the video file
    if st.button("Extract Audio"):
        video = mp.VideoFileClip("temp_video.mp4")
        audio = video.audio
        audio.write_audiofile("output_audio.mp3")
        
        # Allow user to download the audio file
        with open("output_audio.mp3", "rb") as f:
            st.download_button(
                label="Download Audio",
                data=f,
                file_name="output_audio.mp3",
                mime="audio/mpeg"
            )

    
