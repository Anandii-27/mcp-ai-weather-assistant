from ollama import chat
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import asyncio
import json


# MCP Server Configuration
server_params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)


async def main():

    # User question
    user_question = input("Ask something: ")

    # Prompt for AI
    prompt = f"""
You are an AI weather assistant.

Available tool:

1. get_weather
   Arguments:
   - city
   - info

info can be:
- temperature
- humidity
- wind
- condition
- weather

Rules:
- If user asks temperature, use info="temperature"
- If user asks humidity, use info="humidity"
- If user asks wind, use info="wind"
- If user asks weather, use info="weather"
- If user asks condition, use info="condition"

Return ONLY valid JSON.
No markdown.
No explanation.
No extra text.

Examples:

User: What's temperature in Bangalore?

{{
    "tool": "get_weather",
    "arguments": {{
        "city": "Bangalore",
        "info": "temperature"
    }}
}}

User: What's humidity in Mumbai?

{{
    "tool": "get_weather",
    "arguments": {{
        "city": "Mumbai",
        "info": "humidity"
    }}
}}

User: What's weather in Delhi?

{{
    "tool": "get_weather",
    "arguments": {{
        "city": "Delhi",
        "info": "weather"
    }}
}}

User question:
{user_question}
"""

    # Ask local LLM
    response = chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    # Raw AI output
    ai_output = response['message']['content'].strip()

    print("\nAI Output:")
    print(ai_output)

    # Remove markdown formatting
    ai_output = ai_output.replace("```json", "")
    ai_output = ai_output.replace("```", "")
    ai_output = ai_output.strip()

    # Extract ONLY JSON part
    start = ai_output.find("{")
    end = ai_output.rfind("}") + 1

    json_text = ai_output[start:end]

    # Convert JSON string → Python dictionary
    try:
        action = json.loads(json_text)

    except Exception as e:
        print("\nJSON Error:")
        print(e)
        return

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

            # Initialize session
            await session.initialize()

            # Execute tool
            result = await session.call_tool(
                tool_name,
                arguments
            )

            print("\nTool Result:")

            try:
                print(result.content[0].text)

            except:
                print(result)


# Start agent
asyncio.run(main())