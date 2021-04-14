class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    ramao.sobrenome = 'Rolon'
    del ramao.filhos
    ramao.olhos = 1
    print(ramao.__dict__)
    print(erickson.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(erickson.olhos)
    print(ramao.olhos)
    print(id(Pessoa.olhos), id(erickson.olhos), id(ramao.olhos))
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), erickson.nome_e_atributos_de_classe())


