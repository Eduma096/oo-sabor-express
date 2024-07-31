#6 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
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

categoria = restaurante_praca.categoria
print(f'A categoria do restaurante {restaurante_pizza.nome} é {categoria}.')