#9 - Imprima no console o nome e a categoria da instância restaurante_praca.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

ativo = 'ativo' if restaurante_praca.ativo else 'falso'
print(f'O restaurante {restaurante_praca.nome} está com o status {ativo}.')
