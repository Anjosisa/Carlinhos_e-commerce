# class E_commerce():
#     def __init__(self, nome, endereco, cnpj):
#         self.nome = nome
#         self.endereco = endereco
#         self.cnpj = cnpj
#         self.cliente = {}
#         self.produto = None
#         self.produtos = []
#         self.carrinho = {}
#         self.estoque = {}

class E_commerce():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}
        self.produtos = [] 
        self.carrinho = {}
        self.estoque = {}  

    def cadastrarCliente(self, id, nome, cpf, tel, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.senha = senha      
        self.cliente[self.id] = [self.nome, self.cpf, self.tel, self.senha]

    def login(self, cpf, senha):
        for id, cliente_info in self.cliente.items():
            _, cpf_salvo, _, senha_salva = cliente_info
            if cpf == cpf_salvo and senha == senha_salva:
                return id 
        return None

    def adicionar_carrinho(self, cliente_id, produto_id,qtd):
        if cliente_id in self.carrinho:
            self.carrinho[cliente_id].append(produto_id)
        else: 
            self.carrinho[cliente_id] = [produto_id]

        if produto_id in self.estoque and self.estoque[produto_id] > 0:
            self.estoque[produto_id] -= qtd
        elif produto_id.qtd in self.estoque and self.estoque[produto_id] > self.estoque:
            print("Quantidade indisponível")
        else:
            print("Produto não encontrado ou não está disponível.")
    

    # def listar_produtos(self):
    #     for chave, valor in self.produtos.items():
    #         print(f"{chave} - Nome: {valor[0]}, Valor: R${valor[1]}, Quantidade: {valor[2]}")

    def listar_produtos(self):
        print("--- LISTA DE PRODUTOS ---")
        for produto in self.produtos:
            print(f"{produto.num} - Nome: {produto.getNomePD}, Valor: R${produto.getPrecoPD}, Quantidade: {produto.getQtd}")



    # def excluir_produto_carrinho(self, vetor):
    #     self.vetor_lista = vetor-1
    #     return self.listar_pr_produtos.pop(vetor)


    def cadastrar_produtos(self, nomePd, precoPd, qtd):
        produto = Produtos(self.produto)
        self.produtos.append(produto)
       
    def meu_carrinho(self, nomePd, quantPd, precoPd):
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.quantPd = quantPd
        self.valor_Total = 0

        self.valor_Total = self.precoPd * quantPd
        
        print("--- CARRINHO DE COMPRAS ---")
        for chave, valor in self.produtos.items():
            print(f"{chave} - Produto: {valor[0]}, Valor: R${valor[1]}")

        print(f"O Valor total é R${self.valor_Total}")

class Produtos:
    def __init__(self, num, nomePd, precoPd, qtd):
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.qtd = qtd
        self.num = num
        self.produto = {}
    
    def dicionario_produto(self, num, nomePd, precoPd, qtd):
        self.produto[num] = [self.nomePd, self.precoPd, self.qtd]


    def getNomePD(self):
        return self.nomePd
    
    def getPrecoPD(self):
        return self.precoPd

    def getQtd(self):
        return self.qtd


        
