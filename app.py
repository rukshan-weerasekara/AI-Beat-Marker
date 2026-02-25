import streamlit as st
import librosa
import numpy as np
import os


st.set_page_config(page_title="AI Beat Marker", page_icon="🎬", layout="centered")

st.title("🎬 AI Beat-to-XML Marker Generator")
st.markdown("Automate your Premiere Pro workflow using AI. Upload your audio and get the XML markers instantly!")


st.sidebar.header("⚙️ Configuration")
fps = st.sidebar.number_input("Frame Rate (FPS)", min_value=1, max_value=120, value=24)
seq_name = st.sidebar.text_input("Sequence Name", value="AI_Beat_Sequence")


audio_file = st.file_uploader("Upload Audio File (MP3, WAV)", type=["mp3", "wav"])

if audio_file is not None:
    with st.spinner("🔍 AI is analyzing the beats..."):
        # Temporary save for librosa to read
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.getbuffer())

        
        y, sr = librosa.load("temp_audio.mp3", sr=None)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        duration_secs = librosa.get_duration(y=y, sr=sr)
        total_frames = int(duration_secs * fps)
        
        
        actual_tempo = float(tempo[0]) if isinstance(tempo, np.ndarray) else float(tempo)
        st.success(f"✅ Found {len(beat_times)} beats at {actual_tempo:.2f} BPM")

        
        xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="5">
<project>
    <name>AI_Beat_Project</name>
    <children>
        <sequence id="sequence-1">
            <name>{seq_name}</name>
            <duration>{total_frames}</duration>
            <rate><timebase>{fps}</timebase><ntsc>FALSE</ntsc></rate>
            <media><video><track></track></video><audio><track></track></audio></media>
            <markers>"""

        for i, t in enumerate(beat_times):
            frame_pos = int(t * fps)
            xml_content += f"""
                <marker>
                    <name>Beat {i+1}</name>
                    <in>{frame_pos}</in><out>{frame_pos}</out>
                    <comment>AI Beat at {t:.2f}s</comment>
                </marker>"""

        xml_content += """
            </markers>
        </sequence>
    </children>
</project>
</xmeml>"""

        
        st.download_button(
            label="📥 Download XML for Premiere Pro",
            data=xml_content,
            file_name="Ruka_Beat_Markers.xml",
            mime="application/xml"
        )
        
     
        os.remove("temp_audio.mp3")

st.info("💡 Tip: Import the downloaded XML into Premiere Pro to see the markers.")
