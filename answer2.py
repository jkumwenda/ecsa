def sum_integers(file):
    try:
        with open(file, "r") as file:
            numbers = [int(line.strip()) for line in file]
            return sum(numbers)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except ValueError:
        print("Error: Invalid data.")


file = "numbers.txt"
result_sum = sum_integers(file)

if result_sum is not None:
    print(f"Sum of integers from: {result_sum}")
