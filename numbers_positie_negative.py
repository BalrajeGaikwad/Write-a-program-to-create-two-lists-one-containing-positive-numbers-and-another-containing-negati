"""
Suppose a list contains positive and negative numbers. Write a program to create two lists-one containing positive numbers and another containing negative numbers.

"""

num=[-1,-2,3,4,5,3,2,2,-4,-9,-5]

positive=[]
negative=[]

for i in num:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)


print("positive numbers :",positive)
print("negative numbers: ",negative)