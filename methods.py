text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard

dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen

book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially

unchanged
"""

vowels = {
}

for vowel in 'AEIOU':
    vowels[vowel] = 0

for character in text:
    if character.upper() == 'A':
        vowels['A'] += 1
    if character.upper() == 'E':
        vowels['E'] += 1
    if character.upper() == 'I':
        vowels['I'] += 1
    if character.upper() == 'O':
        vowels['O'] += 1
    if character.upper() == 'U':
        vowels['U'] += 1

for vowel, count in vowels.items():
    print(f'Há {count} letras {vowel} no texto.')



state_and_capital = {
    'São Paulo': 'São Paulo',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Ceará': 'Fortaleza',
    'Mato Grosso': 'Cuiabá',
    'Minas Gerais': 'Belo Horizonte',
}

wants_to_continue = True
rounds = 0
hits = 0

for state, capital in state_and_capital.items():
    if not wants_to_continue:
        break
    rounds += 1
    print(f'\n-> Qual a capital de {state}? ')

    reply = input('Sua resposta: ')
    if reply.upper() == capital.upper():
        hits += 1
        print('Resposta certa!')
    else:
        print(f'Resposta invalida! O correto seria {capital}')

    while True:
        option = input('Deseja continuar [S/N]? ').lower()
        if option not in ['s', 'n']:
            print('Responda "s" para sim ou "n" para não.')
            continue
        elif option == 'n':
            wants_to_continue = False
        break

porc = hits / rounds * 100

print(f'Você acertou {hits} de {rounds}')
print(f'Porcentagem de acertos: {porc:0.2f}%')



values = list(range(10))
greater_than_five = []

for value in values:
    if value > 5:
        greater_than_five.append(value)

print(greater_than_five)

greater_than_five = [
    value # RESULTADO
    for value in values # para cada ELEMENTO in SEQUÊNCIA
    if value > 5 # se CONDIÇÃO
]
print(greater_than_five)








