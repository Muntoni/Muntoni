import copy
import random

class Hat:

  def __init__(self, **dict):
    print(dict)
    self.contents = list()
    for key, value in dict.items():
      i = 0
      while i < value:
        self.contents.append(key)
        i = i + 1
    print(self.contents)

  def draw(self, n):
    if n > len(self.contents):
      return self.contents
    drawn_balls = list()
    for i in range(n):
      drawn = self.contents.pop(int(random.random() * len(self.contents)))
      drawn_balls.append(drawn)
    return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if color in expected_copy:
        expected_copy[color] -= 1

    if all(x <= 0 for x in expected_copy.values()):
      count += 1

  return count / num_experiments
