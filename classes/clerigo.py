from player import Player

class Clerigo(Player):
    def __init__(self, nome, sexo, danoRecebido=0, vivo=True, hp=100, mana = 120):
        super().__init__(nome, sexo, danoRecebido, vivo, hp)
        self.mana = mana

    def curar(self):
        cura = 30
        if self.mana >=15:
            self.hp += 30
            self.mana -= 15
        if self.hp >= 100:
            self.hp = 100
            self.mana -= 15


            print(f"{self.nome} usa 'Cura' e se restaura {cura} de hp! (mana restante: {self.mana}/120 )")
            return cura
        else:
            print(f"{self.nome} falha ao usar a cura, mana insuficiente (mana: {self.mana}/120)")
    
    def conjurarRaio(self):
        if self.mana >= 40:
            dano = 50
            self.mana -= 40
            print(f"{self.nome} usa o ataque 'Conjurar Raio' e arremessa em seu inimigo. Isso causa {dano} de dano! (mana restante: {self.mana}/120 )")
            return dano
        else:
            print(f"{self.nome} falha ao usar o ataque 'Conjurar Raio', mana insuficiente (mana: {self.mana}/120) ")
            return 0