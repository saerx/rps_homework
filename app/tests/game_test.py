import unittest
from app.models.game import Game 
from app.models.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Greg", "rock")
        self.player_2 = Player("Chris", "paper")
        self.player_3 = Player("Plam", "scissors")
        self.player_4 = Player("Brad", "rock")
        self.player_5 = Player("Beck", "paper")
        self.player_6 = Player("Klat", "scissors")


        self.game1 = Game(self.player_1, self.player_2)
        self.game2 = Game(self.player_2, self.player_1)
        self.game3 = Game(self.player_1, self.player_3)
        self.game4 = Game(self.player_3, self.player_1)
        self.game5 = Game(self.player_2, self.player_3)
        self.game6 = Game(self.player_3, self.player_2)
        self.game7 = Game(self.player_3, self.player_6)

    def test_game_has_player1(self):
        self.assertEqual(self.game1.first_player, self.player_1)

    def test_game_has_player2(self):
        self.assertEqual(self.game1.second_player, self.player_2)

    def test_enter_the_ring_method_returns_a_list_with_both_hands(self):
        competing_hands  = self.game1.enter_the_ring()
        self.assertEqual(competing_hands, ["rock", "paper"])

    def test_find_winner_for_rock_and_paper(self):
        winning_player_1 = self.game1.find_winner()
        winning_player_2 = self.game2.find_winner()
        self.assertEqual(winning_player_1, self.player_2)
        self.assertEqual(winning_player_2, self.player_2)

    def test_find_winner_for_rock_and_scissors(self):
        winning_player_1 = self.game3.find_winner()
        winning_player_2 = self.game4.find_winner()
        self.assertEqual(winning_player_1, self.player_1)
        self.assertEqual(winning_player_2, self.player_1)
