import random
import numpy as np
import matplotlib.pyplot as plt
from blackjack import blackjack


if __name__ == '__main__':

    piles = blackjack().piles
    final_point = []

    for _ in range(10000):
        dealer = blackjack()
        random.shuffle(piles)
        dealer.take_poker(random.choice(piles))
        dealer.take_poker(random.choice(piles))
        while dealer.point < 17:
            dealer.take_poker(random.choice(piles))
        final_point.append(dealer.point)
    print(f'average of final points: {np.mean(final_point)}')
    print(f'dealer points <=21 vs >21: {np.sum(np.array(final_point)<=21)} vs {np.sum(np.array(final_point)>21)}')
    plt.scatter(np.linspace(1, 10000, 10000), final_point)
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.show()

    plt.hist(final_point)
    plt.show()
