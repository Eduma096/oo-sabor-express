#8 - Mude o estado da instância restaurante_pizza para ativo.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

ativo = 'ativo' if restaurante_pizza.ativo else 'falso'
print(f'O restaurante {restaurante_pizza.nome} está com o status {ativo}.')