from functions import generateInitialPopulation, defineFitnessArray, crossover, chanceMutation, checkHighestFitness, tournamentSelection, removeTheWeakest

print("A partir das letras do alfabeto")
user_string = input("Digite uma frase: ")

# pega o tamanho da string que o usuario digitou
max_length_string = len(user_string)

# gera a populção inicial de frases
array_string = generateInitialPopulation(max_length_string)

# retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
array_fitness = defineFitnessArray(user_string, array_string)

# retorna qual é o maior valor do fitness e o index desse maior valor
highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)

max_generations = 10000
current_generation = 0

# enquanto a palavra não for igual a do usuário e enquanto a geração atual não for igual ao máximo de gerações vai rodar o código baixo
while (highest_fitness != max_length_string) and (current_generation != max_generations):

    # seleciona os melhores pais através da seleção de torneio
    parent1, parent2 = tournamentSelection(array_string, array_fitness)

    # faz o crossover dos pais e gera dois filhos
    son1, son2 = crossover(parent1, parent2)

    # ve se algum dos dois filhos tem alguma letra mutada
    son1, son2 = chanceMutation(son1, son2)

    # atualiza a população com os 2 novos filhos removendo as 2 strings com piores fitness
    array_string = removeTheWeakest(son1, son2, array_string, array_fitness)

    # retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
    array_fitness = defineFitnessArray(user_string, array_string)

    highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)
    current_generation += 1
    print("Geração ", current_generation, ", melhor string: ",
            array_string[index_highest_fitness])