# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Determine the start and end points regardless of input order
start = min(num1, num2)
end = max(num1, num2)
# Print numbers strictly between start and end
for i in range(start + 1, end):
    print(i)