#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_score(item):
    return item > 50

print(list(filter(filter_score,scores)))    