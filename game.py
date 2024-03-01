from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str

class Player(object):
    """
        The Player class represents a single player of battleship.
        The Player class will be responsible for storing and updating each player’s data, placing ships during Part One
        of the game, and for reading their guesses during each turn of the game (Part Two).
    """
    def __init__(self, name, board, ship_list):
        """
            This method creates a Player object. You must provide a name, a board object, and a ship_list in this order
        as parameters. You must define the following attributes (remember to use self) The name is a str ("Player 1" or "Player 2")
        board represents the board object belonging to the current player, guesses will be
        a list of coordinates that the player has guessed, and ship_list will be a list of integers representing the
        length of each ship that the player has not yet placed on the board.
        """
        self.name = name  # a str ("Player 1" or "Player 2")
        self.board = board  # the board object belonging to the current player
        self.guesses = []  # a list of coordinates that the player has guessed
        self.ship_list = ship_list  # a list of integers representing the length of each ship that the player has not yet placed on the board

    def validate_guess(self, guess):
        """
            This method takes a guess tuple and checks if it is valid. A valid guess is one that has not already been
            guessed by the Player, and is an existing location on the board. If the guess is invalid, raise
            exceptions
        """
        try:
            if guess in self.guesses:  #  if the guess has already been guessed
                raise RuntimeError("This guess has already been made!")
            elif guess[0] < 0 or guess[0] >= self.board.size or guess[1] < 0 or guess[1] >= self.board.size:  #  if the guess is out of bounds
                raise RuntimeError("Guess is not a valid location!")
            else:
                self.board.apply_guess(guess)  #  apply the guess to the board
        except RuntimeError as error:  #  if there is an error
            print(error)  #  print the error

    def get_player_guess(self):
        """
            This method will read a guess from the user using the following string: "Enter your guess: ". The guess will
            be in the format "row, col" (ex: "3, 2"). After obtaining the guess from the user, this method should check
            if the guess is valid (which method checks that a guess is valid?). If the guess is invalid, re-prompt the user
            until they have entered a valid guess. If the guess is valid, return the guess as a tuple (hint: the returned tuple
            will have two int values).
        """
        player_guess = input("Enter your guess: ")  #  get the player's guess
        while True:  #  while the guess is invalid
            try:
                player_guess = player_guess.split(',')  # split the player's guess
                player_guess = (int(player_guess[0]), int(player_guess[1]))  # convert the player's guess to a tuple
                self.validate_guess(player_guess)  #  validate the guess. If this fails it will except a RuntimeError
                break  #  break out of the loop
            except RuntimeError:  #  if there is an error
                player_guess = input("Enter your guess: ")  #  get the player's guess
                continue  #  continue the loop
        return player_guess  #  return the player's guess

    def set_all_ships(self):
        ''' This function will place all ships for the player. For each ship size in ship_list this function will
        get ship coordinates from the user, get ship orientation from the user, create a Ship object, and make sure
        it is valid. If the ship is valid, it will be placed on the board. If the ship is invalid, it will reprompt the user until
        all ships have been placed. User input will be the following strings: "Enter the coordinates of the ship of size {}: "
        "Enter the orientation of the ship of size {}: "
        '''
        for ship_size in self.ship_list:  #  for each ship size in the ship list
            while True:  #  while the ship is invalid
                try:
                    ship_coordinates = input("Enter the coordinates of the ship of size {}: ".format(ship_size))  #  get the ship's coordinates
                    ship_coordinates = ship_coordinates.split(',')  #  split the ship's coordinates
                    ship_coordinates = (int(ship_coordinates[0]), int(ship_coordinates[1]))  #  convert the ship's coordinates to a tuple
                    ship_orientation = input("Enter the orientation of the ship of size {}: ".format(ship_size))  #  get the ship's orientation
                    ship = Ship(ship_size, ship_coordinates, ship_orientation)  #  create a ship object
                    self.board.validate_ship_coordinates(ship)  #  validate the ship's coordinates. If this fails it will except a RuntimeError
                    self.board.place_ship(ship)  #  place the ship on the board
                    break  #  break out of the loop
                except RuntimeError as e:
                    print(e)
                    continue  #  continue the loop


class BattleshipGame(object):
    """
        The BattleshipGame class is responsible for running the game, keeping track of turns, and checking if a player
        has won.
    """

    def __init__(self, player1, player2):
        """
            This method creates a BattleshipGame object. The BattleshipGame class is initialized with two players.
        """
        self.player1 = player1  #  the first player
        self.player2 = player2  #  the second player

    def check_game_over(self):
        """
            This method checks if the game has ended (i.e. all ships belonging to a player have been sunk). If the game is
            over, return the name of the winning player. Otherwise, return "".
        """
        player1_ship_count = 0  #  initialize the ship count to 0
        player2_ship_count = 0  #  initialize the ship count to 0
        #  check player 1's board to see if are no S's left
        for row in self.player1.board.board:  #  for each row in player 1's board
            for column in row:  #  for each column in the row
                if column == 'S':  #  if there is an S
                    player1_ship_count += 1  #  increment the ship count
        if player1_ship_count == 0:  #  if there are no S's
            return self.player1.name  #  return player 2's name
        for row in self.player2.board.board:  #  for each row in player 2's board
            for column in row:  #  for each column in the row
                if column == 'S':  #  if there is an S
                    player2_ship_count += 1  #  increment the ship count
        if player2_ship_count == 0:  #  if there are no S's
            return self.player2.name  #  return player 1's name
        return ""  #  return an empty string


    def display(self):
        """
            This method displays the current state of the game. It should display the name of the current player,
            and the current board of the current player.
        """
        print("Player 1's board:")
        print(self.player1.board)  #  print player 1's board
        print("Player 2's board:")
        print(self.player2.board)  #  print player 2's board

    def play(self):
        """
            This method will run the entire game until one of the players has won (similar to a main function in previous
            projects). Specifically, this method will do the following (remember to use self):
            1. (Part One) Each player will place their ships on the board. Each player will have their own board.
            2. (Part Two) Then, players will start try to start sinking each other's ship. The game should go until someone ends.
            If a shit is hit, print "Hit!"
            After each player has made a guess, ask if they want to continue playing. If they enter q the game ends, otherwise keep playing.
        """
        self.player1.set_all_ships()  #  player 1 sets all of their ships
        self.player2.set_all_ships()  #  player 2 sets all of their ships
        while True:  #  while the game is not over
            self.display()  #  display the game
            print("{}'s turn.".format(self.player1.name))  #  print player 1's turn
            player1_guess = self.player1.get_player_guess()  #  get player 1's guess
            self.player1.guesses.append(player1_guess)  #  add player 1's guess to their list of guesses
            for ship in self.player2.board.ships:  #  for each ship in player 2's board's ships
                if player1_guess in ship.get_positions():  #  if player 1's guess is in the ship's positions
                    ship.apply_hit()  #  apply a hit to the ship
            if self.check_game_over() != "":  #  if the game is over
                print("{} wins!".format(self.check_game_over()))  #  print the winner
                break  #  break out of the loop
            print("{}'s turn.".format(self.player2.name))  #  print player 2's turn
            player2_guess = self.player2.get_player_guess()  #  get player 2's guess
            self.player2.guesses.append(player2_guess)  #  add player 2's guess to their list of guesses
            for ship in self.player1.board.ships:  #  for each ship in player 1's board's ships
                if player2_guess in ship.get_positions():  #  if player 2's guess is in the ship's positions
                    ship.apply_hit()  #  apply a hit to the ship
            if self.check_game_over() != "":  #  if the game is over
                print("{} wins!".format(self.check_game_over()))  #  print the winner
                break  #  break out of the loop
            continue_playing = input("Continue playing?: ")  #  ask the user if they want to continue playing
            if continue_playing == 'q':  #  if the user wants to quit
                break  #  break out of the loop
            else:  #  if the user wants to continue playing
                continue  #  continue the loop