'''Refazendo o programa utilizando loço for.'''

n = int(input('Digite um número inteiro: '))
print('='*11)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('='*11)
