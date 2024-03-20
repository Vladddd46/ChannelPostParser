import pytest
from datetime import datetime
from src.entities.Post import Post
from src.entities.Comment import Comment
from src.entities.Reaction import Reaction


@pytest.fixture
def sample_post():
    datetime_now = datetime.now()
    reactions = [Reaction(1, "😊"), Reaction(2, "😢")]
    comments = [Comment(1, "Great post!", datetime_now, None, reactions, 10, False, False)]
    return Post(1, datetime_now, "This is a sample post.", False, 100, reactions, False, False, comments)


def test_post_attributes(sample_post):
    assert sample_post.post_id == 1
    assert sample_post.datetime.date() == datetime.now().date()  # Check date only, time may vary
    assert sample_post.text == "This is a sample post."
    assert sample_post.pinned == False
    assert sample_post.views == 100
    assert len(sample_post.reactions) == 2
    assert sample_post.is_reply == False
    assert sample_post.contains_media == False
    assert len(sample_post.comments) == 1


def test_add_comment(sample_post):
    initial_comments_count = len(sample_post.comments)
    new_comment = Comment(2, "Another comment", datetime.now(), None, [], 5, False, False)
    sample_post.add_comment(new_comment)
    assert len(sample_post.comments) == initial_comments_count + 1
    assert sample_post.comments[-1] == new_comment

def test_equality(sample_post):
    post1 = sample_post
    post2 = Post(1, datetime.now(), "This is a sample post.", False, 100, [], False, False)
    assert post1 == post2
    assert hash(post1) == hash(post2)
