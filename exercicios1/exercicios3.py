#3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

ativo = 'ativo' if restaurante_praca.ativo else 'falso'
print(f'O restaurante {restaurante_praca.nome} está com o status {ativo}.')