#4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

categoria = restaurante_praca.categoria
print(f'A categoria do restaurante {restaurante_praca.nome} é {categoria}.')