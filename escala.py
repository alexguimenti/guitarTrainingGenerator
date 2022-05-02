import random
from random import randrange, shuffle
import array

notas_com_acidentes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notas_naturais = ["C", "D", "E", "F", "G", "A", "B"]
escala1 = ["Maior", "Menor"]
escala2 = ["Normal", "Pentatonica"]
desenho = range(4)
shuffle(notas_naturais)
shuffle(notas_com_acidentes)


print('\n\n')
print(f'Nota: {random.choice(notas_com_acidentes)}\n')
print(f'Escala: {random.choice(escala1)} {random.choice(escala2)}\n')
print(f'Posicao: {randrange(5)+1}\n')
print(f'Sequencia: {notas_naturais}, {random.choice(notas_naturais)}\n')
print(f'Sequencia: {notas_com_acidentes}\n')
# print(f'Corda: {randrange(3)+1}')
print('\n\n')
