import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
file_path = os.path.join(script_dir, file_name)

f = open(file_path, "r")

inputs = list(map(int, f.readlines()))


# complexity O(n^2)
def sumofTwo(numbers):
    desiredSum = 2020
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == desiredSum:
                print(numbers[i] * numbers[j])

# complexity O(n^3)
def sumOfThree(numbers):
    desiredSum = 2020
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == desiredSum:
                    print(numbers[i] * numbers[j] * numbers[k])

sumOfThree(inputs)
