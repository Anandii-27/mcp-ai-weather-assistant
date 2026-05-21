from ollama import chat
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import asyncio
import json


#MCP SERVER CONFIGURATION

server_params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)


#MEMORY CODE

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


#MAIN FUNCTION

async def main():

    while True:

        user_question = input("\nAsk something: ")

        if user_question.lower() == "quit":
            break

        messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        response = chat(
            model='phi3',
            messages=messages
        )

        ai_output = response['message']['content'].strip()

        messages.append(
            {
                "role": "assistant",
                "content": ai_output
            }
        )

        print("\nAI Output:")
        print(ai_output)

        
        ai_output = ai_output.replace("```json", "")
        ai_output = ai_output.replace("```", "")
        ai_output = ai_output.strip()

        
        start = ai_output.find("{")
        end = ai_output.rfind("}") + 1

        json_text = ai_output[start:end]

        
        try:
            action = json.loads(json_text)

        except Exception as e:
            print("\nJSON Error:")
            print(e)
            continue

        
        tool_name = action["tool"]

        
        arguments = action["arguments"]

        print("\nSelected Tool:")
        print(tool_name)

        print("\nArguments:")
        print(arguments)

        
        async with stdio_client(server_params) as streams:

            async with ClientSession(*streams) as session:

               
                await session.initialize()

                
                result = await session.call_tool(
                    tool_name,
                    arguments
                )

                print("\nTool Result:")

                try:
                    tool_result = result.content[0].text

                    print(tool_result)

                    
                    messages.append(
                        {
                            "role": "assistant",
                            "content": tool_result
                        }
                    )

                except Exception:
                    print(result)


#START PROGRAM

asyncio.run(main())
