import random


class blackjack:
    def __init__(self):
        self.piles = self.new_piles()
        self.winner = [0, 0]
        self.wealth = 0

    def new_piles(self):
        new_piles = []
        for i in range(1, 10):
            new_piles.extend([i] * 4)
        for i in range(10, 14):
            new_piles.extend([10] * 4)
        random.shuffle(new_piles)
        self.piles = new_piles
        return new_piles

    def play(self):
        dealer = []
        player = []
        self.take_poker(player)
        self.take_poker(player)
        self.take_poker(dealer)
        self.take_poker(dealer)

        if player == [1,1]\
                or player == [8,8]\
                or (player == [9,9] and dealer[0] in [2,3,4,5,6,8,9])\
                or (player == [7,7] and dealer[0] in [2,3,4,5,6,7])\
                or (player == [6,6] and dealer[0] in [2,3,4,5,6])\
                or (player == [4,4] and dealer[0] in [5,6])\
                or (player == [3,3] and dealer[0] in [2,3,4,5,6,7])\
                or (player == [2,2] and dealer[0] in [2,3,4,5,6,7]):
            split1, split2 = [player[0]], [player[1]]

            while self.count_point(split1) < 17:
                if self.should_stand(split1, dealer[0]):
                    break
                self.take_poker(split1)

            while self.count_point(split2) < 17:
                if self.should_stand(split2, dealer[0]):
                    break
                self.take_poker(split2)

            while self.count_point(dealer) < 17 or self.soft(dealer, 17):
                self.take_poker(dealer)

            self.judge_result(dealer, split1, self.bets(split1[:2], dealer[0]))
            self.judge_result(dealer, split2, self.bets(split2[:2], dealer[0]))
        else:
            # player hits
            while self.count_point(player) < 17:
                # choose times to stand
                if self.should_stand(player, dealer[0]):
                    break
                self.take_poker(player)

            # dealer hits
            while self.count_point(dealer) < 17:
                self.take_poker(dealer)

            self.judge_result(dealer, player, self.bets(player[:2], dealer[0]))

    def judge_result(self, dealer, player, bets):
        if self.count_point(player) > 21:
            self.winner[0] += 1
            self.wealth -= bets
        elif self.count_point(dealer) > 21:
            self.winner[1] += 1
            self.wealth += bets
        elif self.count_point(player) < self.count_point(dealer):
            self.winner[0] += 1
            self.wealth -= bets
        elif self.count_point(player) > self.count_point(dealer):
            self.winner[1] += 1
            self.wealth += bets

    def take_poker(self, person):
        person.append(random.choice(self.piles))

    @staticmethod
    def count_point(person):
        if 1 in person and sum(person) + 10 <= 21:
            return sum(person) + 10
        else:
            return sum(person)

    @staticmethod
    def hard(person, point):
        return True if sum(person) == point else False

    def soft(self, person, point):
        return True if (self.count_point(person) == point) and (not self.hard(person, point)) else False

    def bets(self, player, upcard, money=100):
        if self.soft(player, 19) and upcard == 6\
                or self.soft(player, 18) and upcard in range(2, 7)\
                or self.soft(player, 17) and upcard in range(3, 7)\
                or self.soft(player, 16) and upcard in range(4, 7)\
                or self.soft(player, 15) and upcard in range(4, 7)\
                or self.soft(player, 14) and upcard in range(5, 7)\
                or self.soft(player, 13) and upcard in range(5, 7):
            return 2*money
        return money

    def should_stand(self, player, upcard):
        if self.hard(player, 16) and upcard in range(2, 7) \
                or self.hard(player, 15) and upcard in range(2, 7) \
                or self.hard(player, 14) and upcard in range(2, 7) \
                or self.hard(player, 13) and upcard in range(2, 7) \
                or self.hard(player, 12) and upcard in range(4, 7):
            return True
        return False


if __name__ == '__main__':
    pass