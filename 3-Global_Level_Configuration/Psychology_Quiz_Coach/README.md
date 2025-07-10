🔍 Global Level LLM Configuration kya hoti hai?
------------------------------------------------

Global level LLM ka matlab hai ke aap poore project mein aik hi dafa LLM client set karte ho, aur phir har agent ya runner mein dobara config pass karne ki zarurat nahi hoti.

📌 Asan Alfaaz Mein:
🔸	Run Level Configuration	                                     Global Level Configuration
-------------------------------------------------------------------------------------------------
Har agent ke sath RunConfig pass karni hoti hai     	        Sirf aik dafa top pe config set karni hoti hai
Bar bar LLM aur model batana padta hai	                        Aik hi dafa set ho jata hai sab agents ke liye
Har run ke sath model=... and RunConfig(...)	                Sirf Agent(..., model=...) aur Runner.run_sync(...)

✅ Global LLM Configuration kab use hoti hai?
----------------------------------------------
💡 Jab aap:
OpenAI ke models use kar rahe ho
(e.g. gpt-3.5-turbo, gpt-4)

Same LLM config bar bar reuse karna chahte ho

Sirf set_default_openai_client(...) aur set_default_openai_api(...) se config set karna chahte ho

📘 Example:
from agents import set_default_openai_client, AsyncOpenAI

# 👇 Sirf aik dafa LLM set karo
set_default_openai_client(
  AsyncOpenAI(api_key="sk-...", base_url="https://api.openai.com/v1")
)
Phir aap agents is tarah bana saktay ho:

agent = Agent(
  name="Maths Agent",
  instructions="You are a maths tutor for kids",
  model="gpt-3.5-turbo"  # ✅ sirf model ka naam do
)

result = Runner.run_sync(agent, "Start")
✅ Koi RunConfig ki zarurat nahi.

❌ Kab Global Level LLM kaam nahi karti?
Jab aap OpenAI ke ilawa koi aur model use kar rahe ho:

❌ Gemini (Google) → AIza...

❌ Claude (Anthropic)

❌ Mistral / Cohere

In models ke liye aapko RunConfig zaruri hoti hai.

🔁 Summary
Feature	Global Level
LLM setup	                Sirf aik dafa
Supported models	        ✅ OpenAI models
Not supported	            ❌ Gemini, Claude
Repeat code	                ❌ Nahin hota
RunConfig required	        ❌ Nahin
