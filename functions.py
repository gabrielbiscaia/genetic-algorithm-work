import random
import numpy as np
import random

# configurações inicias
population_size = 50
mutation_rate = 0.2
max_generations = 10000


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


def randomSelection(array_string):
    # pega aleatoriamente 2 individuos do array_string
    parent1 = random.choice(array_string)
    parent2 = random.choice(array_string)

    while parent1 == '':
        parent1 = random.choice(array_string)

    # se os 2 pais forem iguais ele pega outro pai2
    while parent2 == '' or parent1 == parent2:
        parent2 = random.choice(array_string)

    return parent1, parent2


def removeTheWeakest(son1, son2, array_string, array_fitness):
    # Obter índices das duas strings com piores valores fitness
    weakest_indices = np.argsort(array_fitness)[:2]

    # Remover as duas strings com piores valores fitness
    array_string = np.delete(array_string, weakest_indices)

    # Remover os dois piores valores fitness
    array_fitness = np.delete(array_fitness, weakest_indices)

    # Adicionar os dois novos filhos no lugar das removidas
    if (len(array_string) <= weakest_indices[1]):
        array_string = np.append(array_string, "")

    array_string = np.insert(array_string, weakest_indices[1], son1)

    if (len(array_string) <= weakest_indices[0]):
        array_string = np.append(array_string, "")

    array_string = np.insert(array_string, weakest_indices[0], son2)

    return array_string


def mainWithTournament(user_string):
    current_generation = 0

    # pega o tamanho da string que o usuario digitou
    max_length_string = len(user_string)

    # gera a populção inicial de frases
    array_string = generateInitialPopulation(max_length_string)

    # retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
    array_fitness = defineFitnessArray(user_string, array_string)

    # retorna qual é o maior valor do fitness e o index desse maior valor
    highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)

    # enquanto a palavra não for igual a do usuário e enquanto a geração atual não for igual ao máximo de gerações vai rodar o código baixo
    while (highest_fitness != max_length_string) and (current_generation != max_generations):

        # seleciona os melhores pais através da seleção de torneio
        parent1, parent2 = tournamentSelection(array_string, array_fitness)

        # faz o crossover dos pais e gera dois filhos
        son1, son2 = crossover(parent1, parent2)

        # ve se algum dos dois filhos tem alguma letra mutada
        son1, son2 = chanceMutation(son1, son2)

        # atualiza a população com os 2 novos filhos removendo as 2 strings com piores fitness
        array_string = removeTheWeakest(
            son1, son2, array_string, array_fitness)

        # retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
        array_fitness = defineFitnessArray(user_string, array_string)

        # confere qual é o maior fitness do "arrayfitness"
        highest_fitness, index_highest_fitness = checkHighestFitness(
            array_fitness)
        current_generation += 1
        print("Geração ", current_generation, ", melhor string: ",
              array_string[index_highest_fitness])

    return array_string, index_highest_fitness, current_generation


def mainWithRandom(user_string):
    current_generation = 0

    # pega o tamanho da string que o usuario digitou
    max_length_string = len(user_string)

    # gera a populção inicial de frases
    array_string = generateInitialPopulation(max_length_string)

    # retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
    array_fitness = defineFitnessArray(user_string, array_string)

    # retorna qual é o maior valor do fitness e o index desse maior valor
    highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)

    # enquanto a palavra não for igual a do usuário e enquanto a geração atual não for igual ao máximo de gerações vai rodar o código baixo
    while (highest_fitness != max_length_string) and (current_generation != max_generations):

        # seleciona os melhores pais através da seleção de torneio
        parent1, parent2 = randomSelection(array_string)

        # faz o crossover dos pais e gera dois filhos
        son1, son2 = crossover(parent1, parent2)

        # ve se algum dos dois filhos tem alguma letra mutada
        son1, son2 = chanceMutation(son1, son2)

        # atualiza a população com os 2 novos filhos removendo as 2 strings com piores fitness
        array_string = removeTheWeakest(
            son1, son2, array_string, array_fitness)

        # retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
        array_fitness = defineFitnessArray(user_string, array_string)

        # confere qual é o maior fitness do "arrayfitness"
        highest_fitness, index_highest_fitness = checkHighestFitness(
            array_fitness)
        current_generation += 1
        print("Geração ", current_generation, ", melhor string: ",
              array_string[index_highest_fitness])

    return array_string, index_highest_fitness, current_generation
