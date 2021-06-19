firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
thirdNumber = float(input("Enter third number: "))

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


