class Game(): 
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player


    def enter_the_ring(self):
        competing_hands = []
        competing_hands.append(self.first_player.hand)
        competing_hands.append(self.second_player.hand)
        return competing_hands

    # def winning_game(self):
    #     winning_player = None
    #     competing_hands = []
