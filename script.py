import os
import subprocess
from gtts import gTTS
from langdetect import detect, DetectorFactory

# Fix for consistent langdetect results
DetectorFactory.seed = 0

INPUT_FILE = "myroom.txt"
TEMP_FOLDER = "temp_audio"
OUTPUT_FILE = "output.mp3"

os.makedirs(TEMP_FOLDER, exist_ok=True)

# Read lines
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

audio_files = []

print("[Generating audio files with language detection...]")
for i, line in enumerate(lines):
    try:
        lang = detect(line)
        if lang.startswith("ko"):
            tts_lang = "ko"
        else:
            # Default to English for any non-German detected language
            tts_lang = "en"
    except Exception as e:
        print(f"Could not detect language for line {i}: {line}. Defaulting to English.")
        tts_lang = "en"
    
    print(f"Line {i+1}: Detected language '{lang}', using TTS language '{tts_lang}'")

    tts = gTTS(text=line, lang=tts_lang)
    audio_path = os.path.join(TEMP_FOLDER, f"line_{i:03}.mp3")
    tts.save(audio_path)
    audio_files.append(audio_path)
    print(f"Saved audio: {audio_path}")

# Create concat.txt for ffmpeg with absolute paths
concat_list_path = os.path.join(TEMP_FOLDER, "concat.txt")
with open(concat_list_path, "w", encoding="utf-8") as f:
    for audio_file in audio_files:
        abs_path = os.path.abspath(audio_file).replace("\\", "/")
        f.write(f"file '{abs_path}'\n")

print(f"[Created concat list file at: {concat_list_path}]")

# Merge with ffmpeg
ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_list_path,
    "-c", "copy",
    OUTPUT_FILE
]

print("[Merging audio files with FFmpeg...]")
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"[Merged audio saved to {OUTPUT_FILE}]")
except subprocess.CalledProcessError as e:
    print("[Error merging audio files]")
    print(e)
