"""Configuration for {{Component Name}}."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the component."""

    environment: str = "local"
