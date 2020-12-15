import os
import re # regex

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
file_path = os.path.join(script_dir, file_name)

f = open(file_path, "r")

def parseInputStr(input):
    return str.strip(input)
    

inputs = list(map(parseInputStr, f.readlines()))

def sanitizeInputs(rawInputs):
    result = []
    currentPassportData = ""
    for raw in inputs:
        if len(raw) == 0:
            result.append(currentPassportData)
            currentPassportData = ""
            continue
        currentPassportData = currentPassportData + " " + raw
    
    result.append(currentPassportData)
    return result

class PassportData:
    def __init__(self, stringPassportData):
        self.__hclRegex = re.compile("^(#([a-f0-9]{6}|[a-f0-9]{3}))$")
        self.__pidRegex = re.compile("^[0-9]{9}$")

        dataPoints = str.split(stringPassportData)
        dataDictionary = {
            "byr": "",
            "iyr": "",
            "eyr": "",
            "hgt": "",
            "hcl": "",
            "ecl": "",
            "pid": "",
            "cid": ""
        }
        for dataPoint in dataPoints:
            pair = str.split(dataPoint, ":")
            key = pair[0]
            value = pair[1]
            dataDictionary[key] = value
       
        self.byr = dataDictionary["byr"] 
        self.iyr = dataDictionary["iyr"]
        self.eyr = dataDictionary["eyr"]
        self.hgt = dataDictionary["hgt"]
        self.hcl = dataDictionary["hcl"]
        self.ecl = dataDictionary["ecl"]
        self.pid = dataDictionary["pid"]
        self.cid = dataDictionary["cid"]
    
    def allMandatoryFieldsPresent(self):
        return (self.byr != "") and \
        (self.iyr != "") and \
        (self.eyr != "") and \
        (self.hgt != "") and \
        (self.hcl != "") and \
        (self.ecl != "") and \
        self.pid != ""

    def byrIsValid(self):
        return self.__dateIsValid(self.byr, 1920, 2002)

    def iyrIsValid(self):
        return self.__dateIsValid(self.iyr, 2010, 2020)

    def eyrIsValid(self):
        return self.__dateIsValid(self.eyr, 2020, 2030)

    def __dateIsValid(self, dateStr, min, max):
        try:
            value = int(dateStr)
            return len(dateStr) == 4 and \
                value >= min and value <= max
        except:
            return False

    def hgtIsValid(self):
        try:
            unit = self.hgt[-2:]
            value = int(self.hgt[0: len(self.hgt) - 2])
            if unit == "cm":
                return value >= 150 and value <= 193
            if unit == "in":
                return value >= 59 and value <= 76
        except:
            return False
        
    def hclIsValid(self):
        return bool(self.__hclRegex.match(self.hcl))

    def eclIsValid(self):
        allowedColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl in allowedColors

    def pidIsValid(self):
        return bool(self.__pidRegex.match(self.pid))

    def isValid(self):
        return self.allMandatoryFieldsPresent() and \
            self.byrIsValid() and \
            self.iyrIsValid() and \
            self.eyrIsValid() and \
            self.hgtIsValid() and \
            self.hclIsValid() and \
            self.eclIsValid() and \
            self.pidIsValid()


def findValidPassports_firstTask(inputs):
    stringPassportsData = sanitizeInputs(inputs)
    passports = map(lambda data: PassportData(data), stringPassportsData)

    numberOfValidPassports = 0
    for passport in passports:
        if passport.allMandatoryFieldsPresent():
            numberOfValidPassports = numberOfValidPassports + 1
    
    return numberOfValidPassports

def findValidPassports_secondTask(inputs):
    stringPassportsData = sanitizeInputs(inputs)
    passports = map(lambda data: PassportData(data), stringPassportsData)

    numberOfValidPassports = 0
    for passport in passports:
        if passport.isValid():
            numberOfValidPassports = numberOfValidPassports + 1
    
    return numberOfValidPassports

print('first part:')
print(findValidPassports_firstTask(inputs))

print('second part:')
print(findValidPassports_secondTask(inputs))