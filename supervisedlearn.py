import random

class Learner():
    def __init__(self, min=0, max=100, step=10, learn_rate=0.02, initial_weight=1, min_weight=1):
        self.min = min # minimun value that can be generated
        self.max = max # maximum value that can be generated
        self.step = step # interval between values that can be generated [ex. 0, 10, 20, 30...]
        self.learn_rate = learn_rate # scaling to apply to training score
        self.min_weight = min_weight

        self.values = []
        for val in range(self.min, self.max, self.step):
            self.values.append(val)
        self.numvals = len(self.values)
        # create a 3D matrix filled with an inital weight
        self.weights = [ [ [ initial_weight for x in range(self.numvals) ] for y in range(self.numvals) ] for z in range(self.numvals) ]
    
    def generate(self, length=10):
        """ Generate a sequence of values """
        seq = [ random.randint(0, self.numvals-1), random.randint(0, self.numvals-1) ]
        for i in range(2,length):
            seq.append(self._next_val(seq[i-1], seq[i-2]))
        return seq

    def _next_val(self, back1, back2):
        """ Determine the next value in a sequence based on weights """
        # Calculate sum of column
        sum = 0
        for z in range(self.numvals):
            sum += self.weights[back1][back2][z]
        index = sum * random.random()
        weight_sum = 0
        for z in range(self.numvals):
            weight_sum += self.weights[back1][back2][z]
            if weight_sum >= index:
                return z

    def train(self, pattern, score):
        """ adjust weights based on a 0-100 score for a sequence """
        scaled_score = (score-50) * self.learn_rate
        for val in range(2, len(pattern)):
            x = pattern[val-1]
            y = pattern[val-2]
            z = pattern[val]
            # the mim=nimum possible weight is 1
            self.weights[x][y][z] = max(self.min_weight, self.weights[x][y][z] + scaled_score)

    def indices_to_values(self, seq):
        result = []
        for i in range(len(seq)):
            result.append(self.values[seq[i]])
        return result

test = Learner()
while True:
    seq = test.generate()
    print(test.indices_to_values(seq))
    score = min(100, max(0, raw_input("Score:")))
    test.train(seq, score)
    print ""