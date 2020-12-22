from collections import deque

class deck:
    def __init__(self):
        self.cards = deque()

class player:
    def __init__(self, id):
        self.id = id
        self.deck = deck()

class game:
    def __init__(self):
        self.players = []
        with open('input.txt', 'r') as inputfile:
            for p in inputfile.read().split('\n\n'):
                self.player = player(int(p.strip().split('Player ')[1].split(':')[0]))
                for i in p.strip().split(':')[1].strip().split('\n'):
                    self.player.deck.cards.append(int(i))
                self.players.append(self.player)
    def play_round(self):
        round = {}
        for p in self.players:
            round[p.id] = p.deck.cards.popleft()
        winner = max(round, key=round.get)
        for p in self.players:
            if p.id == winner:
                p.deck.cards.append(round[p.id])
                del round[p.id]
                for r in round:
                    p.deck.cards.append(round[r])

def part1():
    cardgame = game()
    finished = False
    while finished != True:
        cardgame.play_round()
        for player in cardgame.players:
            if len(player.deck.cards) == 0:
                finished = True
    for p in cardgame.players:
        if len(p.deck.cards) > 0:
            score = 0
            for i in range(1, len(p.deck.cards) + 1):
                score += i * p.deck.cards.pop()
            print(score)

if __name__ == '__main__':
    part1()

