# Conversational Weather AI Agent using MCP + Phi3

A conversational AI weather assistant built using **MCP (Model Context Protocol)**, **Phi3 local LLM**, **FastAPI**, and **OpenWeather API**.

This project demonstrates how to build a real AI agent with:

- Tool calling
- Conversational memory
- MCP architecture
- Local LLM integration
- FastAPI backend APIs
- Browser-accessible AI endpoints

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
- FastAPI backend integration
- REST API endpoints
- Browser-accessible AI agent

---

# Tech Stack

- Python
- MCP
- Ollama
- Phi3
- OpenWeather API
- FastAPI
- Uvicorn
- Asyncio
- Requests
- JSON
- dotenv
- Git & GitHub

---

# Project Structure

```txt
weather-ai-agent/
│
├── agent.py
├── weather.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# Available Tools

## 1. get_temperature

Returns temperature for a city.

---

## 2. get_humidity

Returns humidity for a city.

---

## 3. get_weather_condition

Returns weather condition for a city.

---

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

```txt
https://ollama.com
```

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

```txt
https://openweathermap.org/api
```

---

# Run The Project

## Start MCP Weather Server

```bash
python weather.py
```

---

## Run AI Agent

In another terminal:

```bash
python agent.py
```

---

# FastAPI Backend Server

Run FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Open in Browser

### Home Route

```txt
http://127.0.0.1:8000
```

---

### Chat Endpoint Example

```txt
http://127.0.0.1:8000/chat?message=temperature in Bangalore
```

---

# Example Questions

```txt
What's the temperature in Mumbai?
```

```txt
What's the humidity in Bangalore?
```

```txt
What's the weather condition in Delhi?
```

```txt
What's the forecast for Chennai?
```

```txt
What about tomorrow?
```

---

# Memory Support

This AI agent supports:

- Conversation memory
- Tool-result memory
- Context-aware follow-up questions

---

# Example Conversation

```txt
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
- FastAPI backend development
- AI API server creation
- REST APIs
- Backend architecture
- Async Python
- Git & GitHub

---

# Future Improvements

- Multi-tool reasoning
- Streamlit UI
- Voice assistant
- Long-term memory
- RAG integration
- Vector databases
- Advanced AI agents
- Frontend integration
- Deployment to cloud platforms

---

# Project Status

Completed features:

- MCP server
- MCP client
- AI agent
- Local LLM integration
- Tool calling
- Conversational memory
- FastAPI backend
- Browser-accessible AI APIs
- Weather API integration

---

# Author

Built as a learning project for understanding:

- AI Agents
- MCP
- FastAPI
- Backend Development
- Local LLM systems
- Tool-based AI architecture

---
<img width="1292" height="783" alt="image" src="https://github.com/user-attachments/assets/48681ff7-7df8-439f-a7b1-b6992f53a709" />
<img width="1306" height="783" alt="image" src="https://github.com/user-attachments/assets/b653f1e3-717a-4bdf-a13e-99ca36cd2cd9" />
<img width="1919" height="585" alt="image" src="https://github.com/user-attachments/assets/0456e835-fa90-43e3-bc46-b859075e81ac" />

