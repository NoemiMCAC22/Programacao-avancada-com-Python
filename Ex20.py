# -*- coding: utf-8 -*-

from sys import exit

nif = list((input('Insira seu NIF: ')))
nif2 = [] 
for i in range(len(nif)):
    nif2.append(int(nif[i]))
   
if len(nif2) != 9:
    print('NIF inválido, numero de digitos incorreto')
    exit()

else:
    n9 = nif2[8] 
    n8 = nif2[7] * 2
    n7 = nif2[6] * 3
    n6 = nif2[5] * 4
    n5 = nif2[4] * 5
    n4 = nif2[3] * 6
    n3 = nif2[2] * 7
    n2 = nif2[1] * 8
    n1 = nif2[0] * 9
    conf_controlo = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9) % 11
if conf_controlo == 0 or conf_controlo == 1:
    num_controlo = 0
else:
    num_controlo = 11 - conf_controlo
if n9 == num_controlo:
    print('NIF VÁLIDO')
else:
    print('NIF INVÁLIDO')

