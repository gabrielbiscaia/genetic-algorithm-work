from functions import mainWithTournment, mainWithRandom

print("A partir das letras do alfabeto")
user_string = input("Digite uma frase: ")

print("\nQual configuração voce prefere?")
print("1 - Seleção por torneio")
print("2 - Seleção aleatória")
user_choice = input("Digite o número da escolha: ")

array_string = []
index_highest_fitness = 0
current_generation = 0

if user_choice == '1':
    array_string, index_highest_fitness, current_generation = mainWithTournment(
        user_string)
elif user_choice == '2':
    array_string, index_highest_fitness, current_generation = mainWithRandom(
        user_string)

print("\n**************************************************")
print("Algoritmo finalizado, melhor string: ",
      array_string[index_highest_fitness],
      "\nEncontrado na geração:", current_generation)
print("**************************************************")
