continuar = True
while continuar == True:
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        print(num1, "/", num2, "=", num1/num2)
        continuar = False
    except ValueError:
        print("Digite apenas números inteiros.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.") 
        continuar = False