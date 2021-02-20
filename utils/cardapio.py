import os
import json

def getCardapio():
  os.system('cls' if os.name == 'nt' else 'clear')
  produtosDisponiveis = open("bd_fake/produtos.txt","r")
  print("----------------------------------------")
  print("Açai Universo - O melhor açai da cidade!")
  print("----------------------------------------")
  print('**********Nosso Cardapio************')
  for produto in produtosDisponiveis:
    produtoModel =  json.loads(produto)
    print(str(produtoModel["id"]) + " - Açai " + str(produtoModel["tipo"]))
  produtos_disponiveis = open("bd_fake/produtos.txt","r")
  return produtos_disponiveis