import random

num = int(input('Enter number of candidates: '))
cand = input(f'Enter {num} candidates now: \n').split()

print('Candidates are: ', cand)
print('Voting is live... please wait for the results...')
print('Voting has been finished... and wait is over')
print('Here are the results')
vote = []

for x in range(0, num):
    c = random.randrange(1, 100, 3)
    vote.append(c)

for i in range(num):
    print(cand[i], " : ", vote[i])

print('Hence the winner is ...')
maximum = max(vote)
count = 0

for r in range(num):
    if vote[r] == maximum:
        count = r

print(cand[count], " : ", maximum)

