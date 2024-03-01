'''CSE Project 8: Battleship
    Algorithm
    PHASE 1 Place ships:
        prompt user for coordinates
        prompt user for direction
        reprompt if invalid
        alternate between players 1 and 2
    PHASE 2:
    prompt user to guess coordinates
    reprompt if invalid
    alternate between players 1 and 2
    display board every cycle
    display winner once all ships are destroyed
'''
from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project





def main():
    ''' . The main method should initialize each player’s Board, each Player object, and then the BattleshipGame object.
        Finally, run the game.'''
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]
    player1 = Player("Player 1", Board(board_size), ship_list)
    player2 = Player("Player 2", Board(board_size), ship_list)
    game = BattleshipGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()