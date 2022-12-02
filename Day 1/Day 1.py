# Elves are logging the calories of the food items that they are carrying.
# Each elf logs each item individually on a new line, the next
# elf leaves an empty line before starting their list.

# Question 1:
# How many calories is the elf with the most calories carrying?
# Question 2:
# How many calories are each of the top 3 elves with the most calories carrying?

# Open file
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
        Elves.append(CumCount)  # Creates an elf level list, summing each elfs calories.
        CumCount = 0            # Reset cumulative calorie count per elf.
    else:
        num = int(item)         # Cast the string number to an interget
        CumCount += num         # Add next food item to previous (cumulative calorie count per elf)
    
    if CumCount > MaxCal:
        MaxCal = CumCount       # Variable for holding the highest number of calories any elf has.

print("Answer to part 1: ", MaxCal)
print("Answer to part 2: ", sum(sorted(Elves, reverse=True)[:3]))