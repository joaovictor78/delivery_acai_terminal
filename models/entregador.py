from models import usuario

class Entregador(usuario.Usuario):
  def __init__(self,telefone,lista_pedido):
    self.telefone = telefone
    self.lista_pedido = []
  def setStatusEntrega(self, idpedido, status):
    self.idpedido = idpedido
    self.status = status
