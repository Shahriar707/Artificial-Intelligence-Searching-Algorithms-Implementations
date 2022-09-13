"""
Alpha - Beta - Pruning with Mini-Max Algorithm
Lab - 3 - Shahriar Ahmed - ID - 20101588
"""

import math
import random

ID = input("Please enter your id: ")
check = False
if len(ID) == 8:
    check = True
else:
    check = False
updated = ''
if check:
    for i in range(len(ID)):
        if ID[i] == '0':
            updated += '8'
        else:
            updated += ID[i]

lowest = int(updated[4])
to_win = int(updated[len(ID)-1:len(ID)-3:-1])
highest = int(to_win * 1.5)
shuffles = int(updated[3])
levels = int(input("Enter the number of levels: "))
depth = levels - 1
leaf_nodes = int(math.pow(2, (levels-1)))
root = int(input("Enter the root node: "))
value = int((input("Enter the value of staring node: ")))
print()
m_node = True
alpha = -math.inf
beta = math.inf

def mini_max_algo(start, term, bool, point, alpha, beta):
    if start == depth:
        return point[term]
    elif bool == True:
        score = alpha
        for i in range(0, depth-1):
            temp = mini_max_algo(start+1, (term * 2) + i, False, point, alpha, beta)
            score = max(score, temp)
            alpha = max(alpha, score)
            if alpha >= beta:
                break
    else:
        score = beta
        for i in range(0, depth-1):
            temp = mini_max_algo(start+1, (term * 2) + i, True, point, alpha, beta)
            score = min(score, temp)
            beta = min(beta, score)
            if alpha >= beta:
                break
    return score

print("Total points to win: ", to_win)
print()
shuffle_list = []
for i in range(shuffles):
    terminal = []
    for i in range(leaf_nodes):
        a = random.randint(lowest, highest)
        terminal.append(a)
    print("Generated 8 random points between the minimum and maximum point limits: ")
    print(terminal)
    a = mini_max_algo(root, value, True, terminal, alpha, beta)
    print("Achieved point by applying alpha-beta pruning = ", a)
    if a >= to_win:
        print("The winner is Optimus Prime")
    else:
        print("The Winner is Megatron")
    print()
    shuffle_list.append(a)
print("After the shuffle: ")
print("List of all points values from each shuffles:")
print(shuffle_list)
count = 0
for i in range(len(shuffle_list)):
    if shuffle_list[i] >= to_win:
        count += 1
print("The maximum value of all shuffles: ", max(shuffle_list))
print("Won", count, "times out of", len(shuffle_list), "number of shuffles")