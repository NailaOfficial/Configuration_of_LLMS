import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# 🌿 Load environment variables
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    raise EnvironmentError("GEMINI_API_KEY is missing from .env file!")

# 🧠 Initialize Gemini client and model
gemini_client = AsyncOpenAI(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

chat_model = OpenAIChatCompletionsModel(
    openai_client=gemini_client,
    model="gemini-2.0-flash"
)

# ⚙️ Set configuration for agent run
settings = RunConfig(
    model=chat_model,
    model_provider=gemini_client,
    tracing_disabled=True
)

# 🐻 Define the Animal Fun Bot for Kids
animal_bot = Agent(
    name="Animal Fun Bot 🐾",
    instructions="""
You're a cheerful animal knowledge coach for kids aged 5–10.

Teach kids fun and educational things about animals using easy language, emojis 🐶🦁🐸, and examples.

Include:
- Interesting animal facts
- Simple animal-based riddles
- Guess-the-animal games
- Encourage curiosity and praise answers!

Be playful, short, and positive in tone. One question or fact at a time.
"""
)

# 🚀 Start the interaction
start_prompt = "Say hello to the child and start with a fun animal fact!"
start_result = Runner.run_sync(
    starting_agent=animal_bot,
    run_config=settings,
    input=start_prompt
)
print(f"\n🐾 AnimalBot: {start_result.final_output}")

# 🔁 Chat loop for interaction
while True:
    reply = input("\n👧 You: ")

    if reply.lower() in ["exit", "quit", "stop"]:
        print("\n🐾 AnimalBot: Bye-bye! Keep exploring the animal kingdom! 🐘🦓")
        break

    bot_response = Runner.run_sync(
        starting_agent=animal_bot,
        run_config=settings,
        input=reply
    )
    print(f"\n🐾 AnimalBot: {bot_response.final_output}")
