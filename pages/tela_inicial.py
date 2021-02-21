from pages import tela_login, tela_cadastro
import os

def telaInicial():
  print('**************************************')
  print('            Açai Universo             ')
  print('      O melhor açai da cidade!        ')
  print('**************************************')
  print('1 - Login')
  print('2 - Cadastrar')
  option = input("Escolha uma das opções acima para continuar: ")
  if(option == "1"):
    tela_login.telaLogin()
    os.system('cls' if os.name == 'nt' else 'clear')
    telaInicial()
  elif(option == "2"):
    tela_cadastro.telaCadastro()
    os.system('cls' if os.name == 'nt' else 'clear')
    telaInicial() 