
numbers = []
serial_num = 1
while True:
    num = int(input(f"Please enter number #{serial_num}: "))
    if num < 0:
        break
    numbers.append(num)
    average = sum(numbers) / len(numbers)
    total_sum = sum(numbers)
    print("Current Mean Average:", average)
    print("Current Sum:", total_sum)
    print()
    serial_num += 1

print("Exiting the program.")

