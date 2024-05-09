"""Input and output schemas for models"""

from ninja import Schema


class DocumentIn(Schema):
    """Input schema for document"""

    command: str
    request_path: str
    documentation: str


class DocumentOut(Schema):
    """Output schema for document"""

    id: int
    command: str
    request_path: str
    documentation: str
