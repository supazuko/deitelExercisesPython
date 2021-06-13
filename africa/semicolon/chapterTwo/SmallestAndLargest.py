firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

total = firstNumber + secondNumber + thirdNumber
product = firstNumber * secondNumber + thirdNumber
average = total / 3
if firstNumber > secondNumber:
    largest = firstNumber
    smallest = secondNumber
else:
    largest = secondNumber
    smallest = firstNumber
if thirdNumber > largest:
    largest = thirdNumber
if thirdNumber < smallest:
    smallest = thirdNumber


print(total, product, average)
print("smallest number is: ", smallest)
print("largest number is: ", largest)