from pages import tela_login, tela_cadastro

def telaInicial():
  print('**************************************')
  print('            Açai Universo     ')
  print('      O melhor açai da cidade!')
  print('**************************************')
  print('1 - Login')
  print('2 - Cadastrar')
  option = input("Escolha uma das opções acima para continuar: ")
  if(option == "1"):
    tela_login.telaLogin()
  elif(option == "2"):
    tela_cadastro.telaCadastro()
  