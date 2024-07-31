#5 - Altere o valor do atributo nome para 'Bistrô'.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

print(f'O restaurante {restaurante_praca.nome}.')