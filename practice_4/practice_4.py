from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful expert tutor."}
]

print("💬 Type your question or message below.")
print("📎 Type 'exit' to quit or 'reset' to start a new conversation.\n")

model_name = "gpt-4"

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Ending conversation. See you next time!")
        break
    elif user_input.lower() == "reset":
        messages = [{"role": "system", "content": "You are a helpful expert tutor."}]
        print("🔄 Conversation reset.\n")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    reply = response.choices[0].message.content.strip()
    print(f"AI: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
