class Cliente:
    def __init__(self, id, nome, cpf, tel, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.senha = senha

class Produto:
    def __init__(self, num, nomePd, precoPd, qtd):
        self.num = num
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.qtd = qtd

class Carrinho:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto, quantidade):
        # Adiciona os produtos no carrinho
        if produto.num in self.produtos:
            self.produtos[produto.num] += quantidade
        else:
            self.produtos[produto.num] = quantidade

    def remover_produto(self, produto, quantidade):
        # Remove os produtos do carrinho
        if produto.num in self.produtos:
            self.produtos[produto.num] -= quantidade
            if self.produtos[produto.num] <= 0:
                del self.produtos[produto.num]

class E_commerce:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = {}
        self.produtos = {}
        self.carrinhos = {}

    def cadastrar_cliente(self, id, nome, cpf, tel, senha):
        cliente = Cliente(id, nome, cpf, tel, senha)
        self.clientes[id] = cliente

    def login(self, cpf, senha):
        for id, cliente in self.clientes.items():
            if cpf == cliente.cpf and senha == cliente.senha:
                return id
        return None

    def cadastrar_produto(self, num, nomePd, precoPd, qtd):
        produto = Produto(num, nomePd, precoPd, qtd)
        self.produtos[num] = produto

    def listar_produtos(self):
        for num, produto in self.produtos.items():
            print(f"{num} - Nome: {produto.nomePd}, Valor: R${produto.precoPd}, Quantidade: {produto.qtd}")

    def adicionar_produto_carrinho(self, cliente_id, produto_id, quantidade):
        if cliente_id in self.carrinhos:
            carrinho = self.carrinhos[cliente_id]
            if produto_id in self.produtos:
                produto = self.produtos[produto_id]
                carrinho.adicionar_produto(produto, quantidade)
            else:
                print("Produto não encontrado.")
        else:
            print("Carrinho não encontrado.")

    def remover_produto_carrinho(self, cliente_id, produto_id, quantidade):
        if cliente_id in self.carrinhos:
            carrinho = self.carrinhos[cliente_id]
            if produto_id in self.produtos:
                produto = self.produtos[produto_id]
                carrinho.remover_produto(produto, quantidade)
            else:
                print("Produto não encontrado.")
        else:
            print("Carrinho não encontrado.")

    def meu_carrinho(self, cliente_id):
        if cliente_id in self.carrinhos:
            carrinho = self.carrinhos[cliente_id]
            print("Produtos no carrinho:")
            for produto_num, quantidade in carrinho.produtos.items():
                produto = self.produtos[produto_num]
                print(f"Nome: {produto.nomePd}, Quantidade: {quantidade}")
        else:
            print("Carrinho não encontrado.")

    def criar_carrinho(self, cliente_id):
        # Cria um carrinho para o cliente
        self.carrinhos[cliente_id] = Carrinho()
