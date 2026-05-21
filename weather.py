from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

#LOAD ENV VARIABLES 

load_dotenv()

#CREATE MCP SERVER

mcp = FastMCP("Weather Server")

# API KEY 

API_KEY = os.getenv("OPENWEATHER_API_KEY")


#TEMPERATURE TOOL 

@mcp.tool()
def get_temperature(city: str):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    try:
        temperature = data["main"]["temp"]

        return {
            "result": f"The temperature in {city} is {temperature}°C"
        }

    except:
        return {
            "error": "Could not fetch temperature data."
        }


# HUMIDITY TOOL

@mcp.tool()
def get_humidity(city: str):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

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


#WEATHER CONDITION TOOL

@mcp.tool()
def get_weather_condition(city: str):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    try:
        condition = data["weather"][0]["description"]

        return {
            "result": f"The weather in {city} is {condition}"
        }

    except:
        return {
            "error": "Could not fetch weather condition."
        }


#FORECAST TOOL

@mcp.tool()
def get_forecast(city: str):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

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


#RUN MCP SERVER 

if __name__ == "__main__":
    mcp.run()
