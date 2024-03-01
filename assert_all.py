#to run this file, uncomment the top part of the code in the game.py file and then run this file
#if you enter 1, this file will run your code with the input from input1.txt
# and output to output1.txt. Then you can match the file with the solution file provided.
#you can use https://www.diffchecker.com/ to compare the files.

import subprocess
n = input("Enter a single-digit test number: ")
myoutput = open("output"+n+".txt","w")
myinput = open("input"+n+".txt",encoding="ascii",errors="surrogateescape")
p1 = subprocess.check_call(['python',"proj08.py"], stdin=myinput,stdout=myoutput)
myinput.close()
myoutput.close()


student_output = open(f"output{n}.txt","r")
teacher_output = open(f"teacher_output{n}.txt","r")

student_lines = student_output.readlines()
teacher_lines = teacher_output.readlines()

student_output.close()
teacher_output.close()

for student_line, teacher_line in zip(student_lines, teacher_lines):
    if teacher_line != student_line:
        print("Error")
        print(f"Expected: {teacher_line}")
        print(f"Student's: {student_line}")
    assert student_line == teacher_line
assert len(student_lines) == len(teacher_lines)

print(f"[Test Output {n}]: [PASSED]")


