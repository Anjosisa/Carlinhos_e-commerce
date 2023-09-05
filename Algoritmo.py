from Classes import *
from Classes import E_commerce
import os

def main():
    contID = 0
    
    sair = False
    os.system("cls")

    CARLINHOS = E_commerce("CARLINHOS-RALPH MOTOCAS", "Av. das Detonações, Nº86", 123456789)

    while sair == False:
        try:
            print("BEM-VINDO AO CARLINHOS-RALPH MOTOCAS!")
            menu = int(input("[1] Cadastrar \n[2] Login \n[3] Sair \nDigite a opção desejada: "))
            
            match menu:
                case 1:
                    os.system("cls")
                    print("--- CADASTRO DE CLIENTE ---")
                    print("INFORME OS SEUS DADOS")
                    id = contID + 1
                    nome = input("Nome: ")
                    cpf = int(input("CPF: "))
                    tel = int(input("Telefone: "))
                    senha = input("Senha: ")

                    CARLINHOS.cadastrarCliente(id, nome, cpf, tel, senha)

                    print("Usuário cadastrado!")
                    os.system("pause")
                    os.system("cls")

                case 2:
                    os.system("cls")
                    print("--- LOGIN ---")
                    cpf_login = int(input("Digite o CPF: "))
                    senha_login = input("Digite a senha: ")

                    # Verifique se o CPF existe nos clientes cadastrados
                    if cpf_login in [cliente['cpf'] for cliente in CARLINHOS.cliente.values()]:
                        cliente = CARLINHOS.cliente[cpf_login]
                        if senha_login == cliente[3]:  # A senha está na posição 3 da lista de informações do cliente
                            print("Login bem-sucedido!")
                            # Aqui você pode prosseguir com o que desejar após o login
                        else:
                            print("Senha incorreta. Tente novamente.")
                    else:
                        print("CPF não encontrado. Verifique suas credenciais.")
                    
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
# print("--------------------------------------")