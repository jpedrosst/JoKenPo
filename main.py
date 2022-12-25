from random import choice
from time import sleep
count = 0 # Definindo contador de vezes que o usuário ganhou
def jokenpo():
    print("===========================================\n")
    print(f'        \033[1;31mJô\033[m')
    sleep(0.7)
    print(f'                \033[1;32mKen\033[m')
    sleep(0.7)
    print(f'                        \033[1;33mPô\033[m\n')
    sleep(0.7)
    print("===========================================\n")


print(f'\n\t\t{"Bem vindo Jogador"}\n')
nome_player = str(input("Informe o seu nome jogador: ")).strip()
while True:
  print("-=" * 20)
  escolha = str(input(f'\t\t{nome_player} você quer jogar JoKenPô?\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\t\t\tDigite \033[1;32mSim\033[m ou \033[1;31mNão\033[m\n>>>>>>>>>>>>>> ')).lower().strip()
  if escolha == 'sim':
      pc_escolhas = ['pedra', 'papel', 'tesoura']
      pc_player = choice(pc_escolhas)
      while True:
        player = str(input("Escolha entre (Pedra / Papel / Tesoura): ")).lower().strip()
        if player == "pedra" or player == "papel" or player == "tesoura":
          break
      jokenpo()
      if player == pc_player:  ########################################### Verificando o Empate
          print(f'PC jogou: {pc_player}')
          print(f'Houve um \033[1;33mEMPATE\033[m, {player} empata com {pc_player}\n\n\n\n')
      elif (player == 'pedra' and pc_player == 'tesoura') or \
              (player == 'tesoura' and pc_player == 'papel') or \
              (player == 'papel' and pc_player == 'pedra'):  ############# Verificando possibilidades de vitórias
          print(f'PC jogou: {pc_player}')
          print(f'Você \033[1;32mGANHOU\033[m, {player} ganha de {pc_player}\n\n\n\n')
          count += 1
      else:  ############################################################# Verificando derrotas
          print(f'PC jogou: {pc_player}')
          print(f'Você \033[1;31mPERDEU\033[m, {pc_player} ganha de {player}')
  elif escolha == 'nao' or escolha == 'não':
      print('Tudo bem, deixa pra próxima!\n\n\n\n')
      break
  else:
    print("-=" * 20)
    print('Digite uma opção válida.\n\n\n\n')
if count == 0:
  print(f"Credo {nome_player} você não ganhou nenhuma vez, que vergonha!!")
elif 1 <= count <= 3:
  print(f"Boa {nome_player} você foi muito bem e ganhou do COMPUTADOR, {count} vezes.")
else:
  print(f"Wow {nome_player}, você simplesmente destruiu o game e ganhou do COMPUTADOR {count} vezes! Meus Parabéns !!!")
