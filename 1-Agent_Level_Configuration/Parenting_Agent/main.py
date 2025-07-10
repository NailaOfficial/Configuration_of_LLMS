import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI

# 🔐 Load API Key from .env
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    raise EnvironmentError("Missing GEMINI_API_KEY in .env file!")

# 🤖 Setup Gemini Client
gemini_client = AsyncOpenAI(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# ❌ Disable telemetry
set_tracing_disabled(True)

# 🚀 Core async loop
async def run_life_guide():
    advisor = Agent(
        name="Life Advice Guide 🌱",
        instructions="""
You are a gentle, concise life advisor.

Your job:
- Answer questions using short wisdom (max 3–5 lines)
- Share only one follow-up suggestion if needed
- Avoid complex explanations unless asked

Focus on emotional support, clarity, and encouragement 🌟
""",
        model=OpenAIChatCompletionsModel(
            openai_client=gemini_client,
            model="gemini-2.0-flash"
        )
    )

    print("🌱 Life Guide is ready! Ask anything (type 'exit' to leave):\n")

    while True:
        question = input("🧍 You: ").strip().lower()
        if question in ["exit", "quit"]:
            print("\n🌱 Life Guide: Take care, and keep growing 🌸")
            break

        answer = await Runner.run(advisor, question)
        print(f"\n🌱 Guide: {answer.final_output}\n")

# 🧠 Start async loop
if __name__ == "__main__":
    asyncio.run(run_life_guide())
