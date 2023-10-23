import os
import pytest

from fastapi.testclient import TestClient

from ca_app import (
    database,
    main,
    models,
)


@pytest.fixture
def client():
    models.Base.metadata.drop_all(bind=database.engine)
    models.Base.metadata.create_all(bind=database.engine)
    with TestClient(main.app) as client:
        yield client
