import pytest
from datetime import datetime
from src.entities.Comment import Comment
from src.entities.Reaction import Reaction, ReactionType
from src.entities.User import User

@pytest.fixture
def sample_comment():
    user = User(uid=1, username="test_user", first_name="John", last_name="Doe")
    reaction1 = Reaction(count=10, emoticon="👍", is_custom=False)
    reaction2 = Reaction(count=5, emoticon="❤️", is_custom=False)
    return Comment(m_id=1, text="Test comment", datetime=datetime.now(), from_user=user, reactions=[reaction1, reaction2], views=20, is_reply=False, contains_media=False)

def test_constructor(sample_comment):
    assert sample_comment.text == "Test comment"
    assert sample_comment.from_user.username == "test_user"
    assert sample_comment.reactions[0].emoticon == "👍"
    assert sample_comment.reactions[1].emoticon == "❤️"
    assert sample_comment.views == 20

def test_contains_media(sample_comment):
    sample_comment.contains_media = True
    assert sample_comment.contains_media is True

def test_is_reply(sample_comment):
    sample_comment.is_reply = True
    assert sample_comment.is_reply is True

def test_m_id(sample_comment):
    sample_comment.m_id = 10
    assert sample_comment.m_id == 10

def test_datetime(sample_comment):
    now = datetime.now()
    sample_comment.datetime = now
    assert sample_comment.datetime == now

def test_from_user(sample_comment):
    new_user = User(uid=2, username="new_user", first_name="Jane", last_name="Doe")
    sample_comment.from_user = new_user
    assert sample_comment.from_user.username == "new_user"

def test_reactions(sample_comment):
    reaction3 = Reaction(count=8, emoticon="😄", is_custom=False)
    sample_comment.reactions.append(reaction3)
    assert len(sample_comment.reactions) == 3
    assert sample_comment.reactions[2] == reaction3

def test_views(sample_comment):
    sample_comment.views = 30
    assert sample_comment.views == 30
