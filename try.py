from blackjack import blackjack
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    wealth = []

    for i in range(10000):
        bj = blackjack()
        for _ in range(100):
            bj.play()
        # print(bj.winner[0]/sum(bj.winner), bj.winner[1]/sum(bj.winner))
        # print(bj.wealth)
        wealth.append(bj.wealth)
    plt.hist(wealth, bins=100)
    plt.show()

    mean = np.mean(wealth)
    variance = np.var(wealth)
    wealth = np.array(wealth)
    bias = np.sum(((wealth-mean)/np.sqrt(variance))**3)
    print(f"mean:{mean}")
    print(f"variance:{variance}")
    print(f"bias:{bias}")