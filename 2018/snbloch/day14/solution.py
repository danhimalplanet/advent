def part1():
    target = 190221
    game = [3, 7]
    player1 = 0
    player2 = 1
    while len(game) <= target + 10:
        sum = game[player1] + game[player2]
        for i in str(sum):
            game.append(int(i))
        move = game[player1] + 1
        counter = 0
        while counter < move:
            if player1 + 1 == len(game):
                player1 = 0
            else:
                player1 += 1
            counter += 1
        move = game[player2] + 1
        counter = 0
        while counter < move:
            if player2 + 1 == len(game):
                player2 = 0
            else:
                player2 += 1
            counter += 1
    print 'Part 1:',''.join(str(i) for i in game[target:target + 10])

def part2():
    target = '190221'
    game = [3, 7]
    player1 = 0
    player2 = 1
    found = False
    while found == False:
        sum = game[player1] + game[player2]
        for i in str(sum):
            game.append(int(i))
        move = game[player1] + 1
        counter = 0
        while counter < move:
            if player1 + 1 == len(game):
                player1 = 0
            else:
                player1 += 1
            counter += 1
        move = game[player2] + 1
        counter = 0
        while counter < move:
            if player2 + 1 == len(game):
                player2 = 0
            else:
                player2 += 1
            counter += 1
        if ''.join(str(i) for i in game[-len(target):]) == target:
            print 'Part 2:',len(game) - len(target)
            found = True
        if ''.join(str(i) for i in game[-(len(target) + 1):-1]) == target:
            print 'Part 2:',len(game) - (len(target) + 1)
            found = True

if __name__ == '__main__':
    part1()
    part2()
