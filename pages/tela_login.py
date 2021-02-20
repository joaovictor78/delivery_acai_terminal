import os
from models import cliente
from pages import tela_admin, tela_cliente, tela_entregador

def telaLogin():
  resp = "S"
  while(resp == "S"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*************************************")
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
       print("********** Ocorreu um erro ao logar Pults *********")
       print(error)
       resp =  input("Deseja tentar novamente? S/N")
    if(resp != "N"):
      if(role == 1):
          tela_admin.telaAdmin()
      elif(role == 2):
          tela_entregador.telaEntregador()
      elif(role == 3):
          tela_cliente.telaCliente(minhaConta)
    