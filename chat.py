import os
import glob
import platform
from services.logic import chat_with_memory, clear_conversation
from services.speech import text_to_speech, stop_audio_playback

SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "services", "sounds")
last_ai_message = None

def delete_all_sounds():
    if os.path.exists(SOUNDS_DIR):
        files = glob.glob(os.path.join(SOUNDS_DIR, "*.wav"))
        for f in files:
            try:
                os.remove(f)
            except Exception as e:
                print(f"⚠️ Could not delete {f}: {e}")

def main():
    global last_ai_message
    print("🤖 Chatbot CLI (type /start to begin, /end to quit, /speak to generate speech, /speak-stop to stop speech, /audio-clear to clear sounds)")
    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "/start":
            clear_conversation()
            last_ai_message = None
            print("✅ Conversation started. Chat away!")
            continue

        elif user_input.lower() == "/end":
            clear_conversation()
            delete_all_sounds()
            last_ai_message = None
            print("👋 Conversation ended and memory cleared. All speech files deleted.")
            break

        elif user_input.lower() == "/speak":
            if last_ai_message:
                text_to_speech(last_ai_message)
            else:
                print("⚠ No AI message to speak.")
            continue

        elif user_input.lower() == "/speak-stop":
            if platform.system() == "Windows":
                stop_audio_playback()
                print("🛑 Speech playback stopped.")
            else:
                print("ℹ️ /speak-stop currently supported only on Windows.")
            continue

        elif user_input.lower() == "/audio-clear":
            delete_all_sounds()
            print("🗑️ All audio files deleted from ./sounds, conversation memory intact.")
            continue

        elif not user_input:
            continue

        else:
            response = chat_with_memory(user_input)
            last_ai_message = response
            print(f"Assistant: {response}")

            # Auto /speak after response
            text_to_speech(response)

if __name__ == "__main__":
    main()
