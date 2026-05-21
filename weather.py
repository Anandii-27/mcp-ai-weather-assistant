from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create MCP server
mcp = FastMCP("Weather Server")

# API Key
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# ---------------- WEATHER TOOL ----------------

@mcp.tool()
def get_weather(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    try:
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        return {
            "result": f"The weather in {city} is {temperature}°C with {condition}"
        }

    except:
        return {
            "result": "Could not fetch weather data."
        }


# ---------------- HUMIDITY TOOL ----------------

@mcp.tool()
def get_humidity(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    try:
        humidity = data["main"]["humidity"]

        return {
            "result": f"The humidity in {city} is {humidity}%"
        }

    except:
        return {
            "result": "Could not fetch humidity data."
        }


# ---------------- FORECAST TOOL ----------------

@mcp.tool()
def get_forecast(city: str):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    try:
        tomorrow = data["list"][0]

        temperature = tomorrow["main"]["temp"]

        condition = tomorrow["weather"][0]["description"]

        return {
            "result": f"Forecast for {city}: {temperature}°C with {condition}"
        }

    except:
        return {
            "result": "Could not fetch forecast data."
        }
# Run MCP server
if __name__ == "__main__":
    mcp.run()