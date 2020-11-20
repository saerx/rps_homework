import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):

        self.player_1 = Player("Greg", "rock")

    def test_player_has_name(self):
        self.assertEqual("Greg", self.player_1.name)

