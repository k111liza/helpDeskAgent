from typing import Any, Dict

from common.agent_base import Agent
from common.llm_wrapper import llm_call


EVENT_INFO = """
Event: AI4Students 2025
Dates: 10–12 June 2025
City: Brussels, Belgium
Venue: TechHub Conference Center, Rue des Sciences 42

Tracks:
- Track A: Intro to Machine Learning
- Track B: Generative AI for Beginners
- Track C: Robotics & AI in the Real World

Registration:
- Early bird deadline: 30 April 2025
- Regular deadline: 31 May 2025
- On-site registration: limited, card payments only

Catering:
- Vegetarian and vegan options available
- Gluten-free lunches available on request (must indicate during registration)
- Coffee breaks morning and afternoon

Social events:
- Welcome reception on 10 June, 18:30
- Poster reception on 11 June, 17:30

Contact:
- Email: info@ai4students2025.org
"""


class HelpdeskAgent(Agent):
    """Example agent: answers attendee questions about the event."""

    @property
    def name(self) -> str:
        return "helpdesk"

    @property
    def description(self) -> str:
        return "Answers attendee questions about AI4Students 2025 using official information."

    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        question = (request.get("question") or "").strip()

        if not question:
            return {
                "success": False,
                "message": "Missing or empty 'question' field in request.",
                "data": None,
            }

        system_prompt = (
            "You are the official helpdesk assistant for the AI4Students 2025 conference. "
            "Use ONLY the event information provided. "
            "If the answer is not in the information, reply exactly: "
            "'I don't know based on the available information.'"
        )

        user_prompt = f"""
Event information:
{EVENT_INFO}

User question: {question}

Answer in 1–3 short sentences:
"""

        answer = llm_call(
            prompt=user_prompt,
            system_prompt=system_prompt,
            temperature=0.2,
        )

        return {
            "success": True,
            "message": "OK",
            "data": {
                "question": question,
                "answer": answer,
            },
        }
