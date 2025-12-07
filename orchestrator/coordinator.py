from typing import Dict, Any

from agents.helpdesk.agent import HelpdeskAgent
from agents.helpDeskML.agent import MLTrackAgent

# Register agents here
AGENTS = {
    "helpdesk": HelpdeskAgent(),
    # Add your own agents, e.g.:
    # "my_agent": MyAgent(),
    "ml_track": MLTrackAgent(),

}


def dispatch(agent_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Dispatch a request to a registered agent by name."""
    agent = AGENTS.get(agent_name)
    if not agent:
        return {
            "success": False,
            "message": f"Unknown agent '{agent_name}'",
            "data": None,
        }
    return agent.run(payload)


if __name__ == "__main__":
    # Simple manual test of the helpdesk agent
    example_request = {"question": "Where is the conference venue?"}
    response = dispatch("helpdesk", example_request)
    print(response)

    ml_request = {"question": "When is the MLOps workshop?"}
    ml_response = dispatch("ml_track", ml_request)
    print("\nML Track Agent test:")
    print(ml_response)
