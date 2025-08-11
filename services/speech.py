import replicate
import os
import requests
import platform
import time
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
SPEECH_MODEL = os.getenv("SPEECH_MODEL")
VOICE = os.getenv("VOICE")

client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# Ensure ./sounds folder exists relative to this file
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "sounds")
os.makedirs(SOUNDS_DIR, exist_ok=True)

def play_audio_windows(file_path):
    import winsound
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

def text_to_speech(text):
    print("🎙️ Generating speech...")

    output = client.run(
        SPEECH_MODEL,
        input={
            "text": text,
            "voice": VOICE
        }
    )

    print(f"DEBUG: Raw output from speech model: {repr(output)}")

    audio_url = None

    # Handle Replicate's FileOutput object with .url attribute
    if hasattr(output, "url"):
        audio_url = output.url
    elif isinstance(output, str):
        audio_url = output.strip()
    elif isinstance(output, list) and len(output) > 0 and isinstance(output[0], str):
        audio_url = output[0].strip()
    elif isinstance(output, dict):
        for key in ["audio", "audio_url", "url"]:
            if key in output and isinstance(output[key], str):
                audio_url = output[key].strip()
                break

    print(f"DEBUG: Extracted audio_url: {audio_url}")

    if not audio_url or len(audio_url) == 0:
        raise ValueError(f"Could not find audio URL in speech model output: {output}")

    # Create unique filename with timestamp
    timestamp = int(time.time() * 1000)
    output_file = os.path.join(SOUNDS_DIR, f"output_{timestamp}.wav")

    # Download audio file
    try:
        r = requests.get(audio_url)
        r.raise_for_status()
        with open(output_file, "wb") as f:
            f.write(r.content)
        print(f"✅ Speech saved to {output_file}")
    except Exception as e:
        print(f"❌ Failed to download audio: {e}")
        return

    # Auto play audio if Windows
    if platform.system() == "Windows":
        try:
            print("▶️ Playing audio...")
            play_audio_windows(output_file)
        except Exception as e:
            print(f"❌ Failed to play audio: {e}")
    else:
        print(f"ℹ️ Audio playback not supported on this OS in this script. File saved: {output_file}")

def stop_audio_playback():
    if platform.system() == "Windows":
        import winsound
        winsound.PlaySound(None, winsound.SND_PURGE)