import random
import string

population_size = 20
max_generations = 10000
mutation_rate = 0.01


def generateInitialPopulation(array_population_lenght):
    alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arrays = []

    # vai fazer N arrays
    for i in range(population_size):
        array = []

        # vai fazer X iterações de forma que o tamanho da string seja igual a do usuario
        for j in range(array_population_lenght):
            letter = random.choice(alphabet)
            array.append(letter)
            string_concatenated = ''.join(array)
        arrays.append(string_concatenated)

    print(arrays)

    return arrays


def defineFitnessArray(user_array, arrays):
    # o valor de fitness é a quantidade de letras iguais que a string tem com a frase do usuario
    fitness = []

    # percorre cada array da população
    for string in arrays:
        letters_equal = 0

        # percorre cada letra do array
        for i in range(len(string)):

            # se a string na posição i for igual a frase do usuario na posição i então fitness += 1
            if string[i] == user_array[i]:
                letters_equal += 1

        fitness.append(letters_equal)

    print(fitness)
    return fitness


def crossover():
    print("teste")


def chanceMutation():
    print("teste")
