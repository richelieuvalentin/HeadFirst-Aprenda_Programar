#### Pedra, Papel e Tesoura ####

# Importa funcionalidades aleatórias
import random

winner = ''

# Cria uma variável para receber um valor aleatório entre 0, 1 e 2
random_choice = random.randint(0, 2)

# Verifica se random_choice é igual a 0 se for atribuia a ela a string "Pedra"
if random_choice == 0:
    computer_choice = 'Pedra'

# Verifica se random_choice é igual a 1 se for atribuia a ela a string "Papel"
elif random_choice == 1:
    computer_choice = 'Papel'

# Caso as duas condições anteriores não seja verdadeiras atribue a computer_choice a string "Tesoura"
else:
    computer_choice = 'Tesoura'

user_choice = ''
while (user_choice != 'Pedra' and
    user_choice != 'Papel' and
    user_choice != 'Tesoura'):
    user_choice = input('Pedra, Papel ou Tesoura???')


if computer_choice == user_choice:
    winner = 'Empate'
elif computer_choice == 'Papel' and user_choice == 'Pedra':
    winner = 'Computer'
elif computer_choice == 'Papel' and user_choice == 'Tesoura':
    winner = 'Computer'
elif computer_choice == 'Tesoura' and user_choice == 'Papel':
    winner = 'Computer'
else: 
    winner = 'User'



if winner == 'Empate':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won, I chose', computer_choice + '.')

