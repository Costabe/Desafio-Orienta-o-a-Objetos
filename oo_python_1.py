# reference: https://miro.medium.com/max/372/0*djgHYNHzUc4_E9E4.png

class Carro:
    # contrutor
    def __init__(self, marca, ano_fabricacao):
        # atributos
        self.marca = marca 
        self.ano_fabricacao = ano_fabricacao
        self.velocidade = 0.0

    # metodos 
    def acelerar(self): # <--- REFERENCIA A CLASSE DO OBJETO.
        self.velocidade  += 10
        print("aumentando a velocidade.")
    
    def freiar(self):
        self.velocidade -= 10
        print("Diminuindo a velocidade.")

# Funcao 
def mostrar_info_carro(carro):
    print("O carro de marca " + carro.marca +
          " e ano de fabricacao" + str(carro.ano_fabricacao) + 
          " esta com velocidade "+ str(carro.velocidade) + "km/h.")


if __name__ == "__main__":
    meu_carro = Carro("Ford", 2018)
    meu_carro.acelerar()
    meu_carro.freiar()
    print('Etapa 1')
    mostrar_info_carro(meu_carro)
    print('Etapa 2')
    meu_carro.acelerar()
    meu_carro.freiar()
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.freiar()
    mostrar_info_carro(meu_carro)
    print('Etapa 3')
    for iteration in range (4):
        meu_carro.acelerar()
    mostrar_info_carro(meu_carro)

    carro_do_irmao = Carro("Tesla", 2021)
    print('Etapa 4')
    for iteration in range(3):
       meu_carro.acelerar()
       for iteration in range(3):
           carro_do_irmao.acelerar()
    mostrar_info_carro(meu_carro)
    mostrar_info_carro(carro_do_irmao)