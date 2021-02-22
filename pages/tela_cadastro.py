import os, time
from models import usuario
from utils import validate

def validaInputs(function):
  while(True):
    try:
      function
      break
    except Exception as error:
      print(error)
      return False

def telaCadastro():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("***************************************")
  print("             Açai Universo             ")
  print("Bem vindo a melhor acaiteria da cidade!")
  print("---------------------------------------")
  print("Cadastre-se para continuar!")
  while(True):
    nome = input("Digite seu nome: ")
    if(validaInputs(nome, validate.validaName) == False):
      continue
    else:
      while(True):
        telefone = input("Digite seu Número:")
        if(validaInputs(telefone, validate.validaTelefone) == False):
          continue
        else:
          while(True):
            email = input("Digite seu email: ")
            if(validaInputs(email, validate.validaEmail) == False):
              continue
  senha = ""
  while(True):
    senha = input("Digite sua senha:")
    confirmar_senha = input("Confirme sua senha:")
    if(senha == confirmar_senha):
      break
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("As senhas não condizem digite novamente:/")
  validaInputs(senha, validate.validaSenha)