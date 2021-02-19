import os
from models import usuario
def telaCadastro():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("*************************************")
  print("             Açai Universo            ")
  print("Bem vindo a melhor acaiteria da cidade!")
  print("--------------------------------------")
  print("Cadastre-se para continuar!")
  senha = ""
  nome = input("Digite seu nome: ")
  telefone = input("Digite seu Número:")
  email = input("Digite seu email: ")
  while(True):
    senha = input("Digite sua senha:")
    confirmar_senha = input("Confirme sua senha:")
    if(senha == confirmar_senha):
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("As senhas não condizem digite novamente:/")
  usuario.Usuario().registrarConta(nome, email, senha, telefone)