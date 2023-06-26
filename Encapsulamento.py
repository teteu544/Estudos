class Animal:
    def __init__(self):
        pass

    def locomove(self):
        pass

    
  #--Agora, desejamos criar classes derivadas da classe Animal que implementam o método locomove de formas diferentes. Um modo de fazer isso é o mostrado no exemplo abaixo:

class Peixe(Animal):

    def locomove(self):
        print("Um peixe nada.")


class Elefante(Animal):

    def locomove(self):
        print("Um elefante anda.")


class Passaro(Animal):

    def locomove(self):
        print("Um pássaro voa.")


#--Com isso, dependendo do tipo de animal com o qual estivermos lidando, o método locomove apresentará um comportamento diferente. Por exemplo, considere o código abaixo, no qual invocamos o método locomove para diferentes tipos de animais:

peixe = Peixe()
elefante = Elefante()
passaro = Passaro()

peixe.locomove()
elefante.locomove()
passaro.locomove()




#Um peixe nada.
#Um elefante anda.
#Um pássaro voa.
# Note que, ao usar herança da forma mostrada acima, podemos implementar uma interface específica (o método locomove, por exemplo) usando objetos de classes distintas, ou seja, estamos implementando polimorfismo.
