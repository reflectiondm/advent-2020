import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
file_path = os.path.join(script_dir, file_name)

f = open(file_path, "r")
# expected input format: 1-3 a: abcde
# returns (min, max, requiredChar, password)
def parseInputStr(input):
    parsed = list(map(str.strip, input.split(" ")))
    numbers = parsed[0].split("-")
    return (int(numbers[0]), int(numbers[1]), parsed[1].strip(":"), parsed[2])
    
inputs = list(map(parseInputStr, f.readlines()))

def isPasswordValid_Old(inputTuple):
    min, max, requiredChar, password = inputTuple
    hit = 0
    for char in password:
        if char == requiredChar:
            hit = hit + 1
        if hit > max:
            return False
    
    return hit >= min and hit <= max

# rule a, b - position of required char, starting at 1
def isPasswordValid_New(inputTuple):
    a, b, requiredChar, password = inputTuple
    indexA = a - 1
    indexB = b - 1
    requiredCharAtA = password[indexA] == requiredChar
    requiredCharAtB = password[indexB] == requiredChar
    return (requiredCharAtA != requiredCharAtB) and (requiredCharAtA or requiredCharAtB)


def coundValidPasswords(validationFun, pwdInputs):
    validPasswords = 0
    for inpt in pwdInputs:
        if validationFun(inpt):
            validPasswords = validPasswords + 1
    
    return validPasswords

print('first part:')
print(coundValidPasswords(isPasswordValid_Old, inputs))

print('second part:')
print(coundValidPasswords(isPasswordValid_New, inputs))