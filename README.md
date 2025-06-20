# chatbot-using-huggingface
# 🤖 Local CLI Chatbot with Hugging Face Transformers

This project implements a **command-line chatbot** using Hugging Face's `transformers` library and a lightweight model (`google/flan-t5-small`) for local, context-aware conversations.

---

## 📦 Requirements

- Python 3.8+
- [transformers](https://pypi.org/project/transformers/)
- [torch](https://pypi.org/project/torch/)

Install with:
```bash
pip install transformers torch
```

## Project Structure
```sh
chatbot/
├── main.py              # Entry point to start chatbot
├── chatbot.py           # Chat logic with model and context handling
├── memory.py            # Manages sliding window memory
```
## Setup Instructions
Install Dependencies
```sh
pip install transformers torch
```
Run the Chatbot
```sh
python main.py
```
## Features
Uses flan-t5-small — a fine-tuned T5 model for factual instruction-following.

Maintains a short-term memory of the last 3–5 exchanges using a sliding window.

Clean and modular codebase:

model_loader.py — Loads model/tokenizer.

chat_memory.py — Maintains dialogue history.

main.py — Runs CLI loop and inference.

## Customization
You can swap flan-t5-small with any other Seq2Seq model from Hugging Face (e.g., t5-small, flan-t5-base) in model_loader.py.

Extend chat_memory.py to add logging or longer-term memory.

## OUTPUT
![Image](https://github.com/user-attachments/assets/a69e6be9-0969-494b-8af8-446d972cc40d)
