from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import asyncio


server_params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)


async def main():

    async with stdio_client(server_params) as streams:
        async with ClientSession(*streams) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available tools:")
            print(tools)

            result = await session.call_tool(
                "get_weather",
                {"city": "Bangalore"}
            )

            print("\nTool Result:")
            print(result)


asyncio.run(main())