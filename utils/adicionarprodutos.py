from models import produtos
from models import produtos, pedido, item_pedido
import json
meu_pedido = pedido.Pedido()
def adicionarProduto(item):
  tipoAcai = input("Escolha um dos nossos formatos de açai e aproveite:):")
  produtos_disponiveis = open("bd_fake/produtos.txt","r")
  for produto in produtos_disponiveis:
    produtoModel =  json.loads(produto)
    if (int(tipoAcai) == int(produtoModel["id"])):
      print("Você escolheu nosso delicioso açai {} :)".format(produtoModel["tipo"]))
      print("Tamanhos: ")
      counter = 0
      for tamanho in produtoModel["tamanhos"]:
        counter += 1
        print(str(counter) + " - " +str(tamanho) + "g")
      if(produtoModel["id"] == 1):
        tamanho = input("Escolha o tamanho: ")
        meu_produto = produtos.AcaiNaBarca(produtoModel["complementos"],   produtoModel["tamanhos"], produtoModel["coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"],   produtoModel["ingredientes"])
        print("Tipos de complementos:")
        counter = 0
        for complemento in produtoModel["complementos"]:
          counter +=1
          print(str(counter) + " - " + complemento)
        complemento_selecionado = input("Selecione um complemento:")
        meu_produto.escolherComplemento(int(complemento_selecionado))
        print("Tipos de coberturas:")
        counter = 0
        for cobertura in produtoModel["coberturas"]:
          counter +=1
          print(str(counter) + " - " + cobertura)
        cobertura_selecionada = input("Selecione uma cobertura: ")
        meu_produto.escolherCobertura(int(cobertura_selecionada))
        quantidade_pedido = input("Quantos açais você deseja? ")
      elif(produtoModel["id"] == 2):
        meu_produto = produtos.AcaiTigela(produtoModel["frutas"], produtoModel  ["tamanhos"], produtoModel["coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"],   produtoModel["ingredientes"])
        tamanho = input("Escolha o tamanho do seu açai: ")
        meu_produto.escolherTigela(int(tamanho))
        print("Hmm Exelente escolha! \nAgora vamos escolher as 3 frutas que irão   compor seu açaí na tigela. Ex: 1, 3, 4")
        resp = "S"
        adicionarFrutaExtra = False
        numeroDeFrutasExtras = 0
        counter = 0
        while(resp == "S"):
          print("Tipos de Frutas:")
          for frutas in produtoModel["frutas"]:
            counter += 1
            print(str(counter) + " - " + frutas)
          frutas_selecionadas = input("Escolha as frutas do seu açai: ")
          if(adicionarFrutaExtra == False):
            meu_produto.escolherFruta(frutas_selecionadas)
            resp = input("Deseja Adicionar mais frutas por apenas um adicional de 2   Reais? S/N ")
            while(resp == "S"):
              print("Tipos de Frutas:")
              counter = 0
              for frutas in produtoModel["frutas"]:
                counter += 1
                print(str(counter) + " - " + frutas)
              frutaExtraSelecionada = input("Selecione uma das frutas acima: ")
              index = int(frutaExtraSelecionada) - 1
              listFrutasAcaiTigela =  meu_produto.frutasExtras
              listFrutas = meu_produto.frutas
              if(listFrutas[index] in listFrutasAcaiTigela):
                print("Essa fruta já foi adicionada")
              else:
                numeroDeFrutasExtras = numeroDeFrutasExtras + 1
                meu_produto.frutasExtras.append(meu_produto.frutas[index])
                resp = input("Deseja adicionar mais alguma fruta? S/N ")
                if(resp == "N"):
                  meu_produto.acaiAddFrutaExtra(numeroDeFrutasExtras)
        counter = 0
        print("Tipos de cobertura:")
        for cobertura in produtoModel["coberturas"]:
          counter += 1
          print(str(counter) +" - " + str(cobertura))
        tipo_cobertura =  input("Escolha uma cobertura:")
        meu_produto.escolherCobertura(tipo_cobertura)
        quantidade_pedido = input("Quantos açais você deseja?")
        meu_produto.calcPrecoTotal(meu_produto.preco_produto, quantidade_pedido)
      elif(produtoModel["id"] == 3):
        meu_produto = produtos.AcaiCopo(produtoModel["Adicionais"], produtoModel  ["tamanhos"], produtoModel["Coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"],   produtoModel["ingredientes"])
        tamanho = input("Escolha o tamanho do Copo: ")
        meu_produto.escolherCopo(int(tamanho))
        print("Tipos de Adicionais:")
        counter = 0
        for adicionais in produtoModel["Adicionais"]:
          counter +=1
          print(str(counter) + " - " + adicionais)
        adicionais = input("Escolha os Adicionais: ")
        counter = 0
        for cobertura in produtoModel["Coberturas"]:
          counter += 1
          print(str(counter) + " - " + cobertura)
        cobertura = input("Escolha as Coberturas:")
        meu_produto.escolherAdicionais(adicionais)
        quantidade_pedido = input("Quantos açais você deseja ?")
  item.produto = meu_produto
  item.quantidade = int(quantidade_pedido)
  meu_pedido.listaProdutos.append(item)
  
  return meu_pedido
  
