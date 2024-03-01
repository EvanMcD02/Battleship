from board import Ship

#horizontal
teacher_length=5
teacher_orientation="h"
teacher_coordinate=(0,0)
teacher_positions = [(0,0), (0,1), (0,2), (0,3), (0,4)]

student_ship = Ship(teacher_length, teacher_coordinate, teacher_orientation)

assert teacher_length == student_ship.length
assert teacher_orientation == student_ship.orientation
assert teacher_positions == student_ship.get_positions()

teacher_hit_count = 5
teacher_ship_sunk = True
for i in range(5):
    student_ship.apply_hit()

assert teacher_hit_count == student_ship.hit_count
assert teacher_ship_sunk == student_ship.is_sunk

#vertical
teacher_length = 5
teacher_orientation = "v"
teacher_coordinate = (0, 0)
teacher_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]

student_ship = Ship(teacher_length, teacher_coordinate, teacher_orientation)

assert teacher_length == student_ship.length
assert teacher_orientation == student_ship.orientation
assert teacher_positions == student_ship.get_positions()

teacher_hit_count = 5
teacher_ship_sunk = True
for i in range(5):
    student_ship.apply_hit()

assert teacher_hit_count == student_ship.hit_count
assert teacher_ship_sunk == student_ship.is_sunk


#horizontal not sunk
teacher_length = 4
teacher_orientation = "h"
teacher_coordinate = (0, 1)
teacher_positions = [(0, 1), (0, 2), (0, 3), (0, 4)]

student_ship = Ship(teacher_length, teacher_coordinate, teacher_orientation)

assert teacher_length == student_ship.length
assert teacher_orientation == student_ship.orientation
assert teacher_positions == student_ship.get_positions()

teacher_hit_count = 3
teacher_ship_sunk = False
for i in range(3):
    student_ship.apply_hit()

assert teacher_hit_count == student_ship.hit_count
assert teacher_ship_sunk == student_ship.is_sunk
