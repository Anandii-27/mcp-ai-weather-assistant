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
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return {
            "result": f"""
Weather in {city}

Temperature : {temperature}°C
Condition   : {condition.title()}
Humidity    : {humidity}%
Wind Speed  : {wind_speed} m/s
"""
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
            "result": f"""
Humidity in {city}

Humidity : {humidity}%
"""
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
        forecast = data["list"][0]

        temperature = forecast["main"]["temp"]
        condition = forecast["weather"][0]["description"]

        return {
            "result": f"""
Forecast for {city}

Temperature : {temperature}°C
Condition   : {condition.title()}
"""
        }

    except:
        return {
            "result": "Could not fetch forecast data."
        }


# ---------------- RUN MCP SERVER ----------------

if __name__ == "__main__":
    mcp.run()
