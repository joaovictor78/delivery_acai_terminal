import json
class Usuario(object):
  id_counter = 0
  def __init__(self):
    self.id= Usuario.id_counter
    Usuario.id_counter += 1
    self.nome = ""
    self.foto = ""
    self.email = ""
    self.telefone = ""
    self.senha = ""
    self.endereco = ""
    self.permissao = 0
    
  def fazerLogin(self,email,senha):
    countError = 0
    countAccont = 0
    usuarios = open('bd_fake/usuarios.txt', 'r')
    for user in usuarios:
      countAccont += 1
      usuarioModel =  json.loads(user)
      email_user = usuarioModel["email"]
      email.split(' ')
      email_user.split(' ')
      senha_user = usuarioModel["senha"]
      role = usuarioModel["role"]
      if (email == email_user and senha == senha_user ):
        print("acesso autorizado")
        self.email = email
        self.senha = senha
        self.nome = usuarioModel["nome"]
        if (role == 1):
          return 1
        elif(role == 2):
          return 2
        elif(role == 3):
          return 3
        break
      else:
        countError += 1
    if(countAccont == countError):
      print("acesso negado")
      raise(Exception("Usuario ou senha invalidos!"))
      return None
    
  def fazerLogout(self):
    self.email = None
    self.senha = None
  def registrarConta(self,nome,email, senha, telefone):
    role = 3
    usuarios = open('bd_fake/usuarios.txt', 'a', newline="")
    dadosUsuario = ' \"email": \"{}\", \"senha\": \"{}\", \"nome\": \"{}\", \"role": {}, \"telefone\" : \"{}\"'.format(email, senha, nome, role, telefone)
    usuarioJson = "{" + dadosUsuario + "}"
    print(usuarioJson)
    usuarios.write(usuarioJson + "\n")
    self.nome = nome
    self.email = email
    self.senha = senha
    self.telefone = telefone
    
  def editarConta(self,nome,email,senha, foto):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.foto = foto
    