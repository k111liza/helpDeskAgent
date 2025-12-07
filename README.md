# Event Agents Skeleton

This repository is a **skeleton** for the *Event Management AI Agents* project.

Students: **fork or clone** this repository and then add your own agent under `agents/`.

## Structure

```text
event-agents-skeleton/
│
├─ common/
│   ├─ agent_base.py        # Agent interface/base class
│   ├─ llm_wrapper.py       # Minimal LLM helper (OpenAI)
│   └─ __init__.py
│
├─ agents/
│   ├─ __init__.py
│   ├─ helpdesk/
│   │   ├─ agent.py         # Example agent
│   │   └─ README.md
│   └─ helpDeskML/
│       ├─ agent.py         # My agent
│       └─ README.md
│
├─ orchestrator/
│   ├─ coordinator.py       # Simple dispatcher to test agents
│   └─ __init__.py
│
├─ .env             
├─ requirements.txt
└─ README.md
```

## Setup

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file from `.env.example` and set your OpenAI API key:

```bash
cp .env.example .env
# then edit .env and put your key:
# OPENAI_API_KEY=sk-...
```

## Quick test

Run the simple coordinator to test the example **helpdesk agent**:

```bash
python -m orchestrator.coordinator
```

You should see a JSON-like response with an answer about the conference venue.

## Adding Your Own Agent

1. Create a new folder under `agents/`, e.g.:

```text
agents/
  my_cool_agent/
    agent.py
    README.md
```

2. In `agent.py`, create a class extending `common.Agent` and implement:

- `name` (property)
- `description` (property)
- `run(self, request: dict) -> dict`

3. Register your agent in `orchestrator/coordinator.py` (add an import + entry in `AGENTS`).

4. Add usage examples in your `README.md` and push to GitHub.
