genA = 116
genB = 299
judge_count = 0
counter = 0

while counter < 40000000:
    genA = genA * 16807 % 2147483647
    genB = genB * 48271 % 2147483647
    genA_binary = bin(genA)[2:].zfill(32)
    genB_binary = bin(genB)[2:].zfill(32)
    if str(genA_binary)[-16:] == str(genB_binary)[-16:]:
        judge_count += 1
    counter += 1

print judge_count
