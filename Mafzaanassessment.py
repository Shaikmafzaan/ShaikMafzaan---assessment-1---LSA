number = input("enter the number")
if number is number:
    print("palindrome")
else :
    print("not a palindrome")
    
# 2.
number = (input("Enter number of rows: "))

for i in range(1, number + 1):
    print(" " * (number - i) + "*" * (2 * i - 1))
    
#5.
num = [1,2,3,4,5,6,7,8,9]
largest = num[0]
for  i in num:
    if i > largest:
        largest = i
print(largest)

#3.
# Program to count vowels in a string

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for text in text:
    if text in vowels:
        count = 1

print(f"Number of vowels in the string is: {count}")
