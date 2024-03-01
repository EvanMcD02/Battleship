class Ship(object):
    """
        add your Class header here.
    """
    def __init__(self, length, position, orientation):
        """
            length: int
            position: tuple (y, x) for some reason...
            orientation: str (v or h)
        """
        self.length = length
        self.orientation = orientation
        self.position = position
        self.positions = []

        if self.orientation == 'h':  #  if the orientation is horizontal
            for i in range(self.length):  #  for each part of the ship
                self.positions.append((self.position[0], self.position[1] + i))  #  append the position to the list of positions
        else:  #  if the orientation is vertical
            for i in range(self.length):  #  for each position in the ship
                self.positions.append((self.position[0] + i, self.position[1]))  #  append the position to the list of positions

        self.hit_count = 0
        self.is_sunk = False

    def get_positions(self):
        """
            add your method header here.
        """
        return self.positions

    def get_orientation(self):
        """
            add your method header here.
        """
        return self.orientation

    def apply_hit(self):
        """
            The apply_hit function increases the hit_count by 1 and checks if the ship is sunk (all positions are hit). If
            it is sunk, then you should update the is_sunk attribute. The only parameter to use is self.
        """
        self.hit_count += 1
        if self.hit_count == self.length:  #  if the hit count is equal to the length of the ship
            self.is_sunk = True


class Board(object):
    """
        add your Class header here.
    """
    def __init__(self, size):
        """
            size (an int) will define the size of the board (size x size)
            board will be a list of lists of strings, where each list will have size number of empty spaces ' '. There will be a total of size lists.
            ships will represent the ships on the board. It will start off as an empty list.
        """
        self.size = size  # an int that defines the size of the board (size x size)
        self.board = []  #  initialize the board to an empty list
        for i in range(self.size):  #  run a loop that runs size times
            self.board.append([" "] * self.size)  #  append a list of size ' 's to the board
        self.ships = []  #  initialize the ships list to an empty list

    def place_ship(self, ship):
        """
            This function takes as a parameter Ship object (in addition to self) and updates the ships list. Additionally,
            this updates the board variable with the character "S" for each location occupied by the ship (hint: what
            function from the Ship class can help get a list of a ship’s positions?). You may assume the ship has already
            been validated to be placed onto the board.
        """
        self.ships.append(ship)  #  append the ship to the list of ships
        for position in ship.get_positions():  #  for each position in the ship's positions
            self.board[position[0]][position[1]] = 'S'  #  set the position on the board to 'S'

    def apply_guess(self, guess):
        """
            This function takes as a parameter a tuple guess with two integers (row, column) of a player guess (in addition
to self). Assume the guess has already been validated.
        """
        if self.board[guess[0]][guess[1]] == 'S':  #  if the guess is a hit
            self.board[guess[0]][guess[1]] = 'H'  #  set the guess on the board to 'H'
            print("Hit!")
            for ship in self.ships:  #  for each ship in the list of ships
                if guess in ship.get_positions():  #  if the guess is in the ship's positions
                    ship.apply_hit()  #  apply a hit to the ship
        else:  #  if the guess is a miss
            self.board[guess[0]][guess[1]] = 'M'  #  set the guess on the board to 'M'
            print("Miss!")

    def validate_ship_coordinates(self, ship):
        """
            This method takes as a parameter a Ship object (in addition to self) and checks if it can be placed on the
            current board. Raise runtime errors if the ship is out of bounds or overlaps with another ship.
        """
        for position in ship.get_positions():  #  for each part of this ship
            if position[0] < 0 or position[0] >= self.size or position[1] < 0 or position[1] >= self.size: #  if the position is out of bounds
                raise RuntimeError('Ship coordinates are out of bounds!')
            for other_ship in self.ships:  #  for each other ship in the list of ships
                if position in other_ship.get_positions():  #  if the position is in the other ship's positions
                    raise RuntimeError('Ship coordinates are already taken!')
        #  except RuntimeError as e:
            #  print(e)

    def __str__(self):
        """
            Return the current board as a string. Specifically, each line in the returned string
            will be one row in the current board. For each element in the row, place the character between "[]".
        """
        board_str = ''
        for row in self.board:  #  for each row in the board
            for element in row:  #  for each element in the row
                board_str += '[' + element + ']'  #  add the element to the board string
            board_str += '\n'  #  add a new line to the board string
        return board_str
