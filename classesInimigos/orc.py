from inimigo import Inimigo
import random

class Orc(Inimigo):
    def __init__(self, nome, hp=150, danoRecebido_Inimigo=0, estamina = 120, vivo=True):
        super().__init__(nome, hp, danoRecebido_Inimigo)
        self.vivo = vivo
        self.estamina = estamina
    
    def rugir(self):
        if self.estamina >= 30:
            dano = 20
            self.estamina -= 30
            print(f"{self.nome} usa o ataque 'Rugido', fazendo com que tudo se estremeça. Isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/120")
            return 0
    
    def ataquePorrete(self):
        if self.estamina >= 50:
            dano = 45
            self.estamina -= 50
            print(f"{self.nome} usa o ataque 'Pancada com Porrete' e derruba o jogador no chão. Isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/120")
            return 0

    def atacarAlet(self):
        ataques = [self.rugir, self.ataquePorrete, self.ataque]
        ataqueEscolhido = random.choice(ataques)
        dano = ataqueEscolhido()  # Chama o ataque escolhido e obtém o dano
        return dano
