import pytest
from file3 import Database


@pytest.fixture()
def db():
    database = Database()
    yield database
    database.data.clear()


def test_add_user(db):
    db.add_user(1, "Pitt")
    assert db.get_user(1) == "Pitt"


def test_add_duplicate_user(db):
    db.add_user(1, "Pitt")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Pitt")


def test_delete_user(db):
    db.add_user(1, "Pitt")
    db.delete_user(1)
    assert db.get_user(1) is None

