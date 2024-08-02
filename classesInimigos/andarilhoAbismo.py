from inimigo import Inimigo
import random

class AndarilhoAbismo(Inimigo):
    def __init__(self, nome, hp=250, danoRecebido_Inimigo=0, mana = 100, estamina = 100, vivo=True):
        super().__init__(nome, hp, danoRecebido_Inimigo)
        self.vivo = vivo
        self.estamina = estamina
        self.mana = mana
    
    def puloEspada(self):
        if self.estamina >= 35:
            dano = 40
            self.estamina -= 35
            print(f"{self.nome} usa o ataque 'Giro Mortal', ele pula girando várias vezes no ar e esmaga o jogador com sua enorme espada. Isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.estamina}/100")
            return 0
        
    def conjurarAbismo(self):
        if self.mana >= 60:
            dano = 65
            self.mana -= 60
            print(f"{self.nome} usa o ataque 'Conjurar Forças do Abismo', com isso tudo se escurece e uma massa negra envolve o jogador e quase o consome, isso causa {dano} de dano!")
            return dano 
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.mana}/100")
            return 0
    def atacarAlet(self):
        ataques = [self.puloEspada, self.conjurarAbismo, self.ataque]
        ataqueEscolhido = random.choice(ataques)
        dano = ataqueEscolhido()
        return dano