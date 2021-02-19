from models import usuario, estoque_produto
class Administrador(usuario.Usuario):
  def __init__(self):
    self.lista_pedidos = []
    self.lista_usuarios = []
    self.estoque_produto = estoque_produto.EstoqueProduto()
  def listaPedidos(self):
    return self.lista_pedidos
  def setStatusPedido(self, idpedidos, status):
    self.idpedidos = idpedidos
    self.status = status
  def adicionarProduto(self, produto):
    self.estoque_produto.append(produto)
    
  def removerProduto(self,idproduto):
    self.estoque_produto.remove(idproduto) 
  
  def editarProduto(self, produto, index):
    self.estoque_produto.insert(index, produto)
  def editarPermissoesUsuario(self, index_usuario, usuario):
    self.lista_usuarios.insert(index_usuario, usuario)
  def removerUsuario(self, keyusuario):
    self.lista_usuarios.remove(keyusuario)
