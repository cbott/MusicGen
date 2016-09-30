from supervisedlearn import *

def test_tens():
    tens_tester = Learner()
    while True:
        seq = tens_tester.generate()
        values = tens_tester.indices_to_values(seq)
        score = 0
        for val in values:
            if val == 10:
                score += 10
        tens_tester.train(seq, score)
        print (seq, score, tens_tester.weights[1][1])

def test_increasing():
    tens_tester = Learner()
    while True:
        seq = tens_tester.generate()
        values = tens_tester.indices_to_values(seq)
        score = 0
        for i in range(2, len(values)):
            if values[i] > values[i-1]:
                score += 13
        tens_tester.train(seq, score)
        print (seq, score, tens_tester.weights[8][9])

test_increasing()
