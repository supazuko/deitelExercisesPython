number = int(input("Enter a number: "))

if 9999 < number < 100000:
    fifth = number % 10
    number //= 10
    fourth = number % 10
    number //= 10
    third = number % 10
    number //= 10
    second = number % 10
    number //= 10
else:
    print("Invalid input")


print(number, "   ", second, "   ", third, "   ", fourth, "   ", fifth)
