# exemplo: programa que sorteia cem dezenas para mega-sena

import random

ndezenas = 10
dezenas = set()
while len(dezenas) < ndezenas:
    numero = random.randint(1, 60)
    dezenas.add(numero)
print(dezenas)
