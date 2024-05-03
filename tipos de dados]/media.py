import os
os.system("cls || clear")
nome = input( "digite o nome:" )
primeiraNota = float(input("digite a nota: "))
segundaNota = float(input("digite a nota: "))
terceiraNota = float(input("digite a nota: "))
idade = int(input("idade: "))

media = (primeiraNota+ segundaNota+terceiraNota)/3

print("=== exibindo resultado === \n")
print(f"MEDIA: {media}")
print(f"nome: {nome}")
print(f"idade: {idade}")
if (media < 7):
    print("reprovado")
else: print("aprovado")