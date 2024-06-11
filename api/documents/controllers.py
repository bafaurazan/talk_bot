"""Defining controllers"""

import os
import subprocess
import re

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


def eval_document_controller(id: int):
    """GET method subprocess (getting object by id)
    code example:
    "emacsclient -e (with-current-buffer (window-buffer) (latex-insert-block \"center\"))"
    "C:/Program Files/Git/git-bash -c open \"C:/Program Files/Image-Line/FL Studio 20/FL64.exe\""
    """

    document = Document.objects.get(id=id)
    text = document.request_path

    part1 = re.findall(r"^\s*(.*?)\s-", text)[0]
    part2 = re.findall(r' (-(?:\w+|-))', text)[0]
    part3 = re.findall(r" -(?:\w+|-) (.*)", text)[0]

    my_command = [part1, part2, part3]
    subprocess.run(
        my_command,
        capture_output=True,
        shell=False,
        check=True,
    )

    return HTTPStatus.OK
