from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
import requests

@tool
def get_weather(city: str) -> str:
    """ Get the general sense of the weather for a city. """
    return f"It's always sunny in {city}."

@tool
def get_live_weather(city:str) -> str:
    """ Get the current live weather conditons of a city. """
    WEATHER_API_KEY = "XXXXXXXXXXXXXXXXX"
    WEATHER_BASE_URL = "https://api.weatherapi.com/v1/"

    response = requests.get(
        f"{WEATHER_BASE_URL}current.json?key={WEATHER_API_KEY}&q={city}"
    )

    location = response.json()['location']
    current = response.json()['current']

    return (
        f"Live weather for {location['name']}, {location['region']}, {location['country']}:\n"
        f"  Condition : {current['condition']['text']}\n"
        f"  Temp      : {current['temp_f']}°F / {current['temp_c']}°C\n"
        f"  Feels Like: {current['feelslike_f']}°F / {current['feelslike_c']}°C\n"
        f"  Humidity  : {current['humidity']}%\n"
        f"  Wind      : {current['wind_mph']} mph {current['wind_dir']}\n"
        f"  Updated   : {current['last_updated']}"
    )

tools = [get_weather, get_live_weather]
tool_map = {tool.name: tool for tool in tools}

agent = ChatOllama(
    model="llama3.2",
    # <- llama3.2 is the 'latest' or default version, with 3b parameters
    # https://ollama.com/library/llama3.2:1b
    temperature=0.1
    ).bind_tools(tools)

messages = [HumanMessage(content="Tell me what the weather is generally like in San Francisco.")]

response = agent.invoke(messages)

messages.append(response)

while response.tool_calls:
    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        tool_result = tool_map[tool_name].invoke(tool_args)

        messages.append(
            ToolMessage(content=tool_result, tool_call_id=tool_call["id"])
            )
        
        response = agent.invoke(messages)

        messages.append(response)

print(response.content)
