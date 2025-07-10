🧠 Run Level Configuration (LLM other than OpenAI) kya hota hai?
-----------------------------------------------------------------

Jab aap kisi bhi Large Language Model (LLM) — jaise Gemini, Mistral, Anthropic Claude — ko use kar rahe ho OpenAI ke ilawa,
aur aap har ek run (yaani ek conversation/session) ke liye alag se configuration set karti ho,
toh usay hum Run Level Configuration kehte hain.

🔧 Iska matlab:
----------------
Har dafa jab agent run hota hai, aap ek naya RunConfig pass karti ho.

Is RunConfig mein:
------------------
kaunsa model use hoga (gemini, claude, etc)

kaunsa API key/client

kuch optional settings (like temperature, top_p, etc)

💻 Example:
------------

config = RunConfig(
    model=mera_custom_model,  # Gemini ya Claude ka model yahan hoga
    model_provider=external_client,  # Yeh Gemini ya Claude ka client hai
    tracing_disabled=True
)
Fir aap yeh config pass karti ho jab aap agent ko run karti ho:

aisay:-

Runner.run_sync(
    starting_agent=mera_agent,
    run_config=config,
    input="Hello! Can you teach me something?"
)
📌 Yani Summary:
-----------------

RunConfig               Har dafa ka agent run kaisay behave karega yeh batata hai
model           	    Aap Gemini, Mistral, ya Claude ka LLM set karti ho
model_provider     	    Us model ka client ya API connector
tracing_disabled	    Kya logs save hon ya nahi



