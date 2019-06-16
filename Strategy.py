import random


class Strategy:
    bestStrategyInNumbers = []
    bestStrategyInSteps = []
    currentStrategyInNumbers = []
    currentStrategyInSteps = []
    bestReward = -1000000

    def __init__(self):
        self.bestStrategyInNumbers = self.random_num_of_steps_strategy()
        self.bestStrategyInSteps = self.convert_strategy_to_steps(self.bestStrategyInNumbers)

    def random_num_of_steps_strategy(self):
        strategy = []
        for i in range(100):
            # strategy.append(random.randint(0, 50))
            strategy.append(0)

        return strategy

    def convert_strategy_to_steps(self, strategyInNumners):
        strategyInSteps = []
        direction = 2
        for number in strategyInNumners:
            for i in range(number):
                strategyInSteps.append(direction)

            if direction == 0:
                direction = 2
            else:
                direction = 0

        return strategyInSteps

    def newSession(self):
        self.currentStrategyInNumbers = self.bestStrategyInNumbers.copy()
        epsilon = 1/50
        for i in range(self.currentStrategyInNumbers.__len__()):
            rndm = random.random()  # random a number between 0 to 1
            if rndm < epsilon:
                self.currentStrategyInNumbers[i] = random.randint(0, 50)

        self.currentStrategyInSteps = self.convert_strategy_to_steps(self.currentStrategyInNumbers)

    def nextStep(self):
        if self.currentStrategyInSteps.__len__() == 0:
            return 1
        else:
            return self.currentStrategyInSteps.pop()


    def updateStrategy(self,reward):
        if reward > self.bestReward:
            self.bestReward = reward
            self.bestStrategyInNumbers = self.currentStrategyInNumbers
            self.bestStrategyInSteps = self.currentStrategyInSteps



