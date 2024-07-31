#1-Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

print(vars(restaurante_praca))#lista valores em forma de dicionário