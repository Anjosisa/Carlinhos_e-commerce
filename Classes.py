class E_commerce():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente = {}
        self.produto = {}
        self.carrinho = {}

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

    def adicionar_carrinho(self, cliente_id, produto_id):
        if cliente_id in self.carrinho:
            self.carrinho[cliente_id].append(produto_id)
        else:
            self.carrinho[cliente_id] = [produto_id]

    def cadastrar_produtos(self, num, nomePd, precoPd, qtd):
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.qtd = qtd
        self.num = num
        self.produto[num] = [self.nomePd, self.precoPd, self.qtd]

        
    def getNomePD(self):
        return self.nomePd
    
    def getPrecoPD(self):
        return self.precoPd

    def getQtd(self):
        return self.qtd

    def listar_produtos(self):
        for chave, valor in self.produto.items():
            print(f"{chave} - Nome: {valor[0]}, Valor: R${valor[1]}, Quantidade: {valor[2]}")
            

    def getLista(self, vetor):
        return self.lista_compras[vetor]

    def excluir_carrinho(self, vetor):
        self.vetor_lista = vetor-1
        return self.lista_compras.pop(vetor)

class Produtos:

    def meu_carrinho(self, nomePd, quantPd, precoPd, valor_Total):
        self.nomePd = nomePd
        self.precoPd = precoPd
        self.quantPd = quantPd
        self.valor_Total = valor_Total

        self.valor_Total = self.precoPd * quantPd
        
        for chave, valor in self.produto.items():
            print(f"{chave} - Produto: {valor[0]}, Valor: R${valor[1]}, Quantidade: {valor[2]}")

        print(f"O Valor total é R${valor_Total}")
