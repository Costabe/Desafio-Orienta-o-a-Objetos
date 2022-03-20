# reference: https://miro.medium.com/max/372/0*djgHYNHzUc4_E9E4.png

class Pizza:
    # Pizzaria
    def __init__(self, Sabor, quatro_queijos):
        # atributos
        self.Sabor = Sabor 
        self.quatro_queijos = quatro_queijos
        self.pedaco = 8
        self.Preparando = 10
    print(" ------------   🍕🍕 Welcome a Bonissima Pizza. melhor Pizza da Cidade  🍕 🍕 ------------ ")

    # metodos 
    def Pedido1(self): # <--- REFERENCIA A CLASSE DO OBJETO.
        self.Preparando  
        print('Recebendo Seu Pedido... ')
        print("O Sabor Escolhido Foi quatro_queijos 🧀🧀🧀🧀")
    
    def Pedido3(self):
        self.Preparando
        print("Montando seu Pedido 🧑‍🍳")

    def Pedido2(self):
        self.Preparando -= 10
        print('Organizando os ingredietes 🍅 🧀...')

# Funcao 
def mostrar_info_pizza(pizza):
    print("A Pizza de  " + pizza.quatro_queijos +
          " de quatro_queijos no tamanho L " + str(pizza.quatro_queijos) + 
          " Sera Fatiada em "                + str(pizza.Preparando) + " pedaco.")


if __name__ == "__main__":
    minha_pizza = Pizza("pizza" ,0)
    minha_pizza.Pedido1()
    minha_pizza.Pedido2()
    print('Etapa 1')
    minha_pizza.Pedido3()
    print('Etapa 2')
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    print('Etapa 3')
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    minha_pizza.Pedido2()
    print("Sua Pizza agora Esta no Forno 🔥🔥.")
    print('Etapa 4')
    for iteration in range(1):
       print("Esta Quase Pronto..")
       for iteration in range(1):
           print("Sua Pizza Esta Sendo Saindo Do Forno em ...3")
           print("Sua Pizza Esta Sendo Saindo Do Forno em ...2")
           print("Sua Pizza Esta Sendo Saindo Do Forno em ...1")
           print("Sua Pizza Esta Pronta Enjoy sua Pizza 😋🍕🍕...")