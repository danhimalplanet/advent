class math:
    def __init__(self):
        self.collapsed = []
    def run(self, input_string):
        i = 0
        while i < len(input_string):
            if input_string[i] == ' ':
                i += 1
            elif input_string[i] == ')':
                i += 1
            elif input_string[i] == '(':
                start_pos = i+1
                end_pos = i + self.find_end(input_string[start_pos:])
                collapsed_eval = self.collapse(input_string[start_pos:end_pos + 1])
                self.collapsed.append(int(collapsed_eval))
                i = end_pos + 1
            elif input_string[i] == '*' or input_string[i] == '+':
                self.collapsed.append(input_string[i])
                i += 1
            else:
                self.collapsed.append(int(input_string[i]))
                i += 1
        
        total = self.collapsed[0]
        for i in range(len(self.collapsed)):
            if self.collapsed[i] == '*':
                total *= self.collapsed[i+1]
                i += 2
            elif self.collapsed[i] == '+':
                total += self.collapsed[i+1]
                i += 2
        return total
    def find_end(self, substring):
        parens_count = 1
        for i in range(len(substring)):
            if parens_count > 0:
                if substring[i] == '(':
                    parens_count += 1
                elif substring[i] == ')':
                    parens_count -= 1
                    if i == len(substring) - 1:
                        return i
            else:
                return i
    def collapse(self, substring):
        collapsed_string = []
        if substring.count('(') == 0:
            
            for i in range(len(substring)):
                if substring[i] == ' ':
                    continue
                else:    
                    collapsed_string.append(substring[i])
            total = int(collapsed_string[0])        
            i = 0
            while i < len(collapsed_string):
                if collapsed_string[i] == '*':
                    total *= int(collapsed_string[i+1])
                    i += 2
                elif collapsed_string[i] == '+':
                    total += int(collapsed_string[i+1])
                    i += 2
                else:
                    i += 1
            return total
        else:
            
            i = 0
            while i < len(substring):
                if substring[i] == ' ':
                    i += 1
                elif substring[i] == '(':
                    start_pos = i+1
                    end_pos = i + self.find_end(substring[start_pos:])
                    collapsed_string.append(self.collapse(substring[start_pos:end_pos + 1]))
                    i = end_pos + 1
                elif substring[i] == ')':
                    i += 1
                elif substring[i] == '*' or substring[i] == '+':
                    collapsed_string.append(substring[i])
                    i += 1
                else:
                    collapsed_string.append(int(substring[i]))
                    i += 1
            
            total = int(collapsed_string[0])        
            i = 0
            while i < len(collapsed_string):
                if collapsed_string[i] == '*':
                    total *= int(collapsed_string[i+1])
                    i += 2
                elif collapsed_string[i] == '+':
                    total += int(collapsed_string[i+1])
                    i += 2
                else:
                    i += 1
            return total

class advancedmath:
    def __init__(self):
        self.collapsed = []
    def run(self, input_string):
        i = 0
        while i < len(input_string):
            if input_string[i] == ' ':
                i += 1
            elif input_string[i] == ')':
                i += 1
            elif input_string[i] == '(':
                start_pos = i+1
                end_pos = i + self.find_end(input_string[start_pos:])
                collapsed_eval = self.collapse(input_string[start_pos:end_pos + 1])
                self.collapsed.append(int(collapsed_eval))
                i = end_pos + 1
            elif input_string[i] == '*' or input_string[i] == '+':
                self.collapsed.append(input_string[i])
                i += 1
            else:
                self.collapsed.append(int(input_string[i]))
                i += 1
        
        while len(self.collapsed) > 1:
            if self.collapsed.count('+') > 0:
                i = self.collapsed.index('+')
                newval = self.collapsed[i-1] + self.collapsed[i+1]
                self.collapsed.pop(i-1)
                self.collapsed.pop(i-1)
                self.collapsed.pop(i-1)
                self.collapsed.insert(i-1, newval)
            else:
                i = self.collapsed.index('*')
                newval = self.collapsed[i-1] * self.collapsed[i+1]
                self.collapsed.pop(i-1)
                self.collapsed.pop(i-1)
                self.collapsed.pop(i-1)
                self.collapsed.insert(i-1, newval)     
        return self.collapsed[0]
    def find_end(self, substring):
        parens_count = 1
        for i in range(len(substring)):
            if parens_count > 0:
                if substring[i] == '(':
                    parens_count += 1
                elif substring[i] == ')':
                    parens_count -= 1
                    if i == len(substring) - 1:
                        return i
            else:
                return i
    def collapse(self, substring):
        collapsed_string = []
        if substring.count('(') == 0:
            
            for i in range(len(substring)):
                if substring[i] == ' ' or substring[i] == ')':
                    continue
                elif substring[i] == '+' or substring[i] == '*':    
                    collapsed_string.append(substring[i])
                else:
                    collapsed_string.append(int(substring[i]))
            while len(collapsed_string) > 1:
                if collapsed_string.count('+') > 0:
                    i = collapsed_string.index('+')
                    newval = collapsed_string[i-1] + collapsed_string[i+1]
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.insert(i-1, newval)
                else:
                    i = collapsed_string.index('*')
                    newval = collapsed_string[i-1] * collapsed_string[i+1]
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.insert(i-1, newval)     
            return collapsed_string[0]
        else:
            
            i = 0
            while i < len(substring):
                if substring[i] == ' ':
                    i += 1
                elif substring[i] == '(':
                    start_pos = i+1
                    end_pos = i + self.find_end(substring[start_pos:])
                    collapsed_string.append(self.collapse(substring[start_pos:end_pos + 1]))
                    i = end_pos + 1
                elif substring[i] == ')':
                    i += 1
                elif substring[i] == '*' or substring[i] == '+':
                    collapsed_string.append(substring[i])
                    i += 1
                else:
                    collapsed_string.append(int(substring[i]))
                    i += 1
        
            while len(collapsed_string) > 1:
                if collapsed_string.count('+') > 0:
                    i = collapsed_string.index('+')
                    newval = collapsed_string[i-1] + collapsed_string[i+1]
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.insert(i-1, newval)
                else:
                    i = collapsed_string.index('*')
                    newval = collapsed_string[i-1] * collapsed_string[i+1]
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.pop(i-1)
                    collapsed_string.insert(i-1, newval)     
            return collapsed_string[0]
  

def part1():
    total = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            problem = math()
            total += problem.run(line.strip())
    print(total)

def part2():
    total = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            problem = advancedmath()
            total += problem.run(line.strip())
    print(total)

if __name__ == '__main__':
    part1()
    part2()