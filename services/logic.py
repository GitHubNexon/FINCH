import json
import os
from services.api import send_message

CONVO_FILE = os.path.join(os.path.dirname(__file__), "conversation.json")

def load_conversation():
    if os.path.exists(CONVO_FILE):
        with open(CONVO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_conversation(conversation):
    with open(CONVO_FILE, "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=2, ensure_ascii=False)

def add_message(role, content):
    conversation = load_conversation()
    conversation.append({"role": role, "content": content})
    save_conversation(conversation)

def clear_conversation():
    save_conversation([])

def chat_with_memory(user_input):
    conversation = load_conversation()
    # Create prompt including history
    history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
    prompt = f"{history}\nUser: {user_input}\nAssistant:"
    response = send_message(prompt)
    add_message("User", user_input)
    add_message("Assistant", response)
    return response
