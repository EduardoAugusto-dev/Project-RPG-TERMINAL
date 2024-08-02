import random

class Inimigo:
    def __init__(self, nome, hp=100, danoRecebido_Inimigo=0, vivo=True):
        self.nome = nome
        self.vivo = True
        self.hp = hp
        self.danoRecebido_Inimigo = danoRecebido_Inimigo
        self.estamina = 0
        self.mana = 0

    def receberDanoInimigo(self,DanoRecebido_Inimigo):
        if DanoRecebido_Inimigo < 0:
            DanoRecebido_Inimigo = 0

        self.hp -= DanoRecebido_Inimigo
        if self.hp <= 0:
            self.hp = 0
        print (f"{self.nome} recebeu {DanoRecebido_Inimigo} de dano. HP atual : {self.hp}")
    
    def ataque(self):
        dano = 10
        print(f"{self.nome} usa o ataque básico e causa {dano} de dano.")
        return dano

    def defender_dano(self, dano):
        self.danoRecebido = 0
        alet = random.randint(1, 10)

        if 1 <= alet <= 7:
            self.danoRecebido = dano * 0.5
            self.hp -= self.danoRecebido
            if self.hp < 0:
                self.hp = 0
            print(f"O {self.nome} fez uma defesa normal e recebeu {self.danoRecebido} de dano.")
        elif 8 <= alet <= 10:
            self.danoRecebido = 0
            print(f"O {self.nome} realizou uma defesa perfeita e não recebeu dano.")