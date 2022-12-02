# Elves are logging the calories of the food items that they are carrying.
# Each elf logs each item individually on a new line, the next
# elf leaves an empty line before starting their list.

# Question 1:
# How many calories is the elf with the most calories carrying?
# Question 2:
# How many calories are each of the top 3 elves with the most calories carrying?
my_file = open('./Input.txt', 'r')

# reading the file
data = my_file.read()

# Splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")

#print(data_into_list)

my_file.close()

Elves = []
CumCount = 0
MaxCal = 0
for item in data_into_list:
    if item == '':
        Elves.append(CumCount)
        CumCount = 0
    else:
        num = int(item)
        CumCount += num
    
    if CumCount > MaxCal:
        MaxCal = CumCount

print("Answer to part 1: ", MaxCal)
print("Answer to part 2: ", sum(sorted(Elves, reverse=True)[:3]))