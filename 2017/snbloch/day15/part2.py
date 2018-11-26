genA = 116
genB = 299
judge_count = 0

genA_results = []
genB_results = []
genA_count = 0
genB_count = 0

while genA_count < 5000000:
    genA = genA * 16807 % 2147483647
    if genA % 4 == 0:
        genA_binary = bin(genA)[2:].zfill(32)
        genA_results.append(genA_binary)
        genA_count += 1

while genB_count < 5000000:
    genB = genB * 48271 % 2147483647
    if genB % 8 == 0:
        genB_binary = bin(genB)[2:].zfill(32)
        genB_results.append(genB_binary)
        genB_count += 1

counter = 0
while counter < 5000000:
    if str(genA_results[counter])[-16:] == str(genB_results[counter])[-16:]:
        judge_count += 1
    counter += 1

print judge_count
