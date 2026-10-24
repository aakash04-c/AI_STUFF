
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


context_window = []
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

