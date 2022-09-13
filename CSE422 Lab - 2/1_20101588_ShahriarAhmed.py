"""
Shahriar Ahmed - 20101588 - Lab2 - Genetic Algorithm

Sample Input - 1:

8 330
Tamim 68
Shoumyo 25
Shakib 70
Afif 53
Mushfiq 71
Liton 55
Mahmudullah 66
Shanto 29
"""

import random

matrix = []
with open('sample1.txt') as file:
    for i in file:
        lst = [x.strip() for x in i.split()]
        matrix.append(lst)
print("Sample Input:")
print(matrix)
no_bats = int(matrix[0][0])
target = int(matrix[0][1])
batsmen = []
average = []
matrix.pop(0)
for i in range(len(matrix)):
    batsmen.append(matrix[i][0])
    average.append(int(matrix[i][1]))


combos = []
def bit_generate(n, s = ''):
    if len(s) < n:
        bit_generate(n, s + '0')
        bit_generate(n, s + '1')
    else:
        combos.append(s)

bit_generate(no_bats)


fit = []
run = 0
def fitness(combos, fit, batsmen, average, run):
    for i in range(len(combos)):
        run = 0
        for j in range(len(combos[i])):
            if combos[i][j] == '1':
                run += average[j]
        fit.append(run)

    return fit

fitness(combos, fit, batsmen, average, run)


fit_chart = []
def selection(combos, fit):
    for i in range(len(fit)):
        if (fit[i] >= ((target * 80) / 100) and fit[i] <= ((target * 120) / 100)):
            temp1 = (combos[i], fit[i])
            fit_chart.append(temp1)

    return fit_chart

selection(combos, fit)


parent = []
value = []
for i in range(len(fit_chart)):
    parent.append(fit_chart[i][0])
    value.append(fit_chart[i][1])

def crossover(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    point = random.randint(1, len(parent1)-2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent1[:point] + parent2[point:]
    global child
    child = [child1, child2]

    return child


def mutate(child):
    idx1 = random.randint(0, 2)
    idx2 = random.randint(2, 3)
    if child[0][idx1] == '0':
        child[0][idx1].replace('0', '1')
    else:
        child[0][idx1].replace('1', '0')

    if child[1][idx2] == '0':
        child[1][idx2].replace('0', '1')
    else:
        child[0][idx2].replace('1', '0')

    return child


"""Driver Code"""


global parent1, parent2
children = []
generations = 100
for i in range(generations):
    parent1 = random.choice(parent)
    parent2 = random.choice(parent)
    for c in crossover(parent1, parent2):
        mutate(child)
        children.append(c)


final = []
fitness(children, final, batsmen, average, run)

print("Output:")

count = 0
for i in range(len(final)):
    if final[i] == target:
        count += 1
        print(children[i])
        break

if count > 0:
    pass
else:
    print("-1")