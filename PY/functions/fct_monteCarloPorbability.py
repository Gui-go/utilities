from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))

if __name__ == '__main__':
    roll_dice(6)
    print("---")
    roll_dice(6,6)
    print("---")
    roll_dice(6,6,6)

# Returns the probability of each outcome by the Monte Carlo method

# Dict subclass for counting hashable items. Sometimes called a bag or multiset. Elements are stored as dictionary keys and their counts are stored as dictionary values.

# c = Counter('zzzabcdeabcdabcaba')  # count elements from a string
# c.most_common(3)                # three most common elements
# c.most_common(4)
# sorted(c)                       # list all unique elements
# ''.join(sorted(c.elements()))   # list elements with repetitions
# sum(c.values())                 # total of all counts


# c.items()
# c.keys()

# counts = Counter()
# counts[1]+=1
# counts[13]+=1
# counts["a"]+=1



