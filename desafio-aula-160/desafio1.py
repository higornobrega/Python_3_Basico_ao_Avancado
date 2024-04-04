import copy

# Exercícios
# 1 - Aumente os preços dos produtos a seguir em 10%
# 2 - Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 3 - Ordene os produtos por nome decrescente (do maior para menor)
# 4 - Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 5 - Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# 1
for p in produtos:
    p['preco'] = p['preco']*1.10

# 2
novos_produtos = copy.deepcopy(produtos)

# 3
ordenacao = sorted(produtos, key=lambda x: x['nome'], reverse=True)

# 4
produtos_ordenados_por_nome = copy.deepcopy(ordenacao)

# 5
ordenacao2 = sorted(
    produtos_ordenados_por_nome, key=lambda x: x['preco'])

# 6
produtos_ordenados_por_preco = copy.deepcopy(ordenacao2)
