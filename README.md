# Multi-Agent Housing Assistant 🏠

A multi-agent AI system that helps users find housing resources 
through a coordinated pipeline of specialized agents.

## Overview
This system uses three specialized agents that work together 
to understand a user's housing needs, search available resources, 
rank them by relevance, and deliver personalized recommendations.

## Architecture
```
User Request
     ↓
Scout Agent → searches housing resources
     ↓
Analyst Agent → evaluates and ranks results
     ↓
Advisor Agent → formulates final recommendation
     ↓
User Response
```

## Agents
- **Scout Agent** — Searches and retrieves relevant housing 
  resources based on the user's request
- **Analyst Agent** — Evaluates, filters, and ranks resources 
  by relevance and suitability
- **Advisor Agent** — Generates a clear, personalized 
  recommendation for the user

## Tech Stack
- Python
- LangChain
- OpenAI API
- dotenv

## Getting Started
```bash
# Clone the repository
git clone <https://github.com/neginaatai/-Multi-Agent-Housing-Assistant.git>

# Install dependencies
pip install -r requirements.txt

# Add your API key to .env
OPENAI_API_KEY=your_key_here

# Run the assistant
python main.py
```

## Example
```
Input:  "I need emergency housing assistance"

Output: Personalized housing recommendations 
        ranked by relevance to your situation
```

## Project Structure
```
├── main.py              # Entry point and orchestrator
├── data_loader.py       # Loads and processes housing data
├── agents/
│   ├── scout.py         # Scout Agent
│   ├── analyst.py       # Analyst Agent
│   └── advisor.py       # Advisor Agent
└── .env                 # API keys
```
