import time
# Runtime: --- 0.023949623107910156 seconds ---

# Each row of data represents a bag. Each character in the row represents an item in that bag.
# Each item has its own priority: [a-z] = [1-26], [A-Z] = [27-52]
# Each bag has two compartments, each compartment holds an equal number of items (n/2).
# The first half of the row is the first compartment, second half is second compartment.
# No item should be in both compartments, however in every row there is one item type
# that is in both compartments.

# Question 1:
# Sum the priority of all item types that are in both compartments.
# i.e. if the bag was AaaC, a is in both compartments and has a priority of 1, so the answer would be 1.

# Question 2:
# What single item is common in each set of 3 rows?

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

# We have established that all bags contain an even number of items, and the number
# of items ranges from 16 - 48.

# We will split the list into two lists by splitting the strings down the middle.
# We will then compare the elements for what item is in both.

compartment1 = []
compartment2 = []

for item in data_into_list:
    compartment1.append(item[:len(item)//2])
    compartment2.append(item[len(item)//2:])

i = 0
DuplicateItems = [] # This list contains all duplicate items.

while i < len(compartment1):
    DuplicateItems.append(''.join(set(compartment1[i]).intersection(compartment2[i])))
    i += 1

# print(DuplicateItems)

# Next we must assign each letter its priority value.
# ord(') returns the unicode value of strings, and the letters of the alphabet are
# sequential (case independant)

# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(ord('B'))

ItemPriority = []

for item in DuplicateItems:
    if ord(item) >= 97:
        ItemPriority.append(ord(item) - ord('a') + 1)
    else:
        ItemPriority.append(ord(item) - ord('A') + 27)

## sense check: repeated priority ranges 2-52. Potential range: 1-52.
# print(min(ItemPriority))
# print(max(ItemPriority))

answer  = sum(ItemPriority)


# Question 2:
# Here we want to make a list where each item is a list of 3 strings (backpacks).

i  = 0
i2 = 0
GroupList   = []
GroupedList = []
while i < len(data_into_list):
    if i2 < 3:
        GroupList.append(data_into_list[i])
        i2 += 1
        i  += 1
        if i == len(data_into_list)-1:
            GroupedList.append(GroupList)
    else:
        GroupedList.append(GroupList)
        GroupList = []
        i2 = 0
        #i += 1

# print(GroupedList)
# print(len(data_into_list))

# Next we need to find the singular common item in each sub-list.
GroupItem = []
for item in GroupedList:
        a = set(item[0])
        b = set(item[1])
        c = set(item[2])
        join1 = a.intersection(b) 
        join2 = a.intersection(c)
        join3 = repr(join1.intersection(join2))
        GroupItem.append(list(join3))
# This creates a 5 element list e.g. {'A'} is split into its composite characters.

# print(GroupItem)
# print(repr(GroupItem))
# print(str(GroupItem))

ItemPriority2 = []

for item in GroupItem:
    if ord(item[2]) >= 97:
        ItemPriority2.append(ord(item[2]) - ord('a') + 1)
        print(item[2])
    else:
        ItemPriority2.append(ord(item[2]) - ord('A') + 27)
        print(item[2])

answer2 = sum(ItemPriority2)

print(ItemPriority2)

print('Answer to part 1:', answer)
print('Answer to part 2:', answer2)

print("--- %s seconds ---" % (time.time() - start_time))