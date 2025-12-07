from typing import Any, Dict
from common.agent_base import Agent
from common.llm_wrapper import llm_call

ML_TRACK_INFO = """
DEVON 2025 - MACHINE LEARNING TRACK

TRACK LEADER: Dr. Elena Rodriguez, Head of ML Research at DeepMind

SCHEDULE (Track 1: ML Engineering):

Day 1 - June 15, 2025:
• 10:00-11:30: "Foundation Models: Beyond Transformers" - Prof. Chen
• 13:00-14:30: "MLOps in Production: Best Practices" - Sarah Johnson
• 15:00-16:30: "Fine-tuning LLMs with Limited Resources" - Workshop Part 1

Day 2 - June 16, 2025:
• 09:30-11:00: "Explainable AI for Regulatory Compliance" - Panel Discussion
• 11:30-13:00: "Vector Databases for AI Applications" - Pinecone Team
• 14:30-18:00: "Building AI Agents" - Hands-on Workshop (€149)

Day 3 - June 17, 2025:
• 10:00-12:00: "Multimodal AI: Text, Image, Audio" - OpenAI Engineers
• 13:30-15:00: "Edge AI: Deploying Models on Devices" - NVIDIA
• 15:30-17:00: "Ethical AI Frameworks" - Academic Panel

Day 4 - June 18, 2025:
• 09:00-11:00: "Generative AI for Code" - GitHub Copilot Team
• 11:30-13:00: Closing Keynote: "The Next 5 Years in ML" - Dr. Rodriguez

ML-SPECIFIC WORKSHOPS:
1. "Building AI Agents" (2-day workshop, €149)
   - Prerequisites: Python, basic ML knowledge
   - Tools: LangChain, OpenAI API, vector databases
   - Bring: Laptop with Python 3.9+ and 8GB RAM minimum

2. "MLOps Crash Course" (Free, September 16, 17:00-18:30)
   - Tools: MLflow, Docker, Kubernetes
   - For: Engineers transitioning to ML roles

TRACK REQUIREMENTS:
• Recommended background: Intermediate Python, linear algebra basics
• Code examples available on GitHub: github.com/devcon2025/ml-track
• Cloud credits provided for hands-on sessions: $100 AWS/Azure credits per attendee
• Dataset: Provided (synthetic financial data for workshops)

ML COMPETITION:
• "Predictive Maintenance Challenge" - Prize: €5000 + internship offers
• Registration deadline: September 10, 2025
• Team size: 1-3 people
• Tech stack: Any ML framework allowed

SPEAKERS (ML Track):
• Dr. Elena Rodriguez (DeepMind) - Track Chair
• Prof. Marcus Chen (Stanford) - Foundation Models
• Sarah Johnson (MLOps Lead, Docker) - Production ML
• Alex Volkov (NVIDIA) - Edge AI
• Maria Silva (OpenAI) - Multimodal AI
• Dr. Thomas Wright (MIT) - Ethical AI

RESOURCES:
• Discord channel: #ml-track-devcon2025
• Shared notebook: colab.research.google.com/devcon-ml
• Dataset download: devcon2025.tech/datasets
• Competition portal: kaggle.com/competitions/devcon2025-ml

Q&A SESSIONS:
• Daily: 12:00-12:30 (Speaker office hours)
• Mentor matching: Available for students and early-career professionals
• Code review: Sign up at registration desk

PREREQUISITES FOR WORKSHOPS:
• Python 3.9+ with pandas, numpy, scikit-learn
• Basic understanding of neural networks
• GitHub account for code collaboration
• Laptop with minimum 8GB RAM (16GB recommended for LLM workshops)

CONTACT:
• ML Track Email: ml-track@devcon2025.tech
• Track Lead Twitter: @ElenaML_DevCon
"""


class MLTrackAgent(Agent):
    """Specialized agent for Machine Learning track at DevCon 2025"""

    @property
    def name(self) -> str:
        return "ml_track_devcon2025"

    @property
    def description(self) -> str:
        return ("Answers technical questions about Machine Learning at DevCon 2025, "
                "specializes in schedules, workshops, prerequisites, and technical details.")


    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        question = (request.get("question") or "").strip()

        if not question:
            return {
                "success": False,
                "message": "Please ask a question about the ML track.",
                "data": None,
            }

        system_prompt = (
            "You are a technical specialist for the Machine Learning & AI Engineering track at DevCon 2025. "
            "You have deep expertise in ML, AI, MLOps, and related technologies. "
            "Answer questions based ONLY on the provided ML track information. "
            "Be specific about schedules, technical requirements, workshops, and prerequisites. "
            "If information is not in the provided data, say: 'This information is not available in the ML track details.' "
            "When discussing technical requirements, be precise about software versions, hardware specs, and prerequisites."
        )

        user_prompt = f"""
# MACHINE LEARNING TRACK INFORMATION
{ML_TRACK_INFO}

# USER QUESTION
{question}

Answer:
"""

        answer = llm_call(
            prompt=user_prompt,
            system_prompt=system_prompt,
            temperature=0.4
        )

        return {
            "success": True,
            "message": "OK",
            "data": {
                "question": question,
                "answer": answer,
            },
        }



