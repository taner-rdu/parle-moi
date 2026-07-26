from typing import Literal

from langchain_core.language_models.chat_models import BaseChatModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    provider: Literal["anthropic", "openai"] = "anthropic"
    model_name: str = "claude-sonnet-4-5"
    temperature: float = 0.7

    anthropic_api_key: str | None = None
    openai_api_key: str | None = None


def get_chat_model(settings: Settings | None = None) -> BaseChatModel:
    settings = settings or Settings()

    if settings.provider == "anthropic":
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model_name=settings.model_name,
            temperature=settings.temperature,
            api_key=settings.anthropic_api_key,
            timeout=None,
            stop=None,
        )

    if settings.provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=settings.model_name,
            temperature=settings.temperature,
            api_key=settings.openai_api_key,
        )

    raise ValueError(f"Unknown provider: {settings.provider}")
