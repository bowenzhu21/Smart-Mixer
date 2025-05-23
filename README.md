# 🎧 SmartMixer: AI-Powered DJ Transitions from Any Playlist

**SmartMixer** is an open-source AI DJ system that analyzes the tempo and structure of music tracks and automatically generates seamless, beat-aligned transitions between them — simulating the creative techniques of a real DJ.

Whether you're mixing lo-fi, house, or hip-hop, SmartMixer helps automate the art of DJing by learning how to blend songs together like a pro.

---

## 🚀 Features

- 🧠 **Tempo & Beat Detection** — uses signal processing to find the BPM and beat grid of any song
- 🎛 **Crossfade Engine** — create smooth, automated transitions between two songs
- 🔁 **Playlist Mixer (coming soon)** — input a playlist and receive a single, continuous mix
- 🎚️ **Transition Types (in progress)** — spinbacks, EQ fades, beat drops, and more
- 🎼 **Spotify Integration** — pull BPM and energy data from any Spotify track or playlist

---

## 🛠 Tech Stack

| Layer            | Tools/Libraries                  |
|------------------|----------------------------------|
| Audio Analysis   | `librosa`, `madmom`, `numpy`     |
| Audio Mixing     | `pydub`, `ffmpeg`, `torchaudio`  |
| Web API          | `spotipy` (Spotify API)          |
| Notebooks        | `Jupyter`, `matplotlib`          |
| ML (planned)     | `PyTorch`, `scikit-learn`        |
| Interface (future) | `Streamlit` or `Dash`          |

---

## 📂 Project Structure