import os
from Classes import *

def main():
    contID = 0
    sair = False
    pdt = 0

    Carlinhos = E_commerce("CARLINHOS-RALPH MOTOCAS", "Av. das Detonações, Nº828", 123456789)

    while not sair:
        try:
            os.system("cls")
            print("BEM-VINDO AO CARLINHOS-RALPH MOTOCAS!")
            menu = int(input("[1] Cadastrar\n[2] Login\n[3] Sair\nDigite a opção desejada: "))

            if menu == 1:  # Cadastro do Cliente
                os.system("cls")
                print("--- CADASTRO DE CLIENTE ---")
                print("INFORME OS SEUS DADOS")
                contID += 1
                id = contID
                nome = input("Nome: ")
                cpf = int(input("CPF: "))
                tel = int(input("Telefone: "))
                senha = input("Senha: ")

                Carlinhos.cadastrar_cliente(id, nome, cpf, tel, senha)

                print("Usuário cadastrado!")
                os.system("pause")

            elif menu == 2:  # Login do Cliente
                os.system("cls")
                print("--- LOGIN ---")
                cpf_login = int(input("Digite o CPF: "))
                senha_login = input("Digite a senha: ")

                cliente_id = Carlinhos.login(cpf_login, senha_login)
                if cliente_id is not None:
                    os.system("cls")
                    print(f"Bem-vindo, {Carlinhos.clientes[cliente_id].nome}!\n")
                    # Menu
                    while True:
                        menu2 = int(input("[1] Cadastrar Produto\n[2] Listar Produtos\n[3] Comprar\n[4] Meu Carrinho\n[5] Excluir Produto do Carrinho\n[6] Voltar ao Menu Principal\nDigite a opção desejada: "))
                        if menu2 == 1:  # Cadastrar Produtos
                            os.system("cls")
                            print("--- CADASTRAR PRODUTO ---")
                            print("\nPreencha as informações:\n")
                            pdt += 1
                            num = pdt

                            nomePd = input("Nome: ")
                            precoPd = int(input("Preço: "))
                            qtd = int(input("Quantidade: "))

                            Carlinhos.cadastrar_produto(num, nomePd, precoPd, qtd)

                            print("\nProduto cadastrado!")

                            os.system("pause")
                            os.system("cls")

                        elif menu2 == 2:  # Listar os produtos
                            os.system("cls")
                            print("--- LISTA DE PRODUTOS ---")
                            print("Produtos em estoque:\n")
                            Carlinhos.listar_produtos()
                            os.system("pause")
                            os.system("cls")

                        elif menu2 == 3:  # Compras
                            os.system("cls")
                            print("--- COMPRAS ---")
                            print("\nLista de Produtos Disponíveis:")
                            Carlinhos.listar_produtos()

                            if cliente_id not in Carlinhos.carrinhos:
                                Carlinhos.criar_carrinho(cliente_id)

                            produto_id = int(input("\nDigite o número do produto que deseja comprar: "))
                            qtdp = int(input("Selecione a quantidade que deseja comprar: "))

                            Carlinhos.adicionar_produto_carrinho(cliente_id, produto_id, qtdp)

                            os.system("pause")
                            os.system("cls")

                        elif menu2 == 4:  # Meu Carrinho
                            os.system("cls")
                            print("--- MEU CARRINHO ---")
                            Carlinhos.meu_carrinho(cliente_id)

                            os.system("pause")
                            os.system("cls")

                        elif menu2 == 5:  # Excluir produto do carrinho
                            os.system("cls")
                            print("--- EXCLUIR PRODUTO DO CARRINHO ---")
                            Carlinhos.meu_carrinho(cliente_id)
                            produto_num = int(input("\nDigite o número do produto que deseja excluir: "))
                            qtdp = int(input("Digite a quantidade que deseja remover: "))
                            Carlinhos.remover_produto_carrinho(cliente_id, produto_num, qtdp)

                            os.system("pause")
                            os.system("cls")

                        elif menu2 == 6:  # Voltar ao Menu Principal
                            break

                else:
                    print("CPF ou senha incorretos. Tente novamente.")
                    os.system("pause")
                    os.system("cls")

            elif menu == 3:
                sair = True

            else:
                print("Valor Inválido!")
                os.system("pause")
                os.system("cls")

        except Exception as erro:
            print("Opção inválida.")
            print("Erro:", erro.__class__.__name__)
            os.system("pause")
            os.system("cls")

