import random
import numpy as np

population_size = 20
mutation_rate = 0.01


def generateInitialPopulation(array_population_lenght):
    alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    array_strings = []

    # vai fazer N strings
    for i in range(population_size):
        array = []

        # vai fazer X iterações de forma que o tamanho da string seja igual a do usuario
        for j in range(array_population_lenght):
            letter = random.choice(alphabet)
            array.append(letter)
            string_concatenated = ''.join(array)
        array_strings.append(string_concatenated)

    print(array_strings)

    return array_strings


def defineFitnessArray(user_string, array_strings):
    # o valor de fitness é a quantidade de letras iguais que a string tem com a frase do usuario
    fitness = []

    # percorre cada string da população
    for string in array_strings:
        letters_equal = 0

        # percorre cada letra da string
        for i in range(len(string)):

            # se a string na posição i for igual a frase do usuario na posição i então fitness += 1
            if string[i] == user_string[i]:
                letters_equal += 1

        fitness.append(letters_equal)

    print(fitness)
    return fitness


def crossover(parent1, parent2):
    # escolhe um ponto de corte aleatório
    crossover_point = random.randint(1, len(parent1) - 1)

    # realiza o crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    # retorna os dois filhos gerados
    return child1, child2


def chanceMutation(son1, son2):
    # inicializa os filhos mutados
    mutated_son1 = ''
    mutated_son2 = ''

    for char in son1:
        if random.uniform(0, 1) < mutation_rate:
            mutated_son1 += random.choice(
                "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            mutated_son1 += char

    for char in son2:
        if random.uniform(0, 1) < mutation_rate:
            mutated_son2 += random.choice(
                "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            mutated_son2 += char

    return mutated_son1, mutated_son2


def checkHighestFitness(array_fitness):
    highest_fitness = 0
    index_highest_fitness = 0
    for i, fitnessScore in enumerate(array_fitness):
        if fitnessScore > highest_fitness:
            highest_fitness = fitnessScore
            index_highest_fitness = i

    return highest_fitness, index_highest_fitness


def tournamentSelection(array_string, array_fitness):
    # obter os índices dos dois maiores valores fitness
    top_indices = np.argsort(array_fitness)[-2:]

    # obter as duas palavras correspondentes
    parent1 = array_string[top_indices[0]]
    parent2 = array_string[top_indices[1]]

    return parent1, parent2


def removeTheWeakest(son1, son2, array_string, array_fitness):
    # Obter índices das duas strings com piores valores fitness
    weakest_indices = np.argsort(array_fitness)[:2]

    # Remover as duas strings com piores valores fitness
    array_string = np.delete(array_string, weakest_indices)

    # Remover os dois piores valores fitness
    array_fitness = np.delete(array_fitness, weakest_indices)

    # Adicionar os dois novos filhos no lugar das removidas
    array_string = np.insert(array_string, weakest_indices[1], son1)
    array_string = np.insert(array_string, weakest_indices[0], son2)

    return array_string
