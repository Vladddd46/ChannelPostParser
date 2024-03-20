import pytest
from datetime import datetime
from src.entities.Channel import Channel
from src.entities.Post import Post
from src.entities.Comment import Comment
from src.entities.Reaction import Reaction, ReactionType
from src.entities.User import User

@pytest.fixture
def sample_channel():
    return Channel(channel_id=1, title="Test Channel", num_of_subscribers=100)

def test_constructor(sample_channel):
    assert sample_channel.channel_id == 1
    assert sample_channel.title == "Test Channel"
    assert sample_channel.num_of_subscribers == 100

def test_add_post(sample_channel):
    post1 = Post(post_id=1, datetime=datetime.now(), text="Post 1", pinned=False, views=0, reactions=[], is_reply=False, contains_media=False)
    post2 = Post(post_id=2, datetime=datetime.now(), text="Post 2", pinned=False, views=0, reactions=[], is_reply=False, contains_media=False)
    
    sample_channel.add_post(post1)
    assert len(sample_channel.posts) == 1
    assert sample_channel.posts[0] == post1

    sample_channel.add_post(post2)
    assert len(sample_channel.posts) == 2
    assert sample_channel.posts[1] == post2

def test_num_of_subscribers(sample_channel):
    sample_channel.num_of_subscribers = 200
    assert sample_channel.num_of_subscribers == 200

def test_channel_id(sample_channel):
    sample_channel.channel_id = 10
    assert sample_channel.channel_id == 10

def test_title(sample_channel):
    sample_channel.title = "New Title"
    assert sample_channel.title == "New Title"

def test_verified(sample_channel):
    sample_channel.verified = True
    assert sample_channel.verified is True

def test_scam(sample_channel):
    sample_channel.scam = True
    assert sample_channel.scam is True

def test_user_name(sample_channel):
    sample_channel.user_name = "new_username"
    assert sample_channel.user_name == "new_username"

def test_to_json(sample_channel):
    post1 = Post(post_id=1, datetime=datetime.now(), text="Post 1", pinned=False, views=0, reactions=[], is_reply=False, contains_media=False)
    post2 = Post(post_id=2, datetime=datetime.now(), text="Post 2", pinned=False, views=0, reactions=[], is_reply=False, contains_media=False)
    sample_channel.add_post(post1)
    sample_channel.add_post(post2)

    expected_json = {
        "subscribers": 100,
        "id": 1,
        "title": "Test Channel",
        "posts": [
            {"post_id": 1, "datetime": post1.datetime, "text": "Post 1", "pinned": False, "views": 0, "reactions": [], "is_reply": False, "media_in_post": False, "comments": []},
            {"post_id": 2, "datetime": post2.datetime, "text": "Post 2", "pinned": False, "views": 0, "reactions": [], "is_reply": False, "media_in_post": False, "comments": []}
        ]
    }
    assert sample_channel.to_json() == expected_json
