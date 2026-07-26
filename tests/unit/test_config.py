import pytest
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

from parle_moi.config import Settings, get_chat_model


def test_defaults_to_anthropic():
    settings = Settings(_env_file=None)
    assert settings.provider == "anthropic"


def test_get_chat_model_returns_chat_anthropic():
    settings = Settings(_env_file=None, provider="anthropic", anthropic_api_key="test-key")
    model = get_chat_model(settings)
    assert isinstance(model, ChatAnthropic)


def test_get_chat_model_returns_chat_openai():
    settings = Settings(_env_file=None, provider="openai", openai_api_key="test-key")
    model = get_chat_model(settings)
    assert isinstance(model, ChatOpenAI)


def test_get_chat_model_rejects_unknown_provider():
    settings = Settings(_env_file=None, anthropic_api_key="test-key")
    settings.provider = "mistral"  # bypass Literal validation to test the guard
    with pytest.raises(ValueError):
        get_chat_model(settings)
