import streamlit as st

st.title("Video Audio Replacement with AI")

video_file = st.file_uploader("Upload Video File", type=["mp4"])
if video_file is not None:
    with open("input_video.mp4","wb") as f:
        f.write(video_file.getbuffer())
    st.video("input_video.mp4")
    
    if st.button("Process"):
        transcript = transcribe_audio("input_video.mp4")
        corrected_text = correct_transcription(transcript)
        text_to_speech(corrected_text)
        replace_audio("input_video.mp4", "output_audio.wav")
        st.video("output_video.mp4")