from Classes import *
from Classes import E_commerce
import os

def main():
    contID = 0
    
    sair = False
    os.system("cls")
    pdt = 0

    Carlinhos = E_commerce("CARLINHOS-RALPH MOTOCAS", "Av. das Detonações, Nº86", 123456789)

    while sair == False:
        try:
            print("BEM-VINDO AO CARLINHOS-RALPH MOTOCAS!")
            menu = int(input("[1] Cadastrar \n[2] Login \n[3] Sair \nDigite a opção desejada: "))
            
            match menu:
                case 1:
                    os.system("cls")
                    print("--- CADASTRO DE CLIENTE ---")
                    print("INFORME OS SEUS DADOS")
                    contID += 1
                    id = contID
                    nome = input("Nome: ")
                    cpf = int(input("CPF: "))
                    tel = int(input("Telefone: "))
                    senha = input("Senha: ")

                    Carlinhos.cadastrarCliente(id, nome, cpf, tel, senha)

                    print("Usuário cadastrado!")
                    os.system("pause")
                    os.system("cls")

                case 2:
                    os.system("cls")
                    print("--- LOGIN ---")
                    cpf_login = int(input("Digite o CPF: "))
                    senha_login = input("Digite a senha: ")
                    
                    cliente_id = Carlinhos.login(cpf_login, senha_login)
                    if cliente_id is not None:
                        os.system("cls")
                        print(f"Bem-vindo, {Carlinhos.cliente[cliente_id][0]}!\n")

                        menu2 = int(input("\n[1] Cadastrar Produto \n[2] Listar Produtos \n[3] Comprar \n[4] Meu Carrinho \n[5] Excluir Produto do Carrinho \n \nDigite a opção desejada: "))
                        
                        match menu2:
                            case 1:
                                os.system("cls")
                                print("--- CADASTRAR PRODUTO ---")
                                print("\nPreencha as informações: \n")
                                pdt += 1
                                num = pdt

                                nomePd = input("Nome: ")
                                precoPD = int(input("Preço: "))
                                qnt = int(input("Quantidade: "))

                                Carlinhos.cadastrar_produtos(num, nomePd, precoPD, qnt)
                                
                                print("Produto cadastrado")
                            case 2:
                                os.system("cls")
                                print("--- LISTA DE PRODUTOS ---")
                                print("Produtos em estoque: ")
                                Carlinhos.listar_produtos()
                            case 3:
                                os.system("cls")
                                print("--- COMPRAS ---")
                                print("\nLista de Produtos Disponíveis:")
                                Carlinhos.listar_produtos()

                                self.produto[x] = valor[2] - 1

                                if cliente_id is not None:
                                    produto_id = int(input("Digite o número do produto que deseja comprar: "))
                                    
                                    if produto_id in Carlinhos.produto and Carlinhos.produto[produto_id][2] > 0:
                                        Carlinhos.adicionar_carrinho(cliente_id, produto_id)
                                        print("Produto adicionado ao carrinho!")
                                    else:
                                        print("Produto não encontrado ou não está disponível.")
                                else:
                                    print("CPF ou senha incorretos. Tente novamente.")
                                
                                os.system("pause")
                                os.system("cls")
                                
                            case 4:
                                os.system("cls")
                                print("--- MEU CARRINHO ---")
                                print("\nEsta é a lista de seus produtos!")
                            case 5:
                                os.system("cls")
                                print("--- EXCLUIR PRODUTO DO CARRINHO ---")
                            case _:
                                print("Opção inválida.") 
                    else:
                        print("CPF ou senha incorretos. Tente novamente.")
                    
                    os.system("pause")
                    os.system("cls") 
            
                case 3:
                    sair = True

                case _:
                    print("Valor Inválido!")   
                             
        except Exception as erro:
            print("Opção inválida.")
            print("Erro: ", erro.__class__.__name__)
            print("")       



# n1 = Produtos("Notebook", 4500)
# n2 = Produtos("Iphone", 8000)
# n3 = Produtos("Tablet", 2500)

# Carrinho_Cliente = Carrinho_Compra()

# Carrinho_Cliente.inserir_produto(n1)
# Carrinho_Cliente.inserir_produto(n2) 
# Carrinho_Cliente.inserir_produto(n3)

# print("--------------------------------------")
# print(Carrinho_Cliente.getLista(0).getNome())
# print(Carrinho_Cliente.getLista(0).getValor())
# print("--------------------------------------")

# Carrinho_Cliente.listar_produtos()
# print("--------------------------------------")

# Carrinho_Cliente.delProduto(2)

# Carrinho_Cliente.listar_produtos()
