### A Geringonça ###

# Cria uma lista e define seus itens
characters = ['L', 'A', 'B', 'E', 'L', 'Y']

#Inicializa a variavel output com uma string vazia
output = ''

#inicializa a variavel lenght recebendo o valor do tamanho da lista characters
lenght = len(characters)

#Inicializa a variavel i e atribui a ela o valor zero
i = 0

#Enquanto a variavel i for menor que lenght os valores das variáveis output e i são atualizados dentro do laço
while (i < lenght):
    output = output + characters[i] 
    i = i + 1

#Atualiza o valor da variavel lenght multiplicando seu valor por -1
lenght = lenght * -1

#Atualiza o valor da variavel i
i = -2

while (i >= lenght):
    output = output + characters[i]
    i = i - 1

print(output)

