import itertools

mainLeg = ["a", "b", "c", "d"]

defenses = ["1", "2", "3", "4"]

subLegs = []

for comb in itertools.combinations(mainLeg, 3):
    print comb
