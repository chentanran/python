import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# import pizza
# from pizza import pizzaName
# from pizza import pizzaName as pizs
from pizza import *

# piz = pizza.pizzaName()
# piz = pizs()
piz = pizzaName()
print(piz)