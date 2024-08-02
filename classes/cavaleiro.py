from player import Player
from inimigo import Inimigo

class Cavaleiro (Player):
    def __init__(self, nome, sexo, danoRecebido=0, vivo=True, hp=100, estamina = 100):
        super().__init__(nome, sexo, danoRecebido, vivo, hp)
        self.estamina = estamina

    def corteLimpo(self):
        if self.estamina >= 10:
            dano = 25
            self.estamina -= 10
            print (f"{self.nome} usa o ataque 'Corte Limpo' e o inimigo recebe um grande corte no peito. Isso causa {dano} de dano (estamina restante: {self.estamina}/100 )")
            return dano
        else:
            print (f"{self.nome} falha ao usar o ataque, estamina insuficiente (estamina: {self.estamina}/100)")
            return 0 

    def corteCarregado(self):
        if self.estamina >= 30:
            dano = 40
            self.estamina -= 30
            print (f"{self.nome} usa o ataque 'Corte Carregado' e o inimigo é esmagado pela sua espada. Isso causa {dano} (estamina restante: {self.estamina}/100 )")
            return dano
        else:
            print (f"{self.nome} falha ao usar o ataque, estamina insuficiente (estamina: {self.estamina}/100)")
            return 0
