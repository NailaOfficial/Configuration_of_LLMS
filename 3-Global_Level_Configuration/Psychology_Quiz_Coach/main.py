import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI
from agents import set_default_openai_client, set_default_openai_api, set_tracing_disabled

# 🔐 Load environment secrets
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# 🔧 Gemini API setup
client = AsyncOpenAI(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
set_default_openai_client(client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)

# 🧠 Quiz Coach Definition
quiz_bot = Agent(
    name="PsychCoachBot",
    model="gemini-2.0-flash",
    instructions="""
Act as a university-level psychology quiz coach.

Responsibilities:
- Ask one quiz question at a time (MCQ or short-answer)
- Wait for the user's answer
- Share correct response and explain briefly
- Keep a cheerful and encouraging tone 😊

Topics to quiz:
- Cognitive Biases
- Memory systems (STM, LTM)
- Conditioning theories
- Mental Health (e.g., Anxiety, Depression)
- Famous Psychologists (Freud, Bandura, Piaget, etc.)

Add emojis when helpful. Use "next" to give another question. Use "explain" to clarify the concept.
"""
)

# 🚀 Start the quiz interaction
intro_prompt = "Begin with a fun memory-related psychology question."
response = Runner.run_sync(quiz_bot, intro_prompt)
print(f"\n🧠 PsychBot: {response.final_output}")

# 🔁 Interaction Loop
while True:
    user_input = input("\n👤 You: ")

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("\n🧠 PsychBot: Thanks for playing! Keep exploring psychology! 🧠✨")
        break

    follow_up = Runner.run_sync(quiz_bot, user_input)
    print(f"\n🧠 PsychBot: {follow_up.final_output}")
