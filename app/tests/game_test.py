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

    def test_game_has_player2(self):
        self.assertEqual(self.game1.second_player, self.player_2)

    def test_enter_the_ring_method_returns_a_list_with_both_hands(self):
        competing_hands  = self.game1.enter_the_ring()
        self.assertEqual(competing_hands, ["rock", "paper"])
