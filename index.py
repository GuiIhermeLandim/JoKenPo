# JoKenPô
from random import randint
from time import sleep
print('=-'*10)
print('{:-^40}'.format(' \033[1:31mJo\033[1:33mKen\033[1:34mPô\033[m! '))
print('-='*10)
escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('''Escolha uma jogada
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA
 Sua escolha: '''))
if jogador < 0 or jogador > 2: # Jogador escolheu uma opção Inválida!
    print('Por favor, selecione uma opção válida na próxima vez. ')
elif jogador >= 0 and jogador <=2:
    print(' JO')
    sleep(1)
    print(' KEN')
    sleep(2)
    print(' PO !!!')
    print('O computador escolheu {}'.format(escolhas[computador]))
    print('O jogador escolheu {}'.format(escolhas[jogador]))
    if jogador == 0: # Jogador escolheu PEDRA
        if computador == 0:
            print('Empate')
        elif computador == 1:
            print('Computador Venceu')
        elif computador == 2:
            print('Jogador Venceu')
    elif jogador == 1:  # Jogador escolheu PAPEL
        if computador == 0:
            print('Jogador Venceu')
        elif computador == 1:
            print('Empate')
        elif computador == 2:
            print('Computador Venceu')
    elif jogador == 2: # Jogador escolheu TESOURA
        if computador == 0:
            print('Computador Venceu')
        elif computador == 1:
            print('Jogador Venceu')
        elif computador == 2:
            print('Empate')
