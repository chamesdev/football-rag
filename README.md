# Football RAG Chatbot

Short description of what this project does.

## What it does

RAG chatbot that answers questions about football statistics (Premier League, Champions League, La Liga — 2025/26 season) using real data, not guesses.

## Tech Stack

- Data source: API-Football
- Vector DB:
- Embedding model:
- LLM:
- Language: Python

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
API_FOOTBALL_KEY=your_key_here
```

## Usage

```bash
python main.py
```

## Project Structure

```
football-rag/
├── data/           # raw + processed data
├── src/            # source code
├── .env
├── requirements.txt
└── README.md
```

## Status

In progress — learning project for RAG.

## Notes