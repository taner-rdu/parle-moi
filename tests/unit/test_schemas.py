import pytest
from pydantic import ValidationError

from parle_moi.schemas import ConversationResponse


def test_minimal_valid_response():
    response = ConversationResponse(answer="Bonjour !", detected_language="french")
    assert response.corrected_sentence is None


def test_response_with_correction():
    response = ConversationResponse(
        answer="On dit 'je vais bien', pas 'je suis bien'.",
        corrected_sentence="Je vais bien.",
        detected_language="french",
    )
    assert response.corrected_sentence == "Je vais bien."


def test_missing_required_field_raises():
    with pytest.raises(ValidationError):
        ConversationResponse(answer="Bonjour !")
