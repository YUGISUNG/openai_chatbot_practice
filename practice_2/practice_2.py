from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful expert tutor."}
]

user_input = input("You: ")
messages.append({"role": "user", "content": user_input})

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.7,
    max_tokens=400
)

reply = response.choices[0].message.content.strip()
print(f"AI: {reply}")
