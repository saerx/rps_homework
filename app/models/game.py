class Game(): 
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player


    def enter_the_ring(self):
        competing_hands = []
        competing_hands.append(self.first_player.hand)
        competing_hands.append(self.second_player.hand)
        return competing_hands

    def find_winner(self):
        competing_hands = self.enter_the_ring()
        winning_player = None
        if competing_hands[0] == "rock" and competing_hands[1] == "paper":
            winning_player = self.second_player
        elif competing_hands[1] == "rock" and competing_hands[0] == "paper":
            winning_player = self.first_player

        elif competing_hands[0] == "scissors" and competing_hands[1] == "rock":
            winning_player = self.second_player
        elif competing_hands[1] == "scissors" and competing_hands[0] == "rock":
            winning_player = self.first_player

        elif competing_hands[0] == "paper" and competing_hands[1] == "scissors":
            winning_player = self.second_player
        elif competing_hands[1] == "paper" and competing_hands[0] == "scissors":
            winning_player = self.first_player
            
        return winning_player
