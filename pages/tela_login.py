import os
from models import cliente
from pages import tela_admin, tela_cliente, tela_entregador, tela_inicial

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
      os.system('cls' if os.name == 'nt' else 'clear')
      print("****** Ocorreu um erro ao logar *****")
      print(error)
      resp =  input("Deseja tentar novamente? S/N ")
    if(role != None):
      if(role == 1):
        tela_admin.telaAdmin()
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_inicial.telaInicial()
      elif(role == 2):
        tela_entregador.telaEntregador()
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_inicial.telaInicial()
      elif(role == 3):
        tela_cliente.telaCliente(minhaConta)
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_inicial.telaInicial()
