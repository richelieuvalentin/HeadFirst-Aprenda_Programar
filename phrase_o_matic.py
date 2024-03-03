
#Phrase-O_Matic

#Informe ao Python que utitlizaremos funcionalidades aleatórias importando o módulo random

import random

#Faça 3 listas: Uma de verbos(verbs), uma de adjeitvos(adjectives) e uma de substantivos(nouns)

verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crows-sourced', '24/7', 'Lean-in', '30.000 foot' ]
adjectives = ['A/B Tested', 'Freemiun', 'Hyperlocal', 'Siloed', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']
nouns = ['Early adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']

#Escolha um verbo, um adjetivo e um substantivo de cada lista

verb = random.choice(verbs)
adjecitve = random.choice(adjectives)
noun = random.choice(nouns)

#Agora crie a frase "somando" as palavras

phrase = verb +' '+ adjecitve +' '+ noun

#Faça o output da frase

print(phrase)
