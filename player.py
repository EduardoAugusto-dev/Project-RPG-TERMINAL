import random

class Player:
    def __init__(self, nome, sexo, danoRecebido=0, vivo=True, hp = 100, mana = 0, estamina = 0, pocoes = 5):
        self.nome = nome
        self.sexo = sexo
        self.danoRecebido = danoRecebido
        self.vivo = True
        self.hp = 100
        self.mana = mana
        self.estamina = estamina
        self.pocoes = pocoes
      

    def receberDano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0
        print (f"{self.nome} recebeu {dano} de dano. HP atual : {self.hp}")

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
            print(f"O jogador fez uma defesa normal e recebeu {self.danoRecebido} de dano.")
        elif 8 <= alet <= 10:
            self.danoRecebido = 0
            print("O jogador realizou uma defesa perfeita e não recebeu dano.")

    def usarPocao(self):
        cura = 50
        if self.pocoes > 0:
            self.hp = min(100, self.hp + cura)
            self.pocoes -= 1
            print (f"{self.nome} usa uma poção e se cura {cura} de hp! (hp atual: {self.hp}/100)")
        else:
            print ("Você ja usou todas as poções que tinha!")

        
