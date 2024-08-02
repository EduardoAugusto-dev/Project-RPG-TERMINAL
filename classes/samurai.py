from player import Player

class Samurai(Player):
    def __init__(self, nome, sexo, danoRecebido=0, vivo=True, hp=100, estamina = 120):
        super().__init__(nome, sexo, danoRecebido, vivo, hp)
        self.estamina = estamina

    def estocada(self):
        if self.estamina >= 20:
            dano = 20
            self.estamina -= 20
            print(f"{self.nome} usa o ataque 'Estocada' e perfura o inimigo. Isso causa {dano} de dano! (Estamina restante: {self.estamina}/120 )")
            return dano
        else:
            print(f"{self.nome} falha ao usar o ataque, estamina insuficiente! {self.estamina}/120")
            return 0 

    def decepar(self):
        if self.estamina >=50:
            dano = 250
            self.estamina -= 50
            print(f"{self.nome} usa o ataque 'Decepar' e arranca o braço de seu inimigo fora. Isso causa {dano} de dano! (Estamina restante: {self.estamina}/120 )")
            return dano
        else:
            print (f"{self.nome} falha ao usar o ataque, instamina insuficiente! (estamina: {self.estamina}/120)")
            return 0