from typing import Optional, List, Dict, Any

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env if present
load_dotenv()

# Instantiate OpenAI client (requires OPENAI_API_KEY in environment)
client = OpenAI()


def llm_call(
    prompt: str,
    model: str = "gpt-4o-mini",
    system_prompt: Optional[str] = None,
    temperature: float = 0.2,
) -> str:
    """
    Minimal helper to call an OpenAI chat model.
    Returns the response content as a string.

    Parameters
    ----------
    prompt: str
        The user content (question/instruction).
    model: str
        The OpenAI model name (default: gpt-4o-mini).
    system_prompt: Optional[str]
        Optional system-level instruction (role).
    temperature: float
        Sampling temperature (0.0–1.0). Lower = more deterministic.
    """

    messages: List[Dict[str, Any]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()
