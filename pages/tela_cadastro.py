import os
from models import usuario
from utils import validate

def validaInputs(message, function):
  while(True):
    try:
      data = input(message)
      function(data)
      return data
      break
    except Exception as error:
      print(error)

def telaCadastro():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("***************************************")
  print("             Açai Universo             ")
  print("Bem vindo a melhor acaiteria da cidade!")
  print("---------------------------------------")
  print("Cadastre-se para continuar!")
  nome = validaInputs("Digite seu nome: ", validate.validaName)
  telefone = validaInputs("Digite seu Número: ", validate.validaTelefone)
  email = validaInputs("Digite seu email: ", validate.validaEmail)
  senha = validaInputs("Digite sua senha: ", validate.validaSenha)
  usuario.Usuario().registrarConta(nome, email, senha, telefone)