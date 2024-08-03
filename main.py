from player import Player
from classes.mago import Mago
from classes.samurai import Samurai
from classes.clerigo import Clerigo
from classes.cavaleiro import Cavaleiro
from inimigo import Inimigo
from classesInimigos.orc import Orc
from classesInimigos.dragao import Dragao
from classesInimigos.goblin import Goblin
from classesInimigos.andarilhoAbismo import AndarilhoAbismo  # Corrigido o nome da classe para maiúsculo
import random
import os
import time

# Funções

def limpar_tela():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')

# Loop para sistema de confirmação
def confirmarClasse():
    while True:
        classePlayer = input("E agora o mais importante, escolha sua classe (Cavaleiro, Samurai, Mago e Clérigo): ").capitalize()
        if classePlayer in ['Cavaleiro', 'Samurai', 'Mago', 'Clérigo']:
            confirmar = input(f"Você tem certeza que sua classe é {classePlayer}? (Sim | Não): ").lower()
            if confirmar == 'sim':
                return classePlayer
            else:
                print("Como sua escolha foi não, escolha novamente.")
        else:
            print("Classe inválida, por favor escolha novamente entre: Cavaleiro, Samurai, Mago ou Clérigo.")

# Cria um inimigo aleatório
def criarInimigo(batalha_num):
    inimigos = [
        Goblin(nome="Goblin", vivo=True),
        Orc(nome="Orc", vivo=True),
        Dragao(nome="Dragão", vivo=True),
    ]
    return random.choice(inimigos)

# Sistema de batalha
def batalha(player, inimigo):
    while player.hp > 0 and inimigo.hp > 0:
        print(f"\nO player {player.nome} começa!")
        print("Escolha a sua ação:")
        print("1 - Atacar\n2 - Defender\n3 - Ataques Especiais\n4 - Usar Poção")
        acao = input("")

        if acao == '1':
            dano = player.ataque()
            inimigo.receberDanoInimigo(dano)
            time.sleep(3)
        elif acao == '2':
            dano = inimigo.ataque()
            player.defender_dano(dano)
            time.sleep(3)
        elif acao == '3':
            # Cavaleiro
            if isinstance(player, Cavaleiro):
                print("1 - Corte Limpo\n2 - Corte Carregado")
                especial = input("Escolha o ataque especial: ")
                if especial == '1':
                    dano = player.corteLimpo()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                elif especial == '2':
                    dano = player.corteCarregado()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                else:
                    print("Escolha inválida.")
                    continue
            # Mago
            elif isinstance(player, Mago):
                print("1 - Tiro Mágico\n2 - Rajada Mágica das Trevas")
                especial = input("Escolha o ataque especial: ")
                if especial == '1':
                    dano = player.tiroMagico()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                elif especial == '2':
                    dano = player.RajadaMagica()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                else:
                    print("Escolha inválida.")
                    continue
            # Clérigo
            elif isinstance(player, Clerigo):
                print("1 - Cura\n2 - Conjurar Raio")
                especial = input("Escolha o ataque especial: ")
                if especial == '1':
                    player.curar()
                    dano = 0
                    time.sleep(3)
                elif especial == '2':
                    dano = player.conjurarRaio()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                else:
                    print("Escolha inválida.")
                    continue
            # Samurai
            elif isinstance(player, Samurai):
                print("1 - Estocada\n2 - Decepar")
                especial = input("Escolha o ataque especial: ")
                if especial == '1':
                    dano = player.estocada()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                elif especial == '2':
                    dano = player.decepar()
                    inimigo.receberDanoInimigo(dano)
                    time.sleep(3)
                else:
                    print("Escolha inválida.")
                    continue
            else:
                print("Classe inválida. Tente novamente.")
                continue
        elif acao == '4':
            player.usarPocao()
            time.sleep(3)
        else:
            print("Escolha inválida, tente novamente.")

        if inimigo.hp > 0:
            dano = inimigo.atacarAlet()
            player.receberDano(dano)
            time.sleep(3)

        if player.hp <= 0:
            player.vivo = False
            print("Você foi derrotado!")
            time.sleep(5)
            break
        if inimigo.hp <= 0:
            if isinstance(player, Mago):
                player.mana += 100
            if player.mana >= 100:
                player.mana += 100
            if isinstance(player, Clerigo):
                player.mana += 120
            if player.mana >= 120:
                player.mana = 120
            if isinstance(player, Cavaleiro):
                player.estamina += 100
            if player.estamina >= 100:
                player.estamina = 100
            if isinstance(player, Samurai):
                player.estamina += 120
            if player.estamina >= 120:
                player.estamina = 120


            inimigo.vivo = False
            print(f"Você derrotou {inimigo.nome}!")
            time.sleep(3)
            print(f"O {player.nome} descansa após e batalha e recupera sua estamina ou mana e corre para próxima batalha!")
            time.sleep(3)
def iniciar():
    print("----------------------Bem-vindo à criação de personagem, é aqui onde sua jornada começa!----------------------")
    nome = input("Escolha o nome do seu personagem: ")

    while True:
        sexo = input("Escolha o seu sexo (Digite 'F' ou 'M'): ").upper()
        if sexo in ['F', 'M']:
            confirmar = input(f"Você tem certeza que seu personagem é {'feminino' if sexo == 'F' else 'masculino'}? (Sim | Não): ").lower()
            if confirmar == 'sim':
                break
            else:
                print("Como sua escolha foi não, faça sua escolha novamente.")
        else:
            print("Escolha inválida, por favor escolha 'F' para o sexo feminino e 'M' para o masculino.")

    classePlayer = confirmarClasse()

    if classePlayer == 'Mago':
        player = Mago(nome, sexo, danoRecebido=0, vivo=True, hp=100)
    elif classePlayer == 'Cavaleiro':
        player = Cavaleiro(nome, sexo, danoRecebido=0, vivo=True, hp=100)
    elif classePlayer == 'Clérigo':
        player = Clerigo(nome, sexo, danoRecebido=0, vivo=True, hp=100)
    elif classePlayer == 'Samurai':
        player = Samurai(nome, sexo, danoRecebido=0, vivo=True, hp=100)
    else:
        print("Classe inválida. Escolha entre Cavaleiro, Samurai, Mago ou Clérigo.")
        return

    print(f"Personagem criado com sucesso!\nSeu nome é {player.nome},\nseu sexo é {'Feminino' if player.sexo == 'F' else 'Masculino'}\ne sua classe é {classePlayer}.")
    print("Seu objetivo é chegar até um covil secreto cheio de tesouros. Para isso, você terá que enfrentar 10 inimigos que serão aleatórios (O último deles é um boss). Sua jornada começa AGORA!")

    time.sleep(10)

    # Exemplo de inicialização do sistema de batalha
    for batalha_num in range(9):
        limpar_tela()
        inimigo = criarInimigo(batalha_num)
        print(f"Inimigo {batalha_num + 1}: {inimigo.nome}")
        batalha(player, inimigo)
        if not player.vivo:
            break

        andarilho = AndarilhoAbismo(nome="Andarilho do Abismo", vivo=True)
    print(f"Batalha 10: {player.nome} enfrenta o chefe final {andarilho.nome}")
    batalha(player, andarilho)
    if andarilho.vivo == False:
        print ("Parabens você derrotou o grande Andarilho do Abismo! voce se provou um bravo guerreiro e recebeu os seus tesouros!")


if __name__ == "__main__":
    iniciar()
