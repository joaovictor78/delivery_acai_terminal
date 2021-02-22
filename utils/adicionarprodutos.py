from models import produtos, pedido
import json
meu_pedido = pedido.Pedido()
def adicionarProduto(item):
  while(True):
    try:
      tipoAcai = int(input("Escolha um dos nossos formatos de açai e aproveite:): "))
      if(tipoAcai > 3 or tipoAcai <= 0):
        print("Esta respota é inválida, tente novamente")
        continue
      break        
    except ValueError:
      print("Tivemos um problema com o tipo de dado informado, tente novamente!")
      continue
  produtos_disponiveis = open("bd_fake/produtos.txt","r")
  for produto in produtos_disponiveis:
    produtoModel =  json.loads(produto)
    if (tipoAcai == produtoModel["id"]):
      print("Você escolheu nosso delicioso açai {} :)".format(produtoModel["tipo"]).lower())
      print("Tamanhos: ")
      counter = 0
      for tamanho in produtoModel["tamanhos"]:
        counter += 1
        print(str(counter) + " - " +str(tamanho) + "g")
      if(produtoModel["id"] == 1):
        meu_produto = produtos.AcaiNaBarca(produtoModel["complementos"],   produtoModel["tamanhos"], produtoModel["coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"],   produtoModel["ingredientes"])
        while(True):
          try:
            tamanho = int(input("Escolha o tamanho: "))
            if(tamanho > counter or tamanho <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue 
        print("Tipos de complementos:")
        counter = 0
        for complemento in produtoModel["complementos"]:
          counter +=1
          print(str(counter) + " - " + complemento)
        while(True):
          try:
            complemento_selecionado = int(input("Selecione um complemento: "))
            if(complemento_selecionado > counter or complemento_selecionado <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherComplemento(complemento_selecionado)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue 
        print("Tipos de coberturas:")
        counter = 0
        for cobertura in produtoModel["coberturas"]:
          counter +=1
          print(str(counter) + " - " + cobertura)
        while(True):
          try:
            cobertura_selecionada = int(input("Selecione uma cobertura: "))
            if(cobertura_selecionada > counter or cobertura_selecionada <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherCobertura(cobertura_selecionada)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
        while(True):
          try:     
            quantidade_pedido = int(input("Quantos açais você deseja? "))
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue          
      elif(produtoModel["id"] == 2):
        meu_produto = produtos.AcaiTigela(produtoModel["frutas"], produtoModel  ["tamanhos"], produtoModel["coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"],   produtoModel["ingredientes"])
        while(True):
          try:
            tamanho = int(input("Escolha o tamanho do seu açai: "))
            if(tamanho > 2 or tamanho <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherTigela(tamanho)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
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
          while(True):
            try:
              frutas_selecionadas = input("Escolha as frutas do seu açai: ")
              meu_produto.escolherFruta(frutas_selecionadas)
              break
            except Exception as error:
              print("Tivemos um erro, tente novamente")
              print(error)
              continue
          if(adicionarFrutaExtra == False):
            resp = input("Deseja Adicionar mais frutas por apenas um adicional de 2 Reais? S/N ").upper()
            while(resp == "S"):
              print("Tipos de Frutas:")
              counter = 0
              for frutas in produtoModel["frutas"]:
                counter += 1
                print(str(counter) + " - " + frutas)
              while(True):
                try:
                  frutaExtraSelecionada = int(input("Selecione uma das frutas acima: "))
                  if(frutaExtraSelecionada > counter or frutaExtraSelecionada <= 0):
                    print("Esta respota é inválida, tente novamente")
                    continue                    
                  break
                except ValueError:
                  print("Tivemos um problema com o tipo de dado informado, tente novamente")
                  continue
              index = frutaExtraSelecionada - 1
              listFrutasAcaiTigela =  meu_produto.frutasExtras
              listFrutas = meu_produto.frutas
              if(listFrutas[index] in listFrutasAcaiTigela):
                print("Essa fruta já foi adicionada")
              else:
                numeroDeFrutasExtras = numeroDeFrutasExtras + 1
                meu_produto.frutasExtras.append(meu_produto.frutas[index])
                resp = input("Deseja adicionar mais alguma fruta? S/N ").upper()
                if(resp == "N"):
                  meu_produto.acaiAddFrutaExtra(numeroDeFrutasExtras)
                elif(resp == "S"):
                  continue
        counter = 0
        print("Tipos de cobertura:")
        for cobertura in produtoModel["coberturas"]:
          counter += 1
          print(str(counter) +" - " + str(cobertura))
        while(True):
          try:
            tipo_cobertura =  int(input("Escolha uma cobertura:"))
            if(tipo_cobertura > counter or tipo_cobertura <= 0):
                print("Esta respota é inválida, tente novamente")
                continue
            else:
              meu_produto.escolherCobertura(tipo_cobertura)
              break
          except ValueError:
            print("Tivemos um erro com o tipo de dado informado, tente novamente")
            continue
        while(True):
          try:     
            quantidade_pedido = int(input("Quantos açais você deseja? "))
            meu_produto.calcPrecoTotal(meu_produto.preco_produto, quantidade_pedido)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
      elif(produtoModel["id"] == 3):
        meu_produto = produtos.AcaiCopo(produtoModel["Adicionais"], produtoModel  ["tamanhos"], produtoModel["Coberturas"])
        meu_produto.setAtributos(produtoModel["preco"], produtoModel["descricao"], produtoModel["ingredientes"])
        while(True):
          try:
            tamanho = int(input("Escolha o tamanho do Copo: "))
            if(tamanho > 3 or tamanho <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherCopo(tamanho)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
        print("Tipos de Adicionais:")
        counter = 0
        for adicionais in produtoModel["Adicionais"]:
          counter +=1
          print(str(counter) + " - " + adicionais)
        while(True):
          try:
            adicionais = int(input("Escolha os Adicionais: "))
            if(adicionais > counter or adicionais <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherAdicionais(adicionais)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
        print("Tipos de Coberturas:")
        counter = 0
        for cobertura in produtoModel["Coberturas"]:
          counter += 1
          print(str(counter) + " - " + cobertura)
        while(True):
          try:
            cobertura = int(input("Escolha as Coberturas: "))
            if(cobertura > counter or cobertura <= 0):
              print("Esta respota é inválida, tente novamente")
              continue
            else:
              meu_produto.escolherCobertura(cobertura)
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
        while(True):
          try:     
            quantidade_pedido = int(input("Quantos açais você deseja? "))
            break
          except ValueError:
            print("Tivemos um problema com o tipo de dado informado, tente novamente!")
            continue
  item.produto = meu_produto
  item.quantidade = quantidade_pedido
  meu_pedido.listaProdutos.append(item)
  
  return meu_pedido