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
def get_weather(city: str, info: str = "weather"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    try:
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        return {
            "result": f"The weather in {city} is {temperature}°C with {condition}"
        }

    elif info == "wind":
        return {
            "city": city,
            "wind_speed": wind_speed
        }

    elif info == "condition":
        return {
            "city": city,
            "condition": condition
        }

    else:
        # Full weather report
        return {
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "humidity": humidity,
            "wind_speed": wind_speed
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
            "error": "Could not fetch humidity data."
        }


# ---------------- FORECAST TOOL ----------------

@mcp.tool()
def get_forecast(city: str):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    try:
        forecast = data["list"][0]

        temperature = forecast["main"]["temp"]
        condition = forecast["weather"][0]["description"]

        return {
            "result": f"Forecast for {city}: {temperature}°C with {condition}"
        }

    except:
        return {
            "error": "Could not fetch forecast data."
        }


# ---------------- RUN MCP SERVER ----------------

if __name__ == "__main__":
    mcp.run()
