class Produto(object):
  id_counter = 0
  def __init__(self):
    self.id = Produto.id_counter
    Produto.id_counter += 1
    self.descricao = ""
    self.ingredientes = ""
  def setAtributos(self, preco, descricao, ingredientes):
    self.id_produto = id
    self.preco_produto = preco
    self.descricao_produto = descricao
    self.ingredientes_produto = ingredientes
    self.precoTotal = preco 
  def calcPrecoTotal(self, preco, quantidade):
    self.quantidade = quantidade
    self.precoTotal = float(preco) * float(quantidade)

  def getAtributos(self):
    print("Quantidade de itens: " + str(self.quantidade))
    print("Preço Total: "  + "R$" + str(self.precoTotal))
    print('Descrição: ' + str(self.descricao_produto))
    print("****************************************************")
    print('Ingredientes: ' + str(self.ingredientes_produto))
  