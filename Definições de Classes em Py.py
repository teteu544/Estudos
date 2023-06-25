#-- Definições de Classes em Py

#- Exemplos "pessoas"



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade   





    #-- Class é a definição de classe em Python
    # Para uma criação de método usamos DEF
    # O constructor é um método reservado chamado __init__
    # já o SELF é obrigatório , onde definem por nós
    # Nisso definimos o import
    # from pessoa import Pessoa 





    