from supervisedlearn import Learner
from soundlib import TonePlayer
import sys

def test_tens():
    tens_tester = Learner(learn_rate=0.5)
    test = 0
    while True:
        test += 1
        seq = tens_tester.generate()
        values = tens_tester.indices_to_values(seq)
        score = 0
        for val in values:
            if val == 10:
                score += 20
        tens_tester.train(seq, score)
        print test, seq, score, ["{0:0.2f}".format(i) for i in tens_tester.weights[1][1]]

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
        print test, seq, score, ["{0:0.2f}".format(i) for i in tens_tester.weights[5][4]]

def test_song():
    player = TonePlayer()
    tone_tester = Learner(min=500, max=1000, step=100, learn_rate=0.1)
    test = 0
    while True:
        test += 1
        seq = tone_tester.generate()
        values = tone_tester.indices_to_values(seq)
        score = 0
        for val in values:
            if val == 900:
                score += 20
        tone_tester.train(seq, score)
        print test, seq, score, ["{0:0.2f}".format(i) for i in tone_tester.weights[4][4]]
        if test > 800:
            player.play(values,0.1)
        #raw_input("continue")
if __name__ == "__main__":
    test = sys.argv[1]
    if test == "tens":
        test_tens()
    elif test == "increasing":
        test_increasing()
    elif test == "song":
        test_song()
    else:
        print "No known test %s" %test