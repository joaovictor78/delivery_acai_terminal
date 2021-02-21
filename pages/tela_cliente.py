import json
from models import pedido, item_pedido
from utils import cardapio, adicionarprodutos
from pages import tela_entregador
import time

class Pedido:
  lista_produtos = []
def telaCliente(minhaConta):
  meu_pedido =  pedido.Pedido()
  novo_produto = "S"
  while(novo_produto == "S"):
    item = item_pedido.ItemPedido()
    produtos = cardapio.getCardapio()
    tipoAcai = input("Escolha um dos nossos formatos de açai e aproveite:):")
    for produto in produtos:
      produtoModel =  json.loads(produto)
      meu_produto = adicionarprodutos.adicionarProduto(tipoAcai, produtoModel)
      item.produto = meu_produto[0]
      item.quantidade = int(meu_produto[1])
      meu_pedido.listaProdutos.append(item)
    novo_produto = input("Deseja adicionar mais algum produto? S/N ")
    if(novo_produto == "N"):
      for item in meu_pedido.listaProdutos:
        qtd = item.quantidade
        preco = item.produto.preco_produto
        precoTotal = preco * qtd
        meu_pedido.precoTotal += precoTotal
      tela_entregador.pedido = meu_pedido
      minhaConta.fazerPedido(meu_pedido)
 