import time
import os

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal '''
    input('\nDigite uma tecla para voltar ao menu principal')

def atividade1():
    clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
    for cliente in clientes:
        print(cliente)

def atividade2():
    contador = 0
    while contador < 10:
        print("Processando dados...")
        contador += 1

def atividade3():
    for i in range(5):
        print('Bem-vindo ao Buscante!')

def atividade4():
    valores = [10, 20, 30, 40, 50]
    soma = sum(valores)
    print(f"A soma total das receitas é: {soma}")

def atividade5():
    projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
    for projeto in projetos:
        print(projeto if projeto else 'Projeto ausente')

def atividade6():
    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
    for livro in livros:
        if livro == "O Hobbit":
            print(f'Livro encontrado: {livro}')
            break

def atividade7():
    Estoque = 5
    while Estoque > 0:
        Estoque -= 1
        if Estoque > 0:
            print(f"Venda realizada! Estoque restante: {Estoque}")
        else:
            print("Estoque esgotado\n")
        time.sleep(1)

def atividade8():
    for segundos in range(10, 0, -1):
        if segundos % 2 == 0:
            print(f"Restam {segundos} segundos!")
        else:
            print(f"A contagem regressiva continua {segundos} segundos restantes")
        time.sleep(0.1)
    print("Aproveite a promoção agora\n")

def atividade9():
    livros = [
        {"nome": "1984", "estoque": 5},
        {"nome": "Dom Casmurro", "estoque": 0},
        {"nome": "O Pequeno Príncipe", "estoque": 3},
        {"nome": "O Hobbit", "estoque": 0},
        {"nome": "Orgulho e Preconceito", "estoque": 2}
    ]
    for livro in livros:
        if livro['estoque'] == 0:
            print(f"Livro esgotado: {livro['nome']}")
            continue
        print(f"Livro disponível: {livro['nome']}")

def atividade10():
    while True:
        nome_de_usuario = input('Informe seu nome de usuário: ')
        senha = input('Informe a senha: ')

        if len(nome_de_usuario) < 5:
            print('O nome de usuário deve ter pelo menos 5 caracteres!')
            continue

        if len(senha) < 8:
            print('A senha deve ter 8 dígitos no mínimo!')
            continue

        print('Cadastro realizado com sucesso!')
        break

# ---------------- MENU ----------------
def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Atividade 1")
        print("2 - Atividade 2")
        print("3 - Atividade 3")
        print("4 - Atividade 4")
        print("5 - Atividade 5")
        print("6 - Atividade 6")
        print("7 - Atividade 7")
        print("8 - Atividade 8")
        print("9 - Atividade 9")
        print("10 - Atividade 10")
        print("0 - Sair")

        try:
            escolha = int(input("Digite o número da atividade (0 a 10): "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if escolha == 0:
            print("Saindo...")
            break
        elif escolha == 1:
            atividade1()
        elif escolha == 2:
            atividade2()
        elif escolha == 3:
            atividade3()
        elif escolha == 4:
            atividade4()
        elif escolha == 5:
            atividade5()
        elif escolha == 6:
            atividade6()
        elif escolha == 7:
            atividade7()
        elif escolha == 8:
            atividade8()
        elif escolha == 9:
            atividade9()
        elif escolha == 10:
            atividade10()
        else:
            print("Atividade inválida!")

        voltar_ao_menu_principal()

if __name__ == "__main__":
    main()