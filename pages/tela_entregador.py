import os
pedido = None
def telaEntregador():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Bem vindo ao nosso sistema de entregas 🚚")
  print("Pedidos pendentes: ")
  if(pedido != None):
    for meu_pedido in pedido:
      print(meu_pedido.listaProdutos)
  else:
    print("Nenhum pedido realizado")