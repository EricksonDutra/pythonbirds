class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    erickson = Pessoa(nome='Erickson')
    ramao = Pessoa(erickson, nome='Ramão')
    print(Pessoa.cumprimentar(erickson))
    print(id(erickson))
    print(erickson.cumprimentar())
    print(erickson.nome)
    print(erickson.idade)
    for filho in ramao.filhos:
        print('Os filhos de ' + ramao.nome + ' são: ' + filho.nome)

