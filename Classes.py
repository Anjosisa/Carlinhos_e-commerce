class E_commerce():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}

    def cadastrarCliente(self, id, nome, cpf, tel, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.senha = senha      
        self.cliente[self.id] = [self.nome, self.cpf, self.tel, self.senha]

    lista_compras = []

    def adicionar_carrinho(self, produto):
        self.produto = produto
        self.lista_compras.append(self.produto)

    def listar_produtos(self):
        self.cont = 0
        for produto in self.lista_compras:
            self.cont += 1
            print(f"{self.cont}: Nome: {produto.getNome()}, Valor: R${produto.getValor()}")

    def getLista(self, vetor):
        return self.lista_compras[vetor]
    
    def excluir_carrinho(self, vetor):
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
    
    def cadastrar_produtos(self,nome, valor):
        self.nome = nome 
        self.valor = valor 