 Agent-Level Configuration Kya Hai?
 -----------------------------------

Jab tum aik agent (jaise aik parenting chatbot) banati ho kisi LLM (Large Language Model) se, toh us agent ka khaas behavior, style aur tools tum khud set karti ho.Is process ko kehte hain:👉 Agent-level configuration(Yani sirf usi agent ke liye settings lagana)

✅ Agent-Level Pe Kya Kya Configure Hota Hai?
1. Agent ka naam

name = "Parenting Assistant Agent"
Jaise tumhara agent aik parenting expert banay.

2. Instructions / System Message

"You are a helpful parenting assistant. Give short, practical advice."

Yeh agent ko batata hai ke wo kaise behave kare.
Jaise: short jawab do, friendly tone mein baat karo, etc.

3. LLM Model

model = OpenAIChatCompletionsModel(model="gpt-4")
Har agent apna alag model use kar sakta hai. Ek GPT-4, doosra Gemini ya Claude.

4. Tools

tools = [WeatherTool(), EmotionAnalysisTool()]
Agar agent ko kisi kaam ke tools chahiyein (jaise weather check karna, emotion samajhna), woh bhi add kar sakti ho.

5. Output Style
Jaise tum chahti ho:

Sirf bullet points mein jawab do

2 lines se zyada na likho

JSON format mein reply do etc

🧠 Easy Example:

agent = Agent(
    name="Parenting Bot",
    model=gpt_4_model,
    instructions="Give advice in 3 lines only.",
    tools=[EmotionTool()]
)
Yeh agent sirf 3 line ka jawab dega, GPT-4 use karega aur emotions detect kar sakta hai.

🔍 Kyu Zaroori Hai?
Agar tum multiple agents chala rahi ho (jaise ek doctor, ek teacher, ek parent guide), toh har ek ka alag configuration hoga — warna sab ek jaise behave karenge.