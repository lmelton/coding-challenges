#interview questions

#Find the most frequent integer in an array

arr = [1,5,4,7,2,2,6,5,2,8,7,9,2,1,5,4,6,8,4,6,8,2,4,5,6,5,5,9,1,2,3,4,5,5,6,5]
popular = arr[0]
count = 0
tempCount = 0

for i in arr:
    tempCount = 0
    for j in arr:
        if i == j:
            tempCount += 1
        if tempCount > count:
            popular = i
            count = tempCount

print(popular)

print("-------------------------------------------------")

#Find pairs in an integer array whose sum is equal to 10

arr = [1,5,4,7,2,2,6,5,2,8,7,9,2,1,5,4,6,8,4,6,8,2,4,5,6,5,5,9,1,2,3,4,5,5,6,5]

for i in arr:
    for j in arr:
        if i + j == 10:
            print(str(i) + " and " + str(j))

# Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array.
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}

print("-------------------------------------------------")


# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)

rng = 8
first = 0
second = 1

print(first)
print(second)
for i in range(rng-2):
    result = first + second
    print(result)
    first = second
    second = result

# Find the only element in an array that only occurs once.

numbers = [1,1,2,2,3,3,4,4,5,5,6,7,7,8,8,9,9]

print("-------------------------------------------------")

# Find the first non-repeated character in a String

my_str = "aabbccdeer"
current = "none"
answer = "none"

for i in my_str:
    current = i
    for j in my_str[my_str.index(i)+1:len(my_str)]:
        if j == i:
            current = "none"
            break
    if current != "none":
        answer = current
        break

print(answer)

print("-------------------------------------------------")

# Reverse a String iteratively and recursively

def reverse_it(my_str):
    answer = ""

    for i in my_str:
        answer = i + answer
    print(answer)

my_str = "bigfluffycat"
reverse_it(my_str)

def reverse_recur(my_str):
    if len(my_str) == 0:
        return my_str
    else:
        return reverse_recur(my_str[1:]) + my_str[0]

my_str = "bigfluffycat"
print(reverse_recur(my_str))

print("-------------------------------------------------")
