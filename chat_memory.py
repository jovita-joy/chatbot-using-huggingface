# chat_memory.py
class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []

    def add_turn(self, user_input, bot_response):
        self.history.append((user_input, bot_response))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return "\n".join([f"Question: {u}\nAnswer: {b}" for u, b in self.history])
