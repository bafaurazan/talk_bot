from ninja import Schema


class DocumentIn(Schema):
    command: str
    request_path: str
    documentation: str


class DocumentOut(Schema):
    id: int
    command: str
    request_path: str
    documentation: str
