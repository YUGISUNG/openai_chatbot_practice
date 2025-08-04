from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant who can also respond with the current date and time when asked."}
]

print("Type 'exit' to quit.
")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if "time" in user_input.lower():
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"AI: The current time is {now}")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content.strip()
    print(f"AI: {reply}")
    messages.append({"role": "assistant", "content": reply})
