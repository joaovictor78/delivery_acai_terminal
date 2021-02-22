import os, time
from models import cliente
from pages import tela_admin, tela_cliente, tela_entregador

def telaLogin():
  role = None
  resp = "S"
  while(resp == "S"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*********************************")
    print("             Açai Universo            ")
    print("Bem vindo a melhor acaiteria da cidade!")
    print("--------------------------------------")
    print("Digite email e senha para continuar...")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    minhaConta = cliente.Cliente()
    try:
      role = minhaConta.fazerLogin(email, senha)
    except Exception as error:
      print(error)
    if(role != None):
      if(role == 1):
        tela_admin.telaAdmin()
      elif(role == 2):
        tela_entregador.telaEntregador()
      elif(role == 3):
<<<<<<< HEAD
        tela_cliente.telaCliente(minhaConta)
=======
        tela_cliente.telaCliente(minhaConta)
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_inicial.telaInicial()
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("****** Ocorreu um erro ao logar *****")
      resp =  input("Deseja tentar novamente? S/N")
    

>>>>>>> origin/developer_project
