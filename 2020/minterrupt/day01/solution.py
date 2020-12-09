import io
import os

os.chdir(os.path.dirname(__file__))

lowVals  = []
highVals = []
dimsum = 0
lodoswar = 0

def collect():
    global lowVals, highVals
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            l = int(line)
            if l > 1010:
                highVals.append(l)
            else:
                lowVals.append(l)

def add():
    global lowVals, highVals, dimsum, lodoswar
    for lo in lowVals:
        for hi in highVals:
            if lo + hi == 2020:
                print("2x: lo: " + str(lo) + " hi: " + str(hi) + "\n")
                result = lo * hi
                print("2x: " + str(result) + "\n")
                dimsum = result
            
            for lodo in lowVals:
                if lo + lodo + hi == 2020:
                    print("3x: lo: " + str(lo) + " lodo: " + str(lodo) + " hi: " + str(hi) + "\n")
                    result = lo * hi * lodo
                    print("3x: " + str(result) + "\n")
                    lodoswar = result
                    
                


collect()
add()
print("dimsum: " + str(dimsum) + "\n")
print("lodoswar: " + str(lodoswar) + "\n")