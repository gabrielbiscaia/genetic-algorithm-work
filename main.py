from functions import generateInitialPopulation, defineFitnessArray, crossover, chanceMutation, checkHighestFitness

print("A partir das letras do alfabeto")
user_string = input("Digite uma frase: ")

# pega o tamanho da string que o usuario digitou
max_length_string = len(user_string)

# gera a populção inicial de frases
string_population = generateInitialPopulation(max_length_string)

# retorna o array com todos os scores do fitness sendo o maior score possível o tamanho da string informada pelo usuario
array_fitness = defineFitnessArray(user_string, string_population)

# retorna qual é o maior valor do fitness
highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)

max_generations = 10000
current_generation = 0

# enquanto a palavra não for igual a do usuário e enquanto a geração atual não for igual ao máximo de gerações vai rodar o código baixo
while (highest_fitness != max_length_string) and (current_generation != max_generations):

    highest_fitness, index_highest_fitness = checkHighestFitness(array_fitness)
    current_generation += 1
    print("Geração ", current_generation, ", melhor string: ",
          string_population[index_highest_fitness])
