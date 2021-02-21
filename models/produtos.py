from models import produto
import re
class AcaiNaBarca(produto.Produto):
  def __init__(self, complemento, tamanhosBarca, coberturaBarca):
    self.complementos = complemento
    self.tamanhosBarca = tamanhosBarca
    self.coberturas = coberturaBarca
  def escolherComplemento(self, value):
    indexValue = value - 1
    self.complementosSelecionados = self.complementos[indexValue]

  def escolherCobertura(self, value):
    index = value - 1
    self.coberturaSelecionada = self.coberturas[index]
  def escolherBarca(self, value):
    index = value - 1
    self.tamanhoBarcaSelecionada = self.tamanhosBarca[index]

class AcaiTigela(produto.Produto):
  def __init__(self, frutas, tamanhosTigela, cobertura):
    self.frutas = frutas
    self.tamanhosTigela = tamanhosTigela
    self.coberturas = cobertura
    self.frutasExtras = []
    self.precoFrutasExtrasTotal = 0.0
  def acaiAddFrutaExtra(self, quantidadeFrutasExtra):
    self.precoFrutasExtrasTotal = 2 * quantidadeFrutasExtra
  #override
  def calcPrecoTotal(self, preco, quantidade):
    self.quantidade = quantidade
    self.precoTotal = preco * quantidade + self.precoFrutasExtrasTotal
  def escolherFruta(self, value):
    try:
      value = re.sub('[^0-9]', '', value)
      fruta1 = int(value[0]) - 1
      fruta2 = int(value[1]) - 1
      fruta3 = int(value[2]) - 1
      self.frutasSelecionadas = [self.frutas[fruta1], self.frutas[fruta2], self.frutas[fruta3]]
    except:
      raise(Exception("Não foram informadas todas as três frutas!"))
      return None

  def escolherCobertura(self, value):
    index = value - 1
    self.coberturaSelecionada = self.coberturas[index]
  def escolherTigela(self, value):
    index = value - 1
    self.tamanhoTigelaSelecionada = self.tamanhosTigela[index]

class AcaiCopo(produto.Produto):
  def __init__(self, adicionais, tamanhosCopo, cobertura):
    self.adicionais = adicionais
    self.tamanhosCopo = tamanhosCopo
    self.coberturas = cobertura
  def escolherAdicionais(self, value):
    index = value - 1
    self.adicionaisSelecionados = self.adicionais[index]
  def escolherCobertura(self, value):
    index = value - 1
    self.coberturaSelecionada = self.coberturas[index]
  def escolherCopo(self, value):
    index = value - 1
    self.tamanhoCopoSelecionada = self.tamanhosCopo[index]
