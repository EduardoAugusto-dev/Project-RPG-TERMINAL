from inimigo import Inimigo
import random

class Dragao(Inimigo):
    def __init__(self, nome, hp=100, danoRecebido_Inimigo=0, estamina = 100, vivo=True):
        super().__init__(nome, hp, danoRecebido_Inimigo)
        self.vivo = vivo
        self.estamina = estamina

    def rajadaVento(self):
        if self.estamina >= 35:
            dano = 25
            self.estamina -= 35
            print(f"{self.nome} usa o ataque 'Rajada de Vento', balançando suas asas e fazendo uma enorme rajada de vento. Isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/100")
            return 0
        
    def bolaFogo(self):
        if self.estamina >= 50:
            dano = 40
            self.estamina -= 50
            print(f"{self.nome} usa o ataque 'Bola de fogo' e lança uma enorme bola de fogo. Isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/100")
            return 0

    def atacarAlet(self):
        ataques = [self.rajadaVento, self.bolaFogo, self.ataque]
        ataqueEscolhido = random.choice(ataques)
        dano = ataqueEscolhido()  # Chama o ataque escolhido e obtém o dano
        return dano