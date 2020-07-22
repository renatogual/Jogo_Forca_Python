# Importando a biblioteca random para escolher a palavra aleatóriamente da lista de palavras.txt
import random

# Tabuleiro
lista_tabuleiro = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Forca:
    # Declaração das variaveis auxiliares e de controle
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.lista = []
        self.count = 0
        self.count2 = 0
        self.count_letra_certa = []
        self.count_letra_errada = []

    # Escolhe uma palavra aleatória do arquivo "palavras.txt" para ser utilizada no Jogo
    def escolha_palavra(self):
        with open("palavras.txt", "r") as f:
            palavra_escolhida = f.readlines()
        return palavra_escolhida[random.randint(0, len(palavra_escolhida))].strip()

    # Mostra o status do tabuleiro
    def mostra_tabuleiro(self):
        numero = self.count2
        return self.tabuleiro[numero]

    # Mostra a quantidade de letras que a palavra escolhida possui
    def mostra_palavra(self):
        self.palavra = [x for x in self.escolha_palavra()] #Aqui é onde a palavra escolhida é separada letra a letra
        while self.count < len(self.palavra): #Aqui é onde é criado o tabuleiro das letras a serem descobertos da palavra
            for i in self.palavra:
                self.count += 1
                self.lista.append("_")

        return self.lista

    # Verifica se a letra digitada como parametro existe na palavra ou não
    def verifica_letra(self, letra):
        self.letra = letra
        if letra in self.palavra:
            for i in range(0, len(self.palavra)):
                if self.palavra[i] == letra: #Caso a letra exista na palavra, verifica em qual indice ela esta para ser adicionada
                    self.lista[i] = letra
            self.count_letra_certa.append(letra)
        else:
            self.count_letra_errada.append(letra)
            self.count2 += 1

    # Verifica se o jogo foi vencido ou perdido
    def status_jogo(self):
        if self.lista == self.palavra:
            print("Parabens, você venceu o jogo!")
            return False
        elif self.count2 == 6:
            print("Game Over!")
            print("A palavra certa era: ", self.escolha_palavra())
            return False


# Enquanto o jogo não tiver terminado, mostra o status do tabuleiro e faz a leitura da letra
if __name__ == "__main__":
    val = Forca(lista_tabuleiro) # Instancia o objeto val na classe Forca
    while True:
        print(val.mostra_tabuleiro())
        print("Palavra: ",*val.mostra_palavra()) # O asterisco nos nomes descompactam a lista, para mostrar apenas os valores sem as aspas e virgulas
        print("Letras certas: ", *val.count_letra_certa)
        print("Letras erradas: ", *val.count_letra_errada)
        letra = input("Digite uma letra: ")
        val.verifica_letra(letra)
        val.status_jogo()



        




        
        