from __future__ import annotations

from enum import Enum


class LLMBackend(str, Enum):
    """Supported LLM backends for agent summarization."""

    CLAUDE = "claude"
    CODEX  = "codex"
    GEMINI = "gemini"
