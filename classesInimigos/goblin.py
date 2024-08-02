from inimigo import Inimigo
import random

class Goblin (Inimigo):
    def __init__(self, nome, hp=80, danoRecebido_Inimigo = 0, estamina = 80, vivo=True):
        super().__init__(nome, hp, danoRecebido_Inimigo)
        self.vivo = vivo
        self.estamina = estamina

    def apunhalar(self):
        if self.estamina >= 20:
            dano = 20
            self.estamina -= 20
            print (f"{self.nome} usa o ataque 'Apunhalar' e causa {dano} ao jogador!")
            return dano
        else:
            print (f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/80")
            return 0

    def atacarAlet(self):
        ataques = [self.apunhalar, self.ataque]
        ataqueEscolhido = random.choice(ataques)
        dano = ataqueEscolhido()  # Chama o ataque escolhido e obtém o dano
        return dano

