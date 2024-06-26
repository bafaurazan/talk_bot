"""Defining views for documents"""

from http import HTTPStatus
from django.http import HttpRequest

from ninja import Router
from ninja.pagination import LimitOffsetPagination, paginate

from documents.schemas import DocumentIn, DocumentOut
from documents.controllers import (
    create_document_controller,
    list_documents_controller,
    retrieve_document_controller,
    update_document_controller,
    delete_document_controller,
    eval_document_controller,
)


router = Router(tags=["Documents"])


@router.post("/document/", response={HTTPStatus.CREATED: DocumentOut})
def create_document(request: HttpRequest, payload: DocumentIn):
    """
    Response for POST method.
    Example: http://localhost:8000/api/document/
    """
    return create_document_controller(payload)


@router.get("/document/", response={HTTPStatus.OK: list[DocumentOut]})
@paginate(LimitOffsetPagination)
def list_documents(request: HttpRequest):
    """Response for GET method (getting all objects from db)"""
    return list_documents_controller()


@router.get("/document/{id}/", response={HTTPStatus.OK: DocumentOut})
def retrieve_document(request: HttpRequest, id: int):
    """Response for GET method (getting object by id)"""
    return retrieve_document_controller(id)


@router.put("/document/{id}/", response={HTTPStatus.OK: DocumentOut})
def update_document(request: HttpRequest, data: DocumentIn, id: int):
    """Response for PUT method (changing object by id)"""
    return update_document_controller(data, id)


@router.delete("/document/{id}/", response={HTTPStatus.OK: None})
def delete_document(request: HttpRequest, id: int):
    """Response for DELETE method (deletting object by id)"""
    return delete_document_controller(id)

@router.get("/document/{id}/eval/")
def eval_document(request: HttpRequest, id: int):
    """Response for GET method (getting object by id)"""
    return eval_document_controller(id)
