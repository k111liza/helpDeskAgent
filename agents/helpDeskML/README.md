# Helpdesk Agent (Example)

**Purpose**  
Answers attendee questions about the AI4Students 2025 conference (dates, venue, tracks, catering, etc.)
using only the official event information.

## Input format

The `run()` method expects a `dict` with:

```python
{
  "question": "What are the prerequisites for the AI Agents workshop?"
}
```

## Output format

On success (`success = True`):

```python
{
  "success": True,
  "message": "ML track information provided",
  "data": {
    "question": "<original question>",
    "answer": "<text answer>",
    "track": "ML Engineering",
  }
}
```

On error:

```python
{
  "success": False,
  "message": "Missing or empty 'question' field in request.",
  "data": None
}
```

## Example calls

1. Question: `"When is the MLOps workshop?"`  
2. Question: `"What do I need to bring for the AI Agents workshop?"`  
3. Question: `"Are there sessions about quantum computing in the ML track?"`  
   - expected: the agent should typically answer: `"I don't know based on the available information."`
