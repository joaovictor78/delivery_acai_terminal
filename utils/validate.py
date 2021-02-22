import re

def validaEmail(email):
  if(re.search("^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", email) == None):
    raise Exception("Formato de email incorreto!") 

def validaName(name):
  if(len(name) == 0):
    raise Exception("Nome não pode ser nulo!")
  elif(len(name) < 3):
    raise Exception("Nome não pode ser menor que 3 caracteres!")

def validaTelefone(phone):
  if(len(phone) == 0):
    raise Exception("O número de telefone não pode ser nulo!")
  elif(len(phone) != 8 and len(phone) != 9):
    raise Exception("O número de telefone tem que ter 8 ou 9 dígitos")

def validaSenha(password):
  if(len(password) == 0):
    raise Exception("A senha não pode ser nulo!")
  elif(len(password) < 6):
    raise Exception("A senha tem que ter mais de 6 caracteres")
  elif(len(password) > 15):
    raise Exception("A senha tem que ter mais de 15 caracteres")