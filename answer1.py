def pop_snap(n):
    data = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            data.append("PopSnap")
        elif i % 3 == 0:
            data.append("Pop")
        elif i % 5 == 0:
            data.append("Snap")
        else:
            data.append(str(i))
    return data


n = int(input("Enter a positive integer (1 to 100): "))

if 1 <= n <= 100:
    data_array = pop_snap(n)
    print(data_array)
else:
    print("Invalid input. Please enter a positive integer between 1 and 100.")
