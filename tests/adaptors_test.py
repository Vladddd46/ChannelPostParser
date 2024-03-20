import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from pytz import timezone
from src.entities.Channel import Channel
from src.entities.Comment import Comment
from src.entities.Post import Post
from src.entities.Reaction import Reaction
from src.entities.User import User
from src.adaptors.TelethonAdaptors import (
    convert_telethon_channel,
    convert_telethon_comment,
    convert_telethon_post,
    convert_telethon_user,
    convert_telethon_reaction,
)

class TestTelethonAdaptors(unittest.TestCase):
    def setUp(self):
        self.telethon_channel = MagicMock()
        self.telethon_channel.id = 123
        self.telethon_channel.title = "Test Channel"
        self.telethon_channel.username = "test_channel"
        self.telethon_channel.verified = False
        self.telethon_channel.scam = True
        self.telethon_channel.participants_count = 100

        self.telethon_user = MagicMock()
        self.telethon_user.id = 456
        self.telethon_user.first_name = "John"
        self.telethon_user.last_name = "Doe"
        self.telethon_user.username = "johndoe"
        self.telethon_user.premium = True
        self.telethon_user.verified = True
        self.telethon_user.scam = False

        self.telethon_comment = MagicMock()
        self.telethon_comment.id = 789
        self.telethon_comment.message = "Test Comment"
        self.telethon_comment.date = datetime(2024, 3, 20, 10, 30, 0)
        self.telethon_comment.views = 50
        self.telethon_comment.reactions.results = []

        self.telethon_post = MagicMock()
        self.telethon_post.id = 987
        self.telethon_post.message = "Test Post"
        self.telethon_post.date = datetime(2024, 3, 20, 11, 0, 0)
        self.telethon_post.views = 100
        self.telethon_post.reactions.results = []

        self.telethon_reaction = MagicMock()
        self.telethon_reaction.count = 5
        self.telethon_reaction.reaction.emoticon = "😊"

    def test_convert_telethon_channel(self):
        channel = convert_telethon_channel(self.telethon_channel)
        self.assertIsInstance(channel, Channel)
        self.assertEqual(channel.channel_id, 123)
        self.assertEqual(channel.title, "Test Channel")
        self.assertEqual(channel.user_name, "test_channel")
        self.assertEqual(channel.verified, False)
        self.assertEqual(channel.scam, True)
        self.assertEqual(channel.num_of_subscribers, 100)

    def test_convert_telethon_user(self):
        user = convert_telethon_user(self.telethon_user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.uid, 456)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.username, "johndoe")
        self.assertEqual(user.is_premium, True)
        self.assertEqual(user.is_verified, True)
        self.assertEqual(user.is_scam, False)

if __name__ == "__main__":
    unittest.main()
