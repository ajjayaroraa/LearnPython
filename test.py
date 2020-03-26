#program that finds sim of all numbers divisible by 3
'''
n = 11
sum_n = 0
for i in range(n):
    if i % 3 == 0:
        sum_n += i

print(sum_n)

'''

#You are given a string of lowercase characters
#Write a program that finds the count of the number of times m is present
#in the given string
#For example: If the given string is masai the answer is 1

'''
string = input()
substring = "m"

count = string.count(substring)

# print count
print(count)'''

# Given a list of 10 numbers
# find the average of all such numbers which is a multiple of 3

'''
n = [10,15,13,56,52,49,37,18,67,18]
sum_n = 0
count_n = 0
for i in n:
    if i % 3 == 0:
        sum_n += i
        count_n += 1

print(sum_n/count_n)

'''
''''
JEE is one of the most prestigious exams. You need to implement ranking rule in it. Given marks of Physics, Chemistry and Mathematics of two students, Find out who gets better rank using the following rules:

- The student getting more marks in Chemistry gets better rank.
- If two students have same marks in Chemistry then the one who has higher total marks gets a better rank
- In case their marks in Chemistry and total marks are also the same, the one whose marks in Physics is more gets better rank.

You are given marks of two students as 3 integers where the three integers represents their marks in Physics, Chemistry and Mathematics respectively.

Write a program that prints the student(either Student 1 or Student 2) which gets a better rank.
'''

s1_phy = int(input())
s1_che = int(input())
s1_mth = int(input())
s2_phy = int(input())
s2_che = int(input())
s2_mth = int(input())

s1_tot = s1_phy + s1_che + s1_mth
s2_tot = s2_phy + s2_che + s2_mth

if s1_che > s2_che:
    print("Student 1")
elif s2_che > s1_che:
    print("Student 2")
elif s1_tot > s2_tot:
    print("Student 1")
elif s2_tot > s1_tot:
    print("Student 2")
elif s1_phy > s2_phy:
    print("Student 1")
elif s2_phy > s1_phy:
    print("Student 2")
else:
    print("all conditions are exhausted. Marks in chemistry are equal, total marks are equal, and marks in physics are also equal. Program being terminated")
    
