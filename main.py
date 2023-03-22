from functions import generateInitialPopulation, defineFitnessArray, crossover, chanceMutation

print("A partir das letras do alfabeto")
user_array = input("Digite uma frase: ")
# pega o tamanho do array que o usuario digitou
max_lengeth_array = len(user_array)
# gera a populção inicial de frases
arrays_population = generateInitialPopulation(max_lengeth_array)
defineFitnessArray(user_array, arrays_population)
