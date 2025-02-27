import pytest
from file2 import UserManager


@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("pitt", "pitt@gmail.com") == True
    assert user_manager.get_user("pitt") == "pitt@gmail.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("pitt", "pitt@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("pitt", "another@gmail.com")
