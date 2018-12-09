def part1():
    marble_to_remove = None
    marbles = []
    cur_marble = 0
    cur_score = 0
    players = 455
    last_marble_score = 71223
    scores = {}
    player = 1
    while player <= players:
        scores[player] = 0
        player += 1
    marbles.append(cur_marble)
    cur_position = marbles.index(cur_marble)
    cur_marble += 1
    player = 1
    marbles.append(cur_marble)
    cur_position = marbles.index(cur_marble)
    cur_marble += 1
    player += 1
    while cur_marble <= last_marble_score:
        cur_score = 0
        if cur_marble % 23 == 0:
            count = 0
            while count < 7:
                if cur_position == 0:
                    cur_position = len(marbles) - 1
                else:
                    cur_position -= 1
                count += 1
            cur_score += cur_marble
            marble_to_remove = marbles[cur_position]
            cur_score += marbles[cur_position]
            marbles.remove(marble_to_remove)
            scores[player] += cur_score
            cur_marble += 1
            if player == players:
                player = 1
            else:
                player += 1
        else:
            count = 0
            while count < 1:
                if cur_position == len(marbles) - 1:
                    cur_position = 0
                    count += 1
                else:
                    cur_position += 1
                    count += 1
            marbles.insert(cur_position + 1, cur_marble)
            cur_position = marbles.index(cur_marble)
            if player == players:
                player = 1
            else:
                player += 1
            cur_marble += 1
    final_scores = []
    for i in scores:
        final_scores.append(scores[i])
    print 'Part 1: winning score is',sorted(final_scores, reverse=True)[0]

def part2():
    marble_to_remove = None
    marbles = []
    cur_marble = 0
    cur_score = 0
    players = 455
    last_marble_score = 71223 * 100
    scores = {}
    player = 1
    while player <= players:
        scores[player] = 0
        player += 1
    marbles.append(cur_marble)
    cur_position = marbles.index(cur_marble)
    cur_marble += 1
    player = 1
    marbles.append(cur_marble)
    cur_position = marbles.index(cur_marble)
    cur_marble += 1
    player += 1
    while cur_marble <= last_marble_score:
        cur_score = 0
        if cur_marble % 23 == 0:
            count = 0
            while count < 7:
                if cur_position == 0:
                    cur_position = len(marbles) - 1
                else:
                    cur_position -= 1
                count += 1
            cur_score += cur_marble
            marble_to_remove = marbles[cur_position]
            cur_score += marbles[cur_position]
            marbles.remove(marble_to_remove)
            scores[player] += cur_score
            cur_marble += 1
            if player == players:
                player = 1
            else:
                player += 1
        else:
            count = 0
            while count < 1:
                if cur_position == len(marbles) - 1:
                    cur_position = 0
                    count += 1
                else:
                    cur_position += 1
                    count += 1
            marbles.insert(cur_position + 1, cur_marble)
            cur_position = marbles.index(cur_marble)
            if player == players:
                player = 1
            else:
                player += 1
            cur_marble += 1
        if cur_marble % 100000 == 0:
            print 'Processing marble',cur_marble
    final_scores = []
    for i in scores:
        final_scores.append(scores[i])
    print 'Part 2: winning score is',sorted(final_scores, reverse=True)[0]

if __name__ == '__main__':
    part1()
    part2()
