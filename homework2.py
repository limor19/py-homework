def print_divisible_numbers(num):
    print(f"The numbers that {num} divides perfectly with are:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

number = int(input("Enter a number: "))
print_divisible_numbers(number)

