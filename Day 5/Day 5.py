import time
import re
# Runtime: 

# Intro here

# Question 1:
# https://adventofcode.com/2022/day/5
# A crane moves boxes according to the instructions, the crane can carry 1 box at a time.
# What box ends up atop of each column?
# example data
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# This is for timing run time
start_time = time.time()

# Need variables for:
# - Pile to take from
# - Pile to add to
# - Number of crates to take (iterate or order reverse)

# Read the file into a variable
my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

# Splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

#print(data_into_list)
my_file.close()

# print(data_into_list)

# First build an image of the dock. 9 lists, 8 elements long.

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []

col = [col1,col2,col3,col4,col5,col6,col7,col8,col9]

width = len(data_into_list[0])
i = 3
n = 0
#print(width) # 35
#-- This put each row into a list.
# while n < 8:
#     while i <= width:
#         col[n].append(data_into_list[n][i-3:i])
#         i = i+4
#     i=3
#     n += 1

# This puts each column into a list.
while n < 8:
    col1.append(data_into_list[n][i-3:i])
    i = i+4
    col2.append(data_into_list[n][i-3:i])
    i = i+4
    col3.append(data_into_list[n][i-3:i])
    i = i+4
    col4.append(data_into_list[n][i-3:i])
    i = i+4
    col5.append(data_into_list[n][i-3:i])
    i = i+4
    col6.append(data_into_list[n][i-3:i])
    i = i+4
    col7.append(data_into_list[n][i-3:i])
    i = i+4
    col8.append(data_into_list[n][i-3:i])
    i = i+4
    col9.append(data_into_list[n][i-3:i])
    i = i+4
    i=3
    n += 1

# Need 3 lists in a list
Num = []
MoveFrom = []
MoveTo = []

# Need to extract the numbers from the instructions
list_end = len(data_into_list)
Instructions_list = data_into_list[10:list_end]

Instructions_numeric = []
i = 0
# This extracts the numbers from a string as a list (3x1)
while i < len(Instructions_list):
    Instructions_numeric.append([int(s) for s in Instructions_list[i].split() if s.isdigit()])
    i += 1

# [int(s) for s in Instructions_list.split() if s.isdigit()]

# Restructure such that each column is a list of ints, not each row.
i = 0
while i < len(Instructions_numeric): 
    Num.append(Instructions_numeric[i][0])
    MoveFrom.append(Instructions_numeric[i][1]-1) # -1 to change from col# to index#
    MoveTo.append(Instructions_numeric[i][2]-1) # ^^
    i += 1

instructions = [Num, MoveFrom, MoveTo]

#print(instructions)

#print(Instructions_numeric)

# delete column entries of triple space, so that the map has the top
# of each column at index 0.

# while i < len(col):
#     col[i] = (value for value in col[i] if value != '   ')
#     i += 1
# col = [col1,col2,col3,col4,col5,col6,col7,col8,col9]
# for c in col:
#     (value for value in col if value != '   ')

col1 = list((value for value in col1 if value != '   '))
col2 = list((value for value in col2 if value != '   '))
col3 = list((value for value in col3 if value != '   '))
col4 = list((value for value in col4 if value != '   '))
col5 = list((value for value in col5 if value != '   '))
col6 = list((value for value in col6 if value != '   '))
col7 = list((value for value in col7 if value != '   '))
col8 = list((value for value in col8 if value != '   '))
col9 = list((value for value in col9 if value != '   '))

col = [col1,col2,col3,col4,col5,col6,col7,col8,col9]

#print(col)

i = 0
n = 0
while i < len(Instructions_list):
    num_val = instructions[0][i]
    print(num_val)
    MoveFrom_val = instructions[1][i]
    print(MoveFrom_val)
    MoveTo_val = instructions[2][i]
    print(MoveTo_val)
    while n < num_val:
        print(col[MoveTo_val])
        print(col[MoveFrom_val][0])
        #col[MoveTo] = col[MoveFrom][0].append(col[MoveTo])
        col[MoveTo_val] = col[MoveTo_val].insert(0,col[MoveFrom_val][0])
        print(col[MoveTo_val])
        del col[MoveFrom_val][0]
        n += 1
    i += 1
    n = 0
# issue is that col[move_To_Val] is becoming blank/empty on line 170 (insert).
# ALSO! The loop doesn't break, just stops after outputting 'print(col[MoveFrom_val][0])'.
# Actually it apears to continue running despite the error.

# print(col[2])

# # print(Instructions_numeric)
# i = 0
# n = 0
# while i < len(Instructions_list):
#     num = Instructions_numeric[i][0]
#     MoveFrom = Instructions_numeric[i][1]
#     MoveTo = Instructions_numeric[i][2]
#     while n < num:
#         col[MoveTo] = col[MoveFrom][0].append(col[MoveTo])
#         del col[MoveFrom][0]
#         n += 1
#     i += 1
#     n = 0




#print([int(s) for s in Instructions_list[i].split() if s.isdigit()])



# answer  = ''
# answer2 = ''

# print('Answer to part 1:', answer)
# print('Answer to part 2:', answer2)

# print("--- %s seconds ---" % (time.time() - start_time))