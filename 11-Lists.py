# Lists in python

numbers = [4,36,55,6,3,56,3,5,-5,5,-52,4,244]

print(numbers)


# Refer to an element in a list

print(numbers[2])


# iterate throught each element in list

for x in numbers:
    print(x)


# slice a part of the list
# name_of_list[start:stop+1]

sliced = numbers[3:7]
print(sliced)

# name_of_list[start:stop+1]
# let start be blank if you wish to start from zero
# let stop+1 be blank if you wish to let loop go through end
# use negative indexing if you wish to start from last

# get length or number of elements in a list

print(len(numbers))


# append elements in a list

numbers.append(7)
print(numbers)

# sort list
numbers.sort()
print(numbers)
