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

footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: lavender;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: grey;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p> </p>
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/arushi-midha" target="_blank">Arushi Midha</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)   
