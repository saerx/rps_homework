import unittest
from app.models.game import Game 
from app.models.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Greg", "rock")
        self.player_2 = Player("Steve", "paper")

        self.game1 = Game(self.player_1, self.player_2)

    def test_game_has_player1(self):
        self.assertEqual(self.game1.first_player, self.player_1)
