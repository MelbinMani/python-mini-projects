n = int(input("Enter any non-negative and non-zero integer number: "))
if n <= 0:
    print("Please enter a valid positive integer.")
else:
    steps = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(n)  # Print the last number which is 1
    print("Steps:", steps)
