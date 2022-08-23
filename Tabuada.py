'''Melhorando o programa utilizando loço while infinito.O programa será interrompido quando o número solicitado for negativo.'''

print('-=' * 20)
print('{:^40}'.format('TABUADA 3.0'))
print('-=' * 20)
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n<=0:
        break
    print('='*40)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('='*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
