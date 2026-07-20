# m3mmo

A personal household Discord bot for managing appointments, groceries, reminders, and recipes. Built as a learning project exploring rule-based parsing, LLM integration, and local AI deployment.

## Features (planned)
- Appointment tracking with proactive reminders (1 week, 3 days, 1 day out)
- Grocery list with produce expiration tracking
- Daily reminders until marked complete
- Recipe storage and retrieval
- Misc general assistant

## Tech Stack
- Python 3.11+
- discord.py
- SQLite
- Anthropic Claude API (Phase 2)
- Ollama / local LLM (Phase 3)

## Setup
1. Clone the repo
2. Create and activate a virtual environment: `python -m venv venv` then `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your tokens
5. Run the bot: `python bot.py`

## Project Structure
m3mmo/
├── bot.py # entry point
├── .env # secrets (never committed)
├── .env.example # safe template
├── requirements.txt
└── database/
└── m3mmo.db
## Phases
- **Phase 1** — Rule-based parsing, no AI
- **Phase 2** — Claude API for natural language understanding
- **Phase 3** — Local LLM via Ollama for offline/air-gapped use
