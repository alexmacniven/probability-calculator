import copy
import random
from functools import reduce
# Consider using the modules imported above.


class Hat:
    """The Hat class."""

    def __init__(self, **kwargs):
        self.contents: list = reduce(_extend, kwargs.items(), [])

    def draw(self, balls: int):
        if balls >= len(self.contents):
            return self.contents
        return [_pop_random(self.contents) for _ in range(balls)]


def _extend(a, b):
    a.extend([f"{b[0]}" for _ in range(b[1])])
    return a


def _pop_random(a):
    return a.pop(random.randint(0, len(a) - 1))


def _drawn_list_to_dict(a):

    def _func(a, b):
        if b in a.keys():
            a[b] += 1
        else:
            a[b] = 1
        return a

    return reduce(_func, a, {})


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    def _resolve_draw(a, b) -> bool:
        return a and b[1] <= drawn_dict.get(b[0], -1)

    success: int = 0
    for _ in range(num_experiments):
        new_hat: Hat = copy.deepcopy(hat)
        drawn_list: list = new_hat.draw(num_balls_drawn)
        drawn_dict: dict = _drawn_list_to_dict(drawn_list)
        if reduce(_resolve_draw, expected_balls.items(), True):
            success += 1
    return success / num_experiments
