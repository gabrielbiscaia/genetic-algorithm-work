import random

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


def crossover():
    print("teste")


def chanceMutation():
    print("teste")


def checkHighestFitness(array_fitness):
    highest_fitness = 0
    index_highest_fitness = 0
    for i, fitnessScore in enumerate(array_fitness):
        if fitnessScore > highest_fitness:
            highest_fitness = fitnessScore
            index_highest_fitness = i

    return highest_fitness,


def tournamentSelection(array_string):


def removeTheWeakest(son1, son2):
