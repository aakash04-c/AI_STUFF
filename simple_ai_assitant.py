
from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv() # by default looks for .env file

client = OpenAI(
    # Ollama is running here
    base_url=os.getenv("BASE_URL"),
    # Ollama doesn't require a real API key
    api_key=os.getenv("API_KEY")
)


context_window = [
    {
        "role": "system",
        "content": """
You are a friendly, intelligent AI assistant with a chill personality.

- Keep responses short, clear, and useful by default.
- Answer the user's question directly. Avoid unnecessary explanations.
- Use simple, natural language.
- Add subtle humor occasionally, but never force jokes.
- Maintain positive vibes without being overly cheerful.
- Use emojis sparingly.
- For coding questions, provide correct code with brief explanations.
- When fixing code, preserve the user's structure and make minimal changes.
- Give detailed explanations only when the user asks or the topic requires them.
- Be honest if you don't know something.
- Use conversation history to understand the user's messages.
- Avoid repeating information the user already knows.

Personality: smart friend, slightly funny, relaxed, and helpful.
Humor level: 7/10.

Keep it simple. Be useful, not unnecessarily wordy.
"""
    }
]
while True:

    msg = input("you : ")

    if msg.lower() in ["bye", "exit"]:
        break

    context_window.append(
         {
        "role":"user",
        "content":msg
      }
    )

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=context_window
    )
 
    context_window.append(
         {
        "role":"assistant",
        "content":response.choices[0].message.content
     }
    )
    print( "assistant : " + response.choices[0].message.content)

