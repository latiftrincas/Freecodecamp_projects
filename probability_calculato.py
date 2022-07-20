import random
import copy


class Hat:
    # **var allows for a arbiraty number of instances in the form of a dictonary
    def __init__(self, **var):
        # contents should be a list of strings containing one item for each ball in the hat.
        # Each item in the list should be a color name representing a single ball of that color.
        # if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"]
        global contents
        contents = list()
        self.contents = contents
        # append colour to list for each number of values in its var dictionary
        for k in var:
            for v in range(var[k]):
                contents.append(k)

    def draw(self, draw_size):
        self.draw_size = draw_size
        global no_change
        no_change = False
        # randomly select n balls from list, n = draw_size
        if draw_size < len(self.contents):

            drawn_balls = random.sample(self.contents, draw_size)
            print(drawn_balls)
            # turn to set to remove duplicates
            set_drawn_balls = set(drawn_balls)
            global dict_drawn_balls
            dict_drawn_balls = {}
            for k in set_drawn_balls:
                dict_drawn_balls[k] = 0    # {'drawn_ball': 0 }

            for balls in drawn_balls:
                self.contents.remove(balls)
                dict_drawn_balls[balls] += 1
        else:
            drawn_balls = contents
            no_change = True
            print('no success')
        return drawn_balls

    # method that given a Hat, and a dcitonary of expected balls (ie. {"blue":2, "red":1})
    # calculates a probabilty for n experiments
    # binomial ??


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_attempts = 0
    for experiment in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        copy_hat.draw(num_balls_drawn)
        matching_balls = 0
        if no_change:
            successful_attempts = num_experiments
            break
        # for the key in expected balls,
        # if the k is in balls drawn and they appear the same amount of times (check dictionary values),
        # add 1 to matching balls ( this keeps track of number of matches)
        # if num of matches are equal to expected,
        # this is a success
        for colour in expected_balls:
            if colour in dict_drawn_balls and dict_drawn_balls[colour] >= expected_balls[colour]:
                matching_balls += 1
        if matching_balls == len(expected_balls):
            successful_attempts += 1
    probability = successful_attempts/num_experiments
    return probability
