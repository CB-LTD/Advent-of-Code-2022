
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


my_file = open('./Input.txt', 'r')
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
my_file.close()