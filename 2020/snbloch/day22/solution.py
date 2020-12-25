from collections import deque

class Deck:
    def __init__(self):
        self.cards = deque()

class Player:
    def __init__(self, id):
        self.id = id
        self.deck = Deck()
        self.seen = set()

class Game:
    def __init__(self, stateful):
        self.finished = False
        self.players = []
        self.stateful = stateful
        self.winner = None
    def play_game(self):
        while self.finished == False:
            self.play_round()
            for p in self.players:
                if len(p.deck.cards) == 0:
                    self.finished = True
    def play_round(self):
        round = {}
        if self.stateful == True:
            seen_before = True
            for p in self.players:
                if ''.join(str(p.deck.cards)) not in p.seen:
                    seen_before = False
                p.seen.add(''.join(str(p.deck.cards)))
            if seen_before == True:
                self.finished = True
                self.winner = self.players[0].id
            else:
                play_recursive = True
                for p in self.players:
                    round[p.id] = p.deck.cards.popleft()
                    if len(p.deck.cards) < round[p.id]:
                        play_recursive = False
                if play_recursive == True:
                    game_recursive = Game(True)
                    for p in self.players:
                        recursive_deck = Deck()
                        for i in list(p.deck.cards)[:round[p.id]]:
                            recursive_deck.cards.append(i)
                        p1 = Player(p.id)
                        p1.deck = recursive_deck
                        game_recursive.players.append(p1)
                    game_recursive.play_game()
                    self.winner = game_recursive.winner
                else:
                    self.winner = max(round, key=round.get)
            for p in self.players:
                if p.id == self.winner:
                    if len(round) > 0:
                        p.deck.cards.append(round[p.id])
                        del round[p.id]
                        for r in round:
                            p.deck.cards.append(round[r])
        else:
            for p in self.players:
                round[p.id] = p.deck.cards.popleft()
            self.winner = max(round, key=round.get)
            for p in self.players:
                if p.id == self.winner:
                    p.deck.cards.append(round[p.id])
                    del round[p.id]
                    for r in round:
                        p.deck.cards.append(round[r])

def part1():
    cardgame = Game(False)
    with open('input.txt', 'r') as inputfile:
        players = inputfile.read().split('\n\n')
    for p in players:
        p1 = Player(int(p.strip().split('Player ')[1].split(':')[0]))
        for i in p.strip().split(':')[1].strip().split('\n'):
            p1.deck.cards.append(int(i))
        cardgame.players.append(p1)
    cardgame.play_game()
    for p in cardgame.players:
        if len(p.deck.cards) > 0:
            score = 0
            for i in range(1, len(p.deck.cards) + 1):
                score += i * p.deck.cards.pop()
            print(score)

def part2():
    cardgame = Game(True)
    with open('input.txt', 'r') as inputfile:
        players = inputfile.read().split('\n\n')
    for p in players:
        p1 = Player(int(p.strip().split('Player ')[1].split(':')[0]))
        for i in p.strip().split(':')[1].strip().split('\n'):
            p1.deck.cards.append(int(i))
        cardgame.players.append(p1)
    cardgame.play_game()
    for p in cardgame.players:
        if p.id == cardgame.winner:
            score = 0
            for i in range(1, len(p.deck.cards) + 1):
                score += i * p.deck.cards.pop()
            print(score)

if __name__ == '__main__':
    part1()
    part2()