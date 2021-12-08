import io
import os
import re

os.chdir(os.path.dirname(__file__))

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validBYR(byr):
    return int(byr) >= 1920 and int(byr) <= 2002

def validIYR(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020

def validEYR(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030

def validHGT(hgt):
    if len(hgt) < 4 or len(hgt) > 5:
        return False
    u = str(hgt)[len(str(hgt))-2:]
    try:
        v = int(str(hgt)[:-2])
    except:
        return False
    if u == "cm":
        return v >= 150 and v <= 193
    if u == "in":
        return v >= 59 and v <= 76
    return False

def validHCL(hcl):
    r = re.compile('[0-9a-f]+')
    # print(r.match(str(hcl)[1:]))
    return len(str(hcl)) == 7 and r.match(str(hcl)[1:]) != None

def validECL(ecl):
    colors = [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    ]
    return str(ecl) in colors

def validPID(pid):
    r = re.compile('[0-9]+')
    return len(pid) == 9 and r.match(str(pid)) != None

dataKeys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]

docs = []
validPPs = []
invalidPPs = []
extraValidPPs = []

def collect():
    global docs
    docs.append({})
    with open("input.txt", "r") as inputFillet:
        for line in inputFillet:
            if len(line.strip()) == 0:
                # print("new passport")
                docs.append({})
                continue
            parts = line.strip().split(" ")
            for p in parts:
                key, val = p.split(":")
                # print(key + " : " + val)
                p = docs[-1]
                p[key] = val
            
def validate(optionalFields):
    global invalidPPs, validPPs
    for d in docs:
        keysInD = len(d.keys())
        optKeys = len(dataKeys)
        # print("# keys: " + str(keysInD))
        # print("# reqd: " + str(optKeys))
        # for k in dataKeys:
            # if d.get(k) == None:
                # print(k)
        if keysInD == optKeys:
            # print("\nOK - has all keys \n\n")
            validPPs.append(d)
            continue
        if keysInD == optKeys - 1 and d.get("cid") == None:
            # print("\nOK - doesnt have cid \n\n")
            validPPs.append(d)
            continue
        # print("BAD\n\n")
        invalidPPs.append(d)

def dubbelValidate():
    global extraValidPPs
    for pp in validPPs:
        if validBYR(pp["byr"]) and validIYR(pp["iyr"]) and validEYR(pp["eyr"]) and validHGT(pp["hgt"]) and validHCL(pp["hcl"]) and validECL(pp["ecl"]) and validPID(pp["pid"]):
            extraValidPPs.append(pp)
        else:
            print(pp)
           
collect()
validate(["cid"])
print(str(len(validPPs)))
dubbelValidate()
print(str(len(extraValidPPs)))
# print(len(docs))
# [print(d["pid"]) for d in docs if "pid" in d.keys()]
