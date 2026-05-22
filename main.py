from fastapi import FastAPI
from ollama import chat as ollama_chat

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import json


# FASTAPI APP 

app = FastAPI()


#MCP SERVER CONFIG

server_params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)


#HOME ROUTE

@app.get("/")
def home():

    return {
        "message": "AI Weather Agent Running"
    }


#CHAT ROUTE

@app.get("/chat")
async def chat(message: str):

    # Ask Phi3
    response = ollama_chat(
        model="phi3",
        messages=[
            {
                "role": "system",
                "content": """
You are a JSON-only weather assistant.

Return ONLY valid JSON.

Available tools:

1. get_temperature
Arguments:
- city

2. get_humidity
Arguments:
- city

3. get_weather_condition
Arguments:
- city

4. get_forecast
Arguments:
- city

Rules:
- temperature -> get_temperature
- humidity -> get_humidity
- weather condition -> get_weather_condition
- forecast -> get_forecast

Examples:

{
    "tool": "get_temperature",
    "arguments": {
        "city": "Bangalore"
    }
}

{
    "tool": "get_humidity",
    "arguments": {
        "city": "Mumbai"
    }
}

Return ONLY JSON.
No explanation.
No markdown.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    # AI raw output
    ai_output = response["message"]["content"].strip()

    print("\nAI Output:")
    print(ai_output)

    # Remove markdown
    ai_output = ai_output.replace("```json", "")
    ai_output = ai_output.replace("```", "")
    ai_output = ai_output.strip()

    #EXTRACT FIRST JSON OBJECT ONLY

    start = ai_output.find("{")

    brace_count = 0
    end = start

    for i in range(start, len(ai_output)):

        if ai_output[i] == "{":
            brace_count += 1

        elif ai_output[i] == "}":
            brace_count -= 1

            if brace_count == 0:
                end = i + 1
                break

    json_text = ai_output[start:end]

    #JSON PARSE

    try:
        action = json.loads(json_text)

    except Exception as e:

        return {
            "error": f"JSON Error: {str(e)}",
            "raw_output": ai_output
        }

    # Extract tool name
    tool_name = action["tool"]

    # Extract arguments
    arguments = action["arguments"]

    #MCP TOOL EXECUTION

    async with stdio_client(server_params) as streams:

        async with ClientSession(*streams) as session:

            # Initialize MCP session
            await session.initialize()

            # Call MCP tool
            result = await session.call_tool(
                tool_name,
                arguments
            )

            try:
                tool_result = result.content[0].text

            except Exception:
                tool_result = str(result)

    #FINAL RESPONSE

    return {
        "user_message": message,
        "selected_tool": tool_name,
        "arguments": arguments,
        "tool_result": tool_result
    }