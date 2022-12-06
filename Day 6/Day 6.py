import time
# Runtime: --- 0.08382463455200195 seconds ---

# Intro here

# Question 1:
# Find the first instance where a block of 4 consecutive characters contain no
# repeated characters.
# Question 2:
# Same again but 14 not 4


# This is for timing run time
start_time = time.time()

# Read the file into a variable
my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

#print(data)
#print(type(data))

my_file.close()

# Create a list containg the lowercase alphabet:
abc = list(map(chr, range(97, 123)))
#print(len(abc))
#print(abc[0])
#print(data.count(abc[1]))

# Create loop that will serve up each 4 character block.
i = 0
j = 4
x = 0
cnt = 0
max_cnt = 0

while i < len(data):
    temp = data[i:j]
    for item in abc:
        cnt = temp.count(item)
        if cnt > max_cnt:
            max_cnt = cnt
    if max_cnt == 1:
         #print(data[i:j])
         #print(j)
         answer = j
         break
    max_cnt = 0
    x += 1
    i += 1
    j += 1
    
# Question 2:

i = 0
j = 14
x = 0
cnt = 0
max_cnt = 0

while i < len(data):
    temp = data[i:j]
    for item in abc:
        cnt = temp.count(item)
        if cnt > max_cnt:
            max_cnt = cnt
    if max_cnt == 1:
         #print(data[i:j])
         #print(j)
         answer2 = j
         break
    max_cnt = 0
    x += 1
    i += 1
    j += 1   

# answer  = ''
# answer2 = ''

print('Answer to part 1:', answer)
print('Answer to part 2:', answer2)

print("--- %s seconds ---" % (time.time() - start_time))