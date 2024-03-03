
scores = [60, 50, 60, 58, 54, 54, 
          58, 50, 52, 54, 48, 69, 
          34, 55, 51, 52, 44, 51, 
          69, 64, 66, 55, 52, 61, 
          46, 31, 57, 52, 44, 18, 
          41, 53, 55, 61, 51, 44]

high_score = 0

lenght = len(scores)

print(lenght)

for i in range(lenght):
    print('Bubble solution #'+ str(i), 'score', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]

print('Bubble tests:', lenght)
print('Highest bubble score:', high_score)

best_solutions = []

for i in range(lenght):
    if high_score == scores[i]:
        best_solutions.append(i)

print('Solutions with the highest score:', best_solutions)

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

cost = 100.0
most_effective = 0

for i in range(lenght):
    if scores[i] == high_score and costs[i] < cost:
        most_effective = i
        cost = costs [i]

print('Solution', most_effective, 'is the effective with a cost of', costs[most_effective])