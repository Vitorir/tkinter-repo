# nome = input('Digite um nome: ')
# lista = [char for char in nome]
# lista.reverse()
# print(lista)

notas = []
while True:
    nota = float(input("Digite uma nota: (ou digite -1 para parar)"))
    if nota == -1:
        break
    notas.append(nota)

media = sum(notas) / len(notas)
print(media)

if media >= 7:
    print("Aprovado!")
elif media < 5:
    print("Reprovado!")
elif 5 <= media < 7:
    print("Recuperacao!")

