name = input('qual é seu nome: ')
print(name)

year = int(input('qual sua idade? '))

print('o total de leta são: ' + str(len(name)))

print(f'Olá {name}! você tem {year} anos de idade.')

if year < 18:
    print('vc é menor de idede')

print('---INICIO---')
estou_com_fome = input('EStou com fome? (Digite "s" para sim): ') == 's'
tenho_comida = input('Tenho comida em casa? (Digite "s" para sim): ') == 's'

if estou_com_fome and not tenho_comida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

if estou_com_fome and tenho_comida:
    print('Preparar uma refeição')
    print('Comer a comida')

print('\n ---FIM---')


usuario_correto = 'Ronald'
senha_correta = 'PASSWORD'

user = input('qual o seu nome: ') == usuario_correto
password = input('qual sua senha: ') == senha_correta

if user and password:
    print(f'Acesso liberado para {user}!')
if user and not password:
    print(f'Senha incorreta do usuario {user}')
if not user:
    print(f'Usuario {user} não cadastrado!')


num_secret = 10
found = False


for _ in range(1):
    if not found:
        what_num_secret = int(input('Qual é o numero secreto?\n seu chute: '))
        if what_num_secret > num_secret:
            print('Chute alto!')
        elif what_num_secret < num_secret:
            print('Chute baixo!')
        else:
            print('Descobriu!')
            found = True

if found:
    print('Parabéns, você ganhou!!!')
else:
    print(f'Que pena, você perdeu! O numero secreto era {num_secret}')

clients = [('ronald', 'xxx', 'xxx@gmail.com'), ('lo', 'yyy', 'yyy@gmail.com')]

for name, cpf, email in clients:
    print(f'Cliente: {name}\nCPF: {cpf}\nEmail: {email} \n\n')

while True:
    opt = input('Escolha uma opção (1, 2) | "q" para sair: ')
    if opt == 'q':
        break
    elif opt not in ('1', '2'):
        print('Opção inválida!')
        continue
    print(f'Opção selecionada: {opt}')
print('Fim do programa!')

seq_number = range(10)

sum_n = 0
max_n = seq_number[0]
for v in seq_number:
    sum_n += v
    if v > max_n:
        max_n = v

med = sum_n / len(seq_number)
print(f'A soma dos valores {seq_number} é {sum_n}')
print(sum(seq_number))

print(f'A média dos valores {seq_number} é {sum_n}')
print(f'Valor máximo dos valores {seq_number} é {max_n}')
print(max(seq_number))

list1 = [1, 2, 6, 4, 1]
list2 = [6, 2, 8, 9, 6]

for i in list1:
    for j in list2:
        if i == j:
            print(f'Valor {i} aparece nas duas lista')

print('\n\n')

elem_comum = False
for i in list1:
    if elem_comum:
        break
    for j in list2:
        if i == j:
            elem_comum = True
            break

if elem_comum:
    print(f'lista {list1} e {list2} contem elemento em comum')
else:
    print(f'lista {list1} e {list2} NÃO contém elemento em comum')
