
from openai import OpenAI

client = OpenAI(
    # Ollama is running here
    base_url="http://127.0.0.1:11434/v1",
    # Ollama doesn't require a real API key
    api_key="dummy_key"
)

response = client.chat.completions.create(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Hello LLM!"
        }
    ]
)

# print(response)
print(response.choices[0].message.content)
