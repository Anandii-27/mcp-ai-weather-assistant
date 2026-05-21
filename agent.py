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
You are an AI assistant.

Available tools:

1. get_weather
   Arguments:
   - city

   Use for CURRENT weather.

2. get_forecast
   Arguments:
   - city

   Use for TOMORROW or FUTURE weather.

3. get_humidity
   Arguments:
   - city

   Use for humidity questions.

4. calculate
   Arguments:
   - expression

   Use for math calculations.

User question:
{user_question}

IMPORTANT RULES:
- Use ONLY ONE tool
- Return ONLY ONE JSON object
- Return ONLY valid JSON
- Use EXACT argument names
- No markdown
- No explanation
- No extra text

Weather Example:

{{
    "tool": "get_weather",
    "arguments": {{
        "city": "Mumbai"
    }}
}}

Calculator Example:

{{
    "tool": "calculate",
    "arguments": {{
        "expression": "25 * 8"
    }}
}}
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