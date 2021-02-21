from models import pedido, item_pedido
from pages import tela_entregador
from utils import cardapio, adicionarprodutos

def telaCliente(minhaConta):
  meu_pedido = pedido.Pedido()
  novo_produto = "S"
  while(novo_produto == "S"):
    item = item_pedido.ItemPedido()
    cardapio.getCardapio()
    meu_pedido = adicionarprodutos.adicionarProduto(item)
    novo_produto = input("Deseja adicionar mais algum produto? S/N ").upper()
    while(novo_produto != "S" and novo_produto != "N"):
      print("Você inseriu uma resposta inválida, tente novamente!")
      novo_produto = input("Deseja adicionar mais algum produto? S/N ").upper()
      if(novo_produto == "S" or novo_produto == "N"):
        break
    if(novo_produto == "N"):
      for item in meu_pedido.listaProdutos:
        qtd = item.quantidade
        preco = item.produto.preco_produto
        precoTotal = preco * qtd
        meu_pedido.precoTotal += precoTotal
      tela_entregador.pedido = meu_pedido
      minhaConta.fazerPedido(meu_pedido)
  