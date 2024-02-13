import importlib  # Para re-importar um módulo

import modulo2

print('Arquivo modulo1 - Esse módulo é o ', __name__)

# Re-importando módulos

for i in range(10):
    importlib.reload(modulo2)
    print(i)

print('fim')
