# Conversational Weather AI Agent using MCP + Phi3

A conversational AI weather assistant built using MCP (Model Context Protocol), Phi3 local LLM, and OpenWeather API.

This project supports:
- Tool calling
- Conversational memory
- MCP architecture
- Local LLM integration
- Weather forecasting
- Humidity checking
- Weather condition retrieval

---

# Features

- Conversational AI agent
- MCP Server + MCP Client architecture
- Local Phi3 model using Ollama
- OpenWeather API integration
- JSON-based tool calling
- Memory-enabled conversation
- Tool-result memory
- Multiple weather tools
- Secure API key handling using `.env`

---

# Tech Stack

- Python
- MCP
- Ollama
- Phi3
- OpenWeather API
- Asyncio
- Requests
- JSON
- dotenv
- Git & GitHub

---

# Project Structure

```bash
weather-ai-agent/
│
├── agent.py
├── weather.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# Available Tools

## 1. get_temperature
Returns temperature for a city.

## 2. get_humidity
Returns humidity for a city.

## 3. get_weather_condition
Returns weather condition for a city.

## 4. get_forecast
Returns forecast for a city.

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-link>
cd weather-ai-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows
```bash
.venv\Scripts\activate
```


---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama from:

https://ollama.com

---

## 5. Pull Phi3 Model

```bash
ollama pull phi3
```

---

## 6. Create `.env` File

Create a `.env` file in the root folder:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Get API key from:

https://openweathermap.org/api

---

# Run The Project

Start MCP Weather Server:

```bash
python weather.py
```

In another terminal run:

```bash
python agent.py
```

---

# Example Questions

```text
What's the temperature in Mumbai?

What's the humidity in Bangalore?

What's the weather condition in Delhi?

What's the forecast for Chennai?

What about tomorrow?
```

---

# Memory Support

This AI agent supports:
- Conversation memory
- Tool-result memory
- Context-aware follow-up questions

Example:

```text
User: What's temperature in Mumbai?
AI: 32°C

User: What about tomorrow?
AI: Forecast for Mumbai...
```

---

# Learning Outcomes

This project helped in learning:

- MCP Architecture
- AI Agents
- Tool Calling
- Conversational Memory
- API Integration
- Local LLM Usage
- Backend Development
- Git & GitHub
- Async Python

---

# Future Improvements

- Multi-tool reasoning
- FastAPI integration
- Streamlit UI
- Voice assistant
- Long-term memory
- RAG integration
- Vector databases
- Advanced AI agents

---
<img width="1300" height="796" alt="image" src="https://github.com/user-attachments/assets/70e12c28-9243-4ce1-8bd0-b8b7b686793c" />
