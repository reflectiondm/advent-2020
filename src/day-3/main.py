import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
file_path = os.path.join(script_dir, file_name)

f = open(file_path, "r")

def parseInputStr(input):
    return str.strip(input)
    

inputs = list(map(parseInputStr, f.readlines()))

# move tobogan taking world wrapping into account
def moveTobogan(i, j, slopePath, slopeLength):
    i, j = slopePath(i, j)
    if i >= slopeLength:
        i = i - slopeLength
    
    return (i, j)

def setSlopePath(iInc, jInc):
    return lambda i, j: (i + iInc, j + jInc)

def isTreeHit(i, j, slope):
    tree = "#"
    return slope[j][i] == tree

def countTrees(inputs, slopePath):
   i, j = (0, 0)
   sumTrees = 0
   slopeLength = len(inputs[0])
   slopeHeight = len(inputs)
   i, j = moveTobogan(i, j, slopePath, slopeLength)

   while j < slopeHeight:    
       if isTreeHit(i, j, inputs):
           sumTrees = sumTrees + 1
       i, j = moveTobogan(i, j, slopePath, slopeLength)
   
   return sumTrees

def analyseAllPaths(inputs):
    slopes = [
        setSlopePath(1, 1),
        setSlopePath(3, 1),
        setSlopePath(5, 1),
        setSlopePath(7, 1),
        setSlopePath(1, 2),
    ]

    treesOnSlopes = map(lambda slope: countTrees(inputs, slope), slopes)

    result = 1
    for treesOnSlope in treesOnSlopes:
        result = result * treesOnSlope
    
    return result


print('first part:')
print(countTrees(inputs, setSlopePath(3, 1)))

print('second part:')
print(analyseAllPaths(inputs))