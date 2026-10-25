
from datetime import datetime
import requests as req

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_city_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    res = req.get(url, timeout=10)
    res.raise_for_status()
    return res.text


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Return the current date and time as a formatted string.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_city_weather",
            "description": "Return the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City to get the weather for"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_current_time": get_current_time,
    "get_city_weather": get_city_weather
}
