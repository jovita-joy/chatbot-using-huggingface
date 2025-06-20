# interface.py
from model_loader import load_model
from chat_memory import ChatMemory
import torch

def run_chat():
    print("=" * 50)
    print("🤖 Local CLI Chatbot (Hugging Face Model)".center(50))
    print("=" * 50)

    tokenizer, model = load_model()
    memory = ChatMemory(max_turns=5)

    print("Type your message. Type /exit to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        context = memory.get_context()
        prompt = context + f"\nQuestion: {user_input}\nAnswer:" if context else f"Answer the following question:\nQuestion: {user_input}\nAnswer:"



        input_ids = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True).input_ids

        outputs = model.generate(
            input_ids,
            max_new_tokens=100,
            do_sample=False
        )

        bot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True).split("Answer:")[-1].strip()
        memory.add_turn(user_input, bot_reply)
        print(f"Bot: {bot_reply}\n")


if __name__ == "__main__":
    run_chat()
