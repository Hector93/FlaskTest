import os
import tempfile

import pytest

from app import appInstance


@pytest.fixture
def app():
    return appInstance

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()




def test_redirect(client):
    """redirect from / to the first element of the list"""

    response = client.get('/')
    assert response.status == '302 FOUND'
    assert '/list/1' in str(response.data)


def test_firstPage(client):
    """get the first page of the users"""
    response = client.get('/list/1')
    assert response.status == '200 OK'
