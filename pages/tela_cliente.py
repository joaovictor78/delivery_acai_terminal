import os, json
from models import produtos, pedido, item_pedido
from pages import tela_entregador
from utils import cardapio
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
    item.produto = meu_produto
    item.quantidade = int(quantidade_pedido)
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
  
  