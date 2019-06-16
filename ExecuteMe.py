import random
import gym
from Strategy import Strategy

env = gym.make('MountainCar-v0')
# env.reset()

Strategy = Strategy()

numOfTries = 0
while True:
    Strategy.newSession()
    print("------------------")
    print("The best already:")
    print("best reward: "+ Strategy.bestReward.__str__())
    print("best strategy :")
    print(Strategy.bestStrategyInNumbers.__str__())
    print()
    print("try number: " + numOfTries.__str__())

    numOfTries = numOfTries + 1
    env.reset()
    reward = 0
    for i in range(1000):
        env.render()
        observation, rewardTmp, done, info = env.step(Strategy.nextStep())

        maxFarPoint = -2
        #update maxFarPoint
        if (observation[0]) > maxFarPoint:
            maxFarPoint = observation[0]

        #update reward
        reward = reward - 1
        # print(observation, reward, done, info )

        if done or i == 999:
            reward = reward + maxFarPoint * 100
            Strategy.updateStrategy(reward)

            print("The reward in this try :" + reward.__str__())
            print("The strategy in this try :")
            print(Strategy.currentStrategyInNumbers.__str__())
            break


