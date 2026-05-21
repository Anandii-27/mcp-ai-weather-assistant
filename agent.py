from ollama import chat
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import asyncio
import json


# ---------------- MCP SERVER CONFIG ----------------

server_params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)


# ---------------- MEMORY ----------------

messages = [
    {
        "role": "system",
        "content": """
You are a JSON-only weather assistant.

You must return ONLY valid JSON.

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

{
    "tool": "get_weather_condition",
    "arguments": {
        "city": "Delhi"
    }
}

{
    "tool": "get_forecast",
    "arguments": {
        "city": "Chennai"
    }
}

Return ONLY JSON.
No explanation.
No markdown.
"""
    }
]


# ---------------- MAIN FUNCTION ----------------

async def main():

    while True:

        # User input
        user_question = input("\nAsk something: ")

        # Exit condition
        if user_question.lower() == "quit":
            break

        # Store user message in memory
        messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        # Ask Local LLM
        response = chat(
            model='phi3',
            messages=messages
        )

        # AI raw output
        ai_output = response['message']['content'].strip()

        # Store AI response in memory
        messages.append(
            {
                "role": "assistant",
                "content": ai_output
            }
        )

        print("\nAI Output:")
        print(ai_output)

        # Remove markdown if present
        ai_output = ai_output.replace("```json", "")
        ai_output = ai_output.replace("```", "")
        ai_output = ai_output.strip()

        # Extract JSON only
        start = ai_output.find("{")
        end = ai_output.rfind("}") + 1

        json_text = ai_output[start:end]

        # Convert JSON -> Python dict
        try:
            action = json.loads(json_text)

        except Exception as e:
            print("\nJSON Error:")
            print(e)
            continue

        # Extract tool name
        tool_name = action["tool"]

        # Extract arguments
        arguments = action["arguments"]

        print("\nSelected Tool:")
        print(tool_name)

        print("\nArguments:")
        print(arguments)

        # Connect to MCP server
        async with stdio_client(server_params) as streams:

            async with ClientSession(*streams) as session:

                # Initialize MCP session
                await session.initialize()

                # Call MCP tool
                result = await session.call_tool(
                    tool_name,
                    arguments
                )

                print("\nTool Result:")

                try:
                    tool_result = result.content[0].text

                    print(tool_result)

                    # Store tool result in memory
                    messages.append(
                        {
                            "role": "assistant",
                            "content": tool_result
                        }
                    )

                except Exception:
                    print(result)


# ---------------- START PROGRAM ----------------

asyncio.run(main())