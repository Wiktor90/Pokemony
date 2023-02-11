import pytest

from app import app
from utils import NoSuccessApiCode


@pytest.fixture
def payload_with_moves():
    return {"moves": [
      {"move": {"name": "pound"}},
      {"move": {"name": "smash"}},
      {"move": {"name": "blaze"}},
    ]}


@pytest.fixture
def payload_with_no_moves():
    return {"moves": []}


@pytest.fixture
def serialized_moves():
    return [{"move_name": "blaze"}, {"move_name": "pound"}]


@pytest.fixture
def app_client():
    app.config.update({
        "TESTING": True,
    })
    client = app.test_client()

    yield client


@pytest.fixture
def no_success_response_exception():
    status = 404
    text = "some error msg"
    return NoSuccessApiCode(status, text)
