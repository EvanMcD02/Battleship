from board import Board, Ship

teacher_board_size = 10
teacher_ship = Ship(5, (0,0), "h")
student_board = Board(teacher_board_size)
student_board.place_ship(teacher_ship)

teacher_board_after_place_ship = [['S', 'S', 'S', 'S', 'S', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
assert teacher_board_after_place_ship == student_board.board
teacher_board_str="""\
[S][S][S][S][S][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
"""
student_board_str = str(student_board)
assert teacher_board_str == student_board_str

teacher_bad_ship = Ship(5, (0,0), "h")
try:
    student_board.validate_ship_coordinates(teacher_bad_ship)
except RuntimeError as e:
    assert str(e) == "Ship coordinates are already taken!"

teacher_bad_ship = Ship(5, (0, 0), "v")
try:
    student_board.validate_ship_coordinates(teacher_bad_ship)
except RuntimeError as e:
    assert str(e) == "Ship coordinates are already taken!"

teacher_bad_ship = Ship(5, (100,0), "h")
try:
    student_board.validate_ship_coordinates(teacher_bad_ship)
except RuntimeError as e:
    assert str(e) == "Ship coordinates are out of bounds!"

student_board.apply_guess((0,0))
student_board.apply_guess((0,5))
teacher_board_after_place_ship = [['H', 'S', 'S', 'S', 'S', 'M', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
assert teacher_board_after_place_ship == student_board.board