import time
# Runtime: 

# Each row of data represents a bag. Each character in the row represents an item in that bag.
# Each item has its own priority: [a-z] = [1-26], [A-Z] = [27-52]
# Each bag has two compartments, each compartment holds an equal number of items (n/2).
# The first half of the row is the first compartment, second half is second compartment.
# No item should be in both compartments, however in every row there is one item type
# that is in both compartments.

# Question 1:
# Sum the priority of all item types that are in both compartments.
# i.e. if the bag was AaaC, a is in both compartments and has a priority of 1, so the answer would be 1.

# This is for timing run time
start_time = time.time()

# Read the file into a variable
my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

# Splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

#print(data_into_list)

my_file.close()

# This shows that the number of items in the bag varies (min <> max)
print(min(map(len, data_into_list)))
print(max(map(len, data_into_list)))

# defining a funtion that returns 1 if a number is off & 0 if it is even.
def Div2(number):
    return number % 2

# Create a list that contains the number of items in each bag.
DataLength = map(len, data_into_list)

# Create a list that does modulo 2 to the number of items in each bag.
Remainders = map(Div2, DataLength)

# If all bags contain an even number of items this will return 0.
ContainsOdds = max(Remainders)
print(ContainsOdds)

# print(DataLength)

# EvenCheck = any(ele % 2 == 1 for ele in DataLength)
# print(EvenCheck)
# # any(flag % 2 == 1 for ())