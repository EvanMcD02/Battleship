from board import Board, Ship
from game import Player

student_board = Board(10)
student_ship = Ship(5, (0,0), "h")
student_player = Player("Player 1", student_board, [5, 4, 3, 3, 2])
student_player.board.place_ship(student_ship)
try:
    student_player.validate_guess((0,0))
    assert True
except RuntimeError as e:
    assert False

try:
    student_player.validate_guess((10,5))
except RuntimeError as e:
    assert str(e) == "Guess is not a valid location!"
    
student_player.guesses = [(0,0), (0,1), (0,2), (0,3), (0,4)]
try:
    student_player.validate_guess((0,0))
except RuntimeError as e:
    assert str(e) == "This guess has already been made!"
