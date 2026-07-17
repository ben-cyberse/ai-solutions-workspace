numbers = [3, 8, 11, 14, 20, 25]

total = 0

for n in numbers:
    if n % 2 == 0:
        total += n

print("Sum of even numbers:", total)