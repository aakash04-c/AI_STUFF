
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



while True:

    msg = input("you : ")

    if msg in ["bye", "exit"]:
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": msg
            }
        ]
    )
    
    print( "assistant : " + response.choices[0].message.content)

