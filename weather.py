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

    if response.status_code != 200:
        return {"error": data.get("message", "Something went wrong")}

    # Extract values
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    # Return based on requested info
    if info == "temperature":
        return {
            "city": city,
            "temperature": temperature
        }

    elif info == "humidity":
        return {
            "city": city,
            "humidity": humidity
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
            "city": city,
            "humidity": humidity
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
            "city": city,
            "temperature": temperature,
            "condition": condition.title()
        }

    except:
        return {
            "error": "Could not fetch forecast data."
        }


# ---------------- RUN MCP SERVER ----------------

if __name__ == "__main__":
    mcp.run()