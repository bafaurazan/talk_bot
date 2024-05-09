"""Defining controllers"""

from http import HTTPStatus

from documents.models import Document
from documents.schemas import DocumentIn, DocumentOut


def create_document_controller(payload: DocumentIn) -> tuple[HTTPStatus, DocumentOut]:
    """POST method"""
    document = Document(**payload.dict())
    document.full_clean()
    document.save()
    return HTTPStatus.CREATED, document


def list_documents_controller() -> list[DocumentOut]:
    """GET method (getting all objects from db)"""
    return Document.objects.all()


def retrieve_document_controller(id: int) -> DocumentOut:
    """GET method (getting object by id)"""
    document = Document.objects.get(id=id)
    return document


def update_document_controller(payload: DocumentIn, id: int) -> DocumentOut:
    """PUT method (changing object by id)"""
    document = Document.objects.get(id=id)
    for attr, value in payload.dict().items():
        setattr(document, attr, value)
    document.full_clean()
    document.save()
    return document


def delete_document_controller(id: int) -> HTTPStatus:
    """DELETE method (deletting object by id)"""
    document = Document.objects.get(id=id)
    document.delete()
    return HTTPStatus.OK
