from models import usuario
import json
class Endereco():
  def __init__(self,bairro,rua,numero_casa,cep,complemento,cidade,telefone):
    self.bairro = bairro
    self.rua = rua 
    self.numero_casa = numero_casa
    self.cep = cep
    self.complemento = complemento
    self.cidade = cidade
    self.telefone = telefone
    
class Cliente(usuario.Usuario):

  def __init__(self):
    self.meupedido = []
  def fazerPedido(self,pedido):
    ItemPedido = {}
    Produto = {}
    Pedido = {}
    lista_produtos = []
    for p in pedido.listaProdutos:
      Produto["preco"] = p.produto.preco_produto
      Produto["cobertura"] = p.produto.coberturaSelecionada
      ItemPedido["quantidade"] = p.quantidade
      ItemPedido["produto"] = Produto
      lista_produtos.append(ItemPedido)
    Pedido["itens_pedido"] =  lista_produtos
    pedidoJson = json.dumps(Pedido)  
    print(pedidoJson)
    pedidos = open('bd_fake/pedidos.txt', 'a')
    pedidos.write(pedidoJson + "\n")
    print("Seu pedido foi realizado com sucesso!")
  def listaMeusPedidos(self):
    return self.meuspedidos

  def acompanharPedido(self,id_pedido):
    self.id_pedido

  def insere_endereco(self,bairro,rua,numero_casa,cep,complemento,cidade,telefone):
    self.endereco.append(Endereco(bairro,rua,numero_casa,cep,complemento,cidade,telefone))
  