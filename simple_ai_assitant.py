
from openai import OpenAI
from dotenv import load_dotenv
from tools import TOOLS, FUNCTION_NAME_TO_FUNCTION_MAP
import os
import json

load_dotenv()

MAX_STEP = 10

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

context_window = [
    {
        "role": "system",
        "content": """
You are a friendly, intelligent AI assistant with a chill personality.

- Keep responses short, clear, and useful.
- Answer directly without unnecessary explanations.
- Use simple, natural language.
- Add subtle humor occasionally, never force jokes.
- Keep positive vibes without being overly cheerful.
- Use emojis sparingly.
- For coding questions, provide correct code with brief explanations.
- When fixing code, preserve the user's structure and make minimal changes.
- Give detailed explanations only when requested or necessary.
- Be honest when unsure.
- Use conversation history to understand the user.
- Avoid repeating information unnecessarily.

Personality: smart friend, relaxed, slightly funny, and helpful.
Humor level: 5/10.

Be useful, not unnecessarily wordy.
"""
    }
]

while True:
    msg = input("You: ")

    if msg.lower() in ["bye", "exit", "quit"]:
        break

    context_window.append({
        "role": "user",
        "content": msg
    })

    # Chained tool calling
    for STEP in range(MAX_STEP):

        # Call the LLM
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=context_window,
            tools=TOOLS
        )

        res = response.choices[0].message

        # No more tool calls: the model has a final response
        if not res.tool_calls:
            break

        context_window.append(res)

        for tool_call in res.tool_calls:
            function_name = tool_call.function.name

            try:
                function_args = json.loads(
                    tool_call.function.arguments or "{}"
                )

                fn = FUNCTION_NAME_TO_FUNCTION_MAP[function_name]
                result = fn(**function_args)

            except Exception as e:
                result = f"Error while running {function_name}: {e}"

            context_window.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

    else:
        print("Maximum steps reached. Please try again.")
        continue

    # Store and print the final response
    assistant_msg = res.content or ""

    context_window.append({
        "role": "assistant",
        "content": assistant_msg
    })

    print("Assistant:", assistant_msg)
