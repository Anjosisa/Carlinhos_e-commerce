class Carrinho_Compra:
    lista_compras = []

    def inserir_produto(self, produto):
        self.produto = produto
        self.lista_compras.append(self.produto)

    def listar_produtos(self):
        self.cont = 0
        for produto in self.lista_compras:
            self.cont += 1
            print(f"{self.cont}: Nome: {produto.getNome()}, Valor: R${produto.getValor()}")

    def getLista(self, vetor):
        return self.lista_compras[vetor]
    
    def delProduto(self, vetor):
        self.vetor_lista = vetor-1
        return self.lista_compras.pop(vetor)

class Produtos:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor

    