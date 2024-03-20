import pytest
from src.entities.User import User


@pytest.fixture
def sample_user():
    return User(1, "john_doe", "John", "Doe", True, True, False)


def test_user_attributes(sample_user):
    assert sample_user.uid == 1
    assert sample_user.username == "john_doe"
    assert sample_user.first_name == "John"
    assert sample_user.last_name == "Doe"
    assert sample_user.is_premium == True
    assert sample_user.is_verified == True
    assert sample_user.is_scam == False


def test_to_json(sample_user):
    user_json = sample_user.to_json()
    assert user_json["uid"] == 1
    assert user_json["username"] == "john_doe"
    assert user_json["first_name"] == "John"
    assert user_json["last_name"] == "Doe"
    assert user_json["is_premium"] == True
    assert user_json["is_verified"] == True
    assert user_json["is_scam"] == False


def test_equality(sample_user):
    user1 = sample_user
    user2 = User(1, "john_doe", "John", "Doe", True, True, False)
    assert user1 == user2
    assert hash(user1) == hash(user2)


def test_attribute_changes(sample_user):
    sample_user.username = "jane_doe"
    sample_user.is_verified = False
    assert sample_user.username == "jane_doe"
    assert sample_user.is_verified == False
