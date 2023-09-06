import copy
import numpy as np
import random
from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """


        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)
        # TODO (Additional: Learning curve)


        Q = 4
        next_generation = []
        for i in range (num_players):    #Q tornoment
            randoms = random.sample(range(0, len(players)), Q)
            max = randoms[0]
            for j in randoms:
                if players[max].fitness < players[j].fitness:
                    max = j
            next_generation.append(players[max])

        return next_generation



    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """


        first_generation = prev_players is None
        parents, next_generation = [], []

        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )

            Q = 4
            for i in range(num_players):  # Q tornoment
                randoms = random.sample(range(0, len(prev_players)), Q)
                max = randoms[0]
                for j in randoms:
                    if prev_players[max].fitness < prev_players[j].fitness:
                        max = j
                parents.append(prev_players[max])

            for i in range(int(len(parents)/2)):
                rand1 = random.randint(0, len(parents)-1)
                rand2 = random.randint(0, len(parents)-1)
                parent1 = parents[rand1]
                parent2 = parents[rand2]
                child1 = self.clone_player(parent1)
                child2 = self.clone_player(parent2)

                child1.nn.weight1 = parent1.nn.weight1
                child1.nn.weight2 = parent2.nn.weight2
                child1.nn.weight3 = parent1.nn.weight3
                child1.nn.weight4 = parent2.nn.weight4

                child2.nn.weight1 = parent2.nn.weight1
                child2.nn.weight2 = parent1.nn.weight2
                child2.nn.weight3 = parent2.nn.weight3
                child2.nn.weight4 = parent1.nn.weight4

                m1 = random.randint(1, 4)
                m2 = random.randint(1, 4)

                if m1 == 1:
                    child1.nn.weight1 = np.random.normal(size=(30, 3))
                elif m1 == 2:
                    child1.nn.weight2 = np.random.normal(size=(50, 30))
                elif m1 == 3:
                    child1.nn.weight3 = np.random.normal(size=(40, 50))
                else:
                    child1.nn.weight4 = np.random.normal(size=(8, 40))

                if m2 == 1:
                    child2.nn.weight1 = np.random.normal(size=(30, 3))
                elif m2 == 2:
                    child2.nn.weight2 = np.random.normal(size=(50, 30))
                elif m2 == 3:
                    child2.nn.weight3 = np.random.normal(size=(40, 50))
                else:
                    child2.nn.weight4 = np.random.normal(size=(8, 40))


                parents.append(child1)
                parents.append(child2)

                for i in range(num_players):  # Q tornoment
                    randoms = random.sample(range(0, len(parents)), Q)
                    max = randoms[0]
                    for j in randoms:
                        # print(parents[j].fitness)
                        if parents[max].fitness < parents[j].fitness:
                            max = j
                    next_generation.append(parents[max])

        sum, max, min= 0, 0, 10000
        for i in range (len(next_generation)):
            sum += next_generation[i].fitness
            if max < next_generation[i].fitness:
                max = next_generation[i].fitness
            if min > next_generation[i].fitness:
                min = next_generation[i].fitness

        avg = sum/len(next_generation)
        f = open("plot.txt", "a")

        f.write(str(max))
        f.write('\n')
        f.write(str(min))
        f.write('\n')
        f.write(str(avg))
        f.write('\n')

        f.close()


        return next_generation

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """

        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player