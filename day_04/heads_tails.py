# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

import random

random_num = random.randint(0, 1)

if random_num == 0:
    print("Heads")
else:
    print("Tails")