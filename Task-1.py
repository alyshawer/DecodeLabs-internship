# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training Kit - 2026
# ============================================

# --- KNOWLEDGE BASE (Dictionary) ---
# The professional approach: O(1) lookup speed
responses = {
    "hello":        "Hey there! I'm DecoBot. How can I assist you today?",
    "hi":           "Hi! Great to see you. What's on your mind?",
    "hey":          "Hey! I'm online and ready. What do you need?",
    "how are you":  "I'm running at 100% efficiency. Thanks for asking!",
    "what is ai":   "AI is the simulation of human intelligence by machines using logic, data, and learning.",
    "what can you do": "I can answer basic questions using rule-based logic. Ask me anything!",
    "who made you": "I was built by an AI Engineering intern at DecodeLabs as part of Project 1.",
    "bye":          "Goodbye! It was great chatting with you.",
    "thanks":       "You're welcome! Let me know if you need anything else.",
    "help":         "Try asking: 'hello', 'what is ai', 'how are you', or type 'exit' to quit.",
}

# --- STARTUP MESSAGE ---
print("=" * 50)
print("        DecoBot — Rule-Based AI Chatbot")
print("         DecodeLabs | Batch 2026")
print("=" * 50)
print("Type 'exit' to quit.\n")

# --- MAIN LOOP (The Heartbeat) ---
while True:

    # PHASE 1: INPUT & SANITIZATION
    raw_input_text = input("You: ")
    clean_input = raw_input_text.lower().strip()

    # EXIT STRATEGY (Kill Command)
    if clean_input == "exit":
        print("DecoBot: Session terminated. Goodbye!")
        break

    # Skip empty input
    if clean_input == "":
        print("DecoBot: Please type something!")
        continue

    # PHASE 2 & 3: PROCESS & OUTPUT
    # .get() handles lookup + fallback in one atomic operation
    reply = responses.get(clean_input, "I don't understand that yet. Type 'help' to see what I can do.")

    print(f"DecoBot: {reply}\n")