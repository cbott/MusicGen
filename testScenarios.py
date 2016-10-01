from supervisedlearn import *

def test_tens():
    tens_tester = Learner(learn_rate=1)
    test = 0
    while True:
        test += 1
        seq = tens_tester.generate()
        values = tens_tester.indices_to_values(seq)
        score = 0
        for val in values:
            if val == 10:
                score += 10
        tens_tester.train(seq, score)
        print (test, seq, score, ["{0:0.2f}".format(i) for i in tens_tester.weights[1][1]])

def test_increasing():
    tens_tester = Learner()
    test = 0
    while True:
        test += 1
        seq = tens_tester.generate()
        values = tens_tester.indices_to_values(seq)
        score = 0
        for i in range(2, len(values)):
            if values[i] > values[i-1]:
                score += 13
        tens_tester.train(seq, score)
        print (test, seq, score, ["{0:0.2f}".format(i) for i in tens_tester.weights[9][8]])
#test_tens()
test_increasing()
