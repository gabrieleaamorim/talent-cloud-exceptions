continuar = True
while continuar == True:
    try:
        nome = input("Digite seu nome completo: ")
        ano = int(input("Digite um ano de nascimento entre 1922 e 2021: "))
        print(nome, "nasceu em", ano, "e tem", 2024 - ano, "anos.")
        continuar = False
    except ValueError:
        print("Digite apenas números inteiros.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.") 
        continuar = False