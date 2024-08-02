from player import Player

class Mago(Player):
    def __init__(self, nome, sexo, danoRecebido=0, vivo=True, hp=100, mana = 100):
        super().__init__(nome, sexo, danoRecebido, vivo, hp)
        self.mana = mana

    def tiroMagico(self):
        if self.mana >= 15:
            dano = 20
            self.mana -= 15
            print(f"{self.nome} usa o ataque 'Tiro Mágico' e desfere vários tiros azuis contra o inimigo, isso causa {dano} de dano! (mana restante: {self.mana}/100 )")
            return dano
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente {self.mana}/100")
            return 0
    
    def RajadaMagica(self):
        if self.mana >=50:
            dano = 50
            self.mana -= 50
            print(f"{self.nome} usa o ataque 'Rajada Mágica das trevas' e desfere uma enorme massa negra com seu cajado contra o inimigo. Isso causa {dano} de dano! (mana restante: {self.mana}/100 )")
            return dano
        else:
            print(f"{self.nome} falha ao usar o ataque, mana insuficiente (mana: {self.mana}/100)")
            return 0


