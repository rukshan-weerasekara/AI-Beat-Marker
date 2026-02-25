# 🎬 AI Beat-to-XML Marker Pro

An AI-powered workflow automation tool designed for video editors and animators to synchronize visual edits perfectly with audio beats using signal processing and predictive markers.

## 🔗 Live Demo
Check out the live app here: [https://ai-beat-marker-vloubaucicmimdbdgheesd.streamlit.app/](https://ai-beat-marker-vloubaucicmimdbdgheesd.streamlit.app/)

## 🚀 Project Overview
This tool bridges the gap between **Audio Engineering** and **Video Post-Production**. By leveraging AI-driven onset detection, it automates the tedious process of manual beat-marking, allowing creators to focus on the art of storytelling.

### Key Features:
* **AI Beat Detection:** Powered by `librosa`, it identifies percussive onsets and rhythmic patterns with high precision.
* **Frame-Accurate Mapping:** Automatically converts audio timestamps into video frame positions based on user-defined frame rates (24, 30, 60 FPS).
* **FCPXML Integration:** Generates industry-standard XML files compatible with **Adobe Premiere Pro** and **Final Cut Pro**.
* **Tempo Analysis:** Real-time calculation of **BPM (Beats Per Minute)** to assist in edit pacing.
* **Workflow Efficiency:** Reduces manual marking time by up to **90%** for music-driven edits.



## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Audio Intelligence:** Librosa (Digital Signal Processing)
* **Web Framework:** Streamlit
* **Data Handling:** NumPy
* **Output Format:** XML (FCPXML Schema)

## 🧠 The Logic
The application follows a precise signal-to-metadata pipeline:
1.  **Audio Loading:** Extracting raw audio signals and sampling rates ($sr$).
2.  **Onset Detection:** Utilizing a spectral flux-based algorithm to identify peak energy in the frequency domain.
3.  **Timestamp Conversion:** Mapping detected beats to absolute time indices.
4.  **Temporal Calculation:** Converting seconds into specific frame counts using the formula:
    $$\text{Frame Position} = \text{Time (s)} \times \text{FPS}$$
5.  **XML Serialization:** Embedding these frames into an XML structure that professional NLEs (Non-Linear Editors) can interpret as markers.

---
Developed by **Rukshan Weerasekara** *Creative Technologist | Animator | AI Developer*
