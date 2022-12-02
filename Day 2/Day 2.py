import time
# Runtime: --- 0.016997814178466797 seconds ---

# Left value is opponent, right value is me.
# A = X = Rock
# B = Y = Paper
# C = Z = Siccors

# Points wise per round, you get:
#  0 for a loss
#  3 for a draw
#  6 for a win
#  1 for playing rock
#  2 for playing paper
#  3 for playing siccors

# Question 1: What is my total score if I follow the guide exactly?

# This is for timing run time
start_time = time.time()


my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

# Splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

# print(data_into_list)

my_file.close()

NumberList = [w.replace('A X', '4') for w in data_into_list]
NumberList = [w.replace('A Y', '8') for w in NumberList]
NumberList = [w.replace('A Z', '3') for w in NumberList]
NumberList = [w.replace('B X', '1') for w in NumberList]
NumberList = [w.replace('B Y', '5') for w in NumberList]
NumberList = [w.replace('B Z', '9') for w in NumberList]
NumberList = [w.replace('C X', '7') for w in NumberList]
NumberList = [w.replace('C Y', '2') for w in NumberList]
NumberList = [w.replace('C Z', '6') for w in NumberList]

answer = sum([int(x) for x in NumberList])

# Question 2:
# A,B,C retain their meaing.
# X,Y,Z now mean lose, draw, win, respectively.
# What is the score by following the guide?

NumberList2 = [w.replace('A X', '3') for w in data_into_list]
NumberList2 = [w.replace('A Y', '4') for w in NumberList2]
NumberList2 = [w.replace('A Z', '8') for w in NumberList2]
NumberList2 = [w.replace('B X', '1') for w in NumberList2]
NumberList2 = [w.replace('B Y', '5') for w in NumberList2]
NumberList2 = [w.replace('B Z', '9') for w in NumberList2]
NumberList2 = [w.replace('C X', '2') for w in NumberList2]
NumberList2 = [w.replace('C Y', '6') for w in NumberList2]
NumberList2 = [w.replace('C Z', '7') for w in NumberList2]

answer2 = sum([int(x) for x in NumberList2])

print('Answer to part 1:', answer)
print('Answer to part 2:', answer2)

print("--- %s seconds ---" % (time.time() - start_time))