import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import os
import tempfile

st.title("🎵 YouTube Audio Downloader")

# Input: YouTube video link
link = st.text_input("Enter YouTube Video URL")

if st.button("Download Audio"):
    if link:
        try:
            st.info("Downloading...")
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()

            if video is None:
                st.error("No audio stream found for this video.")
            else:
                # Create temp download location
                with tempfile.TemporaryDirectory() as tmp_dir:
                    audio_path = video.download(output_path=tmp_dir)

                    # Convert to mp3
                    mp3_path = os.path.join(tmp_dir, yt.title[:50].replace(" ", "_") + ".mp3")
                    sound = AudioSegment.from_file(audio_path)
                    sound.export(mp3_path, format="mp3")

                    # Provide download button
                    with open(mp3_path, "rb") as f:
                        st.success("✅ Download Complete!")
                        st.download_button(
                            label="Download MP3",
                            data=f,
                            file_name=os.path.basename(mp3_path),
                            mime="audio/mpeg"
                        )

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")
