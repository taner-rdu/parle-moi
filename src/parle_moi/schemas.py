from pydantic import BaseModel, Field


class ConversationResponse(BaseModel):
    answer: str = Field(description="The bot's natural-language reply in French.")
    corrected_sentence: str | None = Field(
        default=None,
        description="Corrected version of the user's message if it contained a grammar mistake, else None.",
    )
    detected_language: str = Field(
        description="The language the user's message was written in, e.g. 'french' or 'english'."
    )
