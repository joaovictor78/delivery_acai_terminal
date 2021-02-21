from pages import tela_login, tela_cadastro
import os

def telaInicial():
  print('**************************************')
  print('            Açai Universo             ')
  print('      O melhor açai da cidade!        ')
  print('**************************************')
  print('1 - Login')
  print('2 - Cadastrar')
<<<<<<< HEAD
  while True:
    try:
      option = input("Escolha uma das opções acima para continuar: ")  
      if(option == "1"):
        tela_login.telaLogin()
        os.system('cls' if os.name == 'nt' else 'clear')
        telaInicial()
      elif(option == "2"):
        tela_cadastro.telaCadastro()
        os.system('cls' if os.name == 'nt' else 'clear')
        telaInicial()
      else:
        print("Opção inavalida, tente novamente")
        continue
      break
    except ValueError:
      print("Ocorreu um erro com o tipo de dado informado, tente novamente")
      continue
=======
  option = input("Escolha uma das opções acima para continuar: ")
  if(option == "1"):
    tela_login.telaLogin()
    os.system('cls' if os.name == 'nt' else 'clear')
    telaInicial()
  elif(option == "2"):
    tela_cadastro.telaCadastro()
    os.system('cls' if os.name == 'nt' else 'clear')
    telaInicial()
>>>>>>> fa417a1494b0a841a8df50ed673c50389a782151
