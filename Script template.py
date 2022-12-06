import time
# Runtime: 

# Intro here

# Question 1:
# 

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

# [MAIN]

answer  = ''
answer2 = ''

print('Answer to part 1:', answer)
print('Answer to part 2:', answer2)

print("--- %s seconds ---" % (time.time() - start_time))