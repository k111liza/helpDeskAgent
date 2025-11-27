from abc import ABC, abstractmethod
from typing import Any, Dict


class Agent(ABC):
    """
    Base class for all event agents.
    Every agent receives a JSON-like dict and returns a JSON-like dict.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Short unique name for the agent."""
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """What this agent does (1–2 sentences)."""
        raise NotImplementedError

    @abstractmethod
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main entrypoint.

        :param request: Input dictionary with agent-specific fields.
        :return: Dictionary with at least:
            - 'success': bool
            - 'message': human-readable string
            - 'data': agent-specific output (or None on error)
        """
        raise NotImplementedError
