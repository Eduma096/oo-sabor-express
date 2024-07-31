#2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

print(restaurante_praca.categoria)