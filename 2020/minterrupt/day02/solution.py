import io
import os

os.chdir(os.path.dirname(__file__))

passwords = []
validSledCo = []
validTobogganCo = []

def collect():
    global passwords
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            policy, pwd = line.split(":")
            minmax, char = policy.split(" ")
            mn, mx = minmax.split("-")
            res = {
                "char": char,
                "min": int(mn),
                "max": int(mx),
                "pwd": pwd[1:]
            }
            passwords.append(res)

def validateSledCo():
    for p in passwords:
        cnt = p["pwd"].count(p["char"])
        if (cnt >= p["min"]) and (cnt <= p["max"]):
            validSledCo.append(p["pwd"])

def validateTobogganCo():
    global passwords
    for p in passwords:
        print(p["char"] + " =? " + p["pwd"][(p["min"]-1)])
        print(p["pwd"][p["max"]-1])
        f1rst = (p["pwd"][p["min"]-1] == p["char"])
        twond = (p["pwd"][p["max"]-1] == p["char"])
        print("^ " + str((f1rst or twond) and not (f1rst and twond)))
        if (f1rst and not twond) or (not f1rst and twond):
            validTobogganCo.append(p["pwd"])

collect()
validateSledCo()
validateTobogganCo()
# print("passwords: " + str(passwords) + "\n")
print("valid sled co: " + str(len(validSledCo)) + "\n")
print("valid toboggan co: " + str(len(validTobogganCo)) + "\n")