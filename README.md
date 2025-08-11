
# CLI Chatbot with Memory using Replicate API

This is a command-line chatbot leveraging [Replicate.com](https://replicate.com/) to run the `openai/gpt-4o-mini` language model with persistent conversation memory and speech synthesis.

---

## Features

- Persistent conversation saved in JSON files
- Start, end, and control chat sessions with commands
- Auto and manual text-to-speech (TTS) playback
- Speech audio saved to `./services/sounds`
- Commands to stop speech and clear audio files
- Easily configurable via `.env` file

---

## Setup Instructions (Windows PowerShell)

### 1. Clone or download this repository

```powershell
git clone https://github.com/your-username/my-chatbot.git
cd my-chatbot
```

### 2. Create `.env` file

Create a `.env` file in the project root directory with the following content:

```env
REPLICATE_API_TOKEN=your_replicate_api_token_here
MODEL_NAME=openai/gpt-4o-mini
```

You can get your Replicate API token here: [https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)

### 3. Create Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate Virtual Environment

```powershell
.env\Scripts\Activate
```

### 5. Install Required Packages

```powershell
pip install -r requirements.txt
```

### 6. Run the Chatbot

```powershell
python chat.py
```

---

## Chat Commands

| Command  | Description                               |
| -------- | --------------------------------------- |
| `/start` | Start a new conversation session        |
| `/end`   | End the current conversation and clear memory |
| `/stop`  | Stop speech playback                     |
| `/clear` | Clear saved audio files from sounds folder |

---

## Notes

- Conversations are stored in JSON files to allow persistent memory between sessions.
- Speech audio files are stored in `./services/sounds`. Use `/clear` command to remove them.
- Ensure your `.env` file is properly configured before running the chatbot.

---


