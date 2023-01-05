print('='*5, 'DESAFIO 18', '='*5)

import math
a = float(input('insira o ângulo em graus: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('Para o ângulo \33[36m{}\33[m, temos o seno \33[34m{}\33[m, o coseno \33[34m{}\33[m e a tangente \33[34m{}\33[m'.format(a, sen, cos, tan))
