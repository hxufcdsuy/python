import os

os.system("cls || clear")
opcao = input("digite a opção desejada:")
numeroa = int(input("digite o primeiro número:"))
numerob = int(input("digite o segundo número:"))


match(opcao):
    case "+":

        resultado= numeroa + numerob
    case "-":

       resultado= numeroa - numerob
    case "*":

       resultado= numeroa * numerob
    case "/":

        resultado= numeroa / numerob    
    case _:
        print("operação invalida")
    
        print(" === exibindo resultados === \n")
    
    
print(f"resultado {resultado}.")


    


    


