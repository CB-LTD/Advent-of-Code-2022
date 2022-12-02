
#f = open('./Input.txt','r')

#data = f.readlines()
##data2 = f.read().splitlines()

#f.close()

#print(data)



#with open('./Input.txt') as file:
#    for line in file:
#        print(line.rstrip())


#with open('./Input.txt') as file:
#    lines = [line.rstrip() for line in file]


my_file = open('./Input3.txt', 'r')

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