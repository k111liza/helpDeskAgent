# Helpdesk Agent (Example)

**Purpose**  
Answers attendee questions about the AI4Students 2025 conference (dates, venue, tracks, catering, etc.) using only the official event information.

## Input format

The `run()` method expects a `dict` with:

```python
{
  "question": "Where is the conference venue?"
}
```

## Output format

On success (`success = True`):

```python
{
  "success": True,
  "message": "OK",
  "data": {
    "question": "<original question>",
    "answer": "<text answer>"
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

1. Question: `"Where is the conference venue?"`  
2. Question: `"What are the conference dates?"`  
3. Question: `"Is childcare available during the event?"`  
   - expected: the agent should typically answer: `"I don't know based on the available information."`
