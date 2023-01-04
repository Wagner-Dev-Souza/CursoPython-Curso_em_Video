print('='*5, 'DESAFIO 18', '='*5)

import math
a = float(input('insira o ângulo em graus: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('Para o ângulo {}, temos o seno {}, o coseno {} e a tangente {}'.format(a, sen, cos, tan))
