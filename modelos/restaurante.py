class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))#utilizar o dir() quando não conhecer a classe.
print(vars(restaurante_praca))#lista valores em forma de dicionário