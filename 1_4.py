count = 0
sum_of_numbers = 0

for i in range(101, 200):
    if i % 7 == 0:
        count += 1
        sum_of_numbers += i

print("Number of integers divisible by 7:", count)
print("Sum of integers divisible by 7:", sum_of_numbers)
